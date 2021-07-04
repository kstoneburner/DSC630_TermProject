import os
import sys
import time
from datetime import date
from datetime import datetime
import time
import json
import platform

import stoneburner
#//*** Custom Functions:
#//*** mr_clean_text(input_series)
#//*** tokenize_series(input_series)
#//*** remove_stop_words(input_series)

# //*** Imports and Load Data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#//*** Use the whole window in the IPYNB editor
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
subreddits = ["wallstreetbets", "stocks", "wallstreetbetsOGs", "spacs", "investing", "pennystocks", "stockmarket", "options", "robinhoodpennystocks", "wallstreetbetsnew", "smallstreetbets"]
filepath = ".\\data\\"
filename_suffix = "_comments.csv.zip"
#//*** Maximize columns and rows displayed by pandas
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', None)

#//*** Input_filename: Comments to Process.
#//*** This will eventually be a list of files
#input_filename  =".\\data\\wallstreetbets_comments.csv.zip"

#//*** Path to processed files
output_filename = ".\\data\\processed_reddit_basic_v3.csv.zip"

#//*** Path to the stock ticker JSON file
stock_ticker_filename = ".\\data\\stock_tickers.json"

#//*** Convert Path to Mac formatting if needed
if platform.system() == 'Darwin':
    output_filename = output_filename.replace("\\","/")
    stock_ticker_filename = stock_ticker_filename.replace("\\","/")

#//*** Load the Stock Tickers
f = open(stock_ticker_filename, "r")
symbols = json.loads(f.read())['symbols']
f.close()

print(symbols)
#//*** Convert symbols to lower case
symbols = [x.lower() for x in symbols]



raw_df = pd.DataFrame()

start_time = time.time()

#//*** Load each Subreddit for Aggregation
for subreddit in subreddits:
    #//*** Filepath + subreddit name + csv.zip
    input_filename = filepath+subreddit+filename_suffix

    #//*** Convert Path to Mac formatting if needed
    if platform.system() == 'Darwin':
        input_filename = input_filename.replace("\\","/")
   
    print(f"Reading Compressed CSV: {input_filename}")
    
    #//*** Read Each DataFrame and combine with raw_df
    raw_df = pd.concat([raw_df,pd.read_csv(input_filename,compression='zip' )])

#//*** Reset the index, since multiple indexes have been combined
raw_df.reset_index(drop=True, inplace=True)

print(f"Files Loaded: {round(time.time()-start_time,2)}s")
print(f"Total Records: {len(raw_df)}")
    
raw_df['body'] = raw_df['body'].astype('str')

#//*** Convert UTC to date (not datetime)
#//** Second pass goes from 12-21 to 4-19
try:
    raw_df['created_utc'] = raw_df['created_utc'].apply(lambda x: date.fromtimestamp(x))
except:
    print()

#//*************************************************************************
#//*** Clean the Body Text, Tokenize and Remove Stop Words.
#//*************************************************************************
raw_df['clean'] = stoneburner.remove_stop_words(stoneburner.tokenize_series(stoneburner.mr_clean_text(raw_df['body'],{"remove_empty":False})))

#//*** Detokenize the clean column as tfidf
raw_df['tfidf'] = raw_df['clean'].apply(lambda x: ' '.join(x))

print(raw_df.tail())

#//*** Encode Comments
df = stoneburner.encode_comments(raw_df)

#//*** Aggregate and Process Comments
ag_df = stoneburner.aggregate_comments(df)
ag_df

#//*** Write File to disk
ag_df.to_csv(output_filename,compression="zip",index=False) 
