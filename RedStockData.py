import os
import sys
# //*** Imports and Load Data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#//*** Maximize columns and rows displayed by pandas
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', None)
red = pd.read_csv("./data/processed_reddit_basic_v1.csv.zip", )
red.shape
stocks = pd.read_csv("./stocks/gme_daily.csv.zip", )
stocks = stocks.sort_values(by="date")
merged = red.merge(stocks)