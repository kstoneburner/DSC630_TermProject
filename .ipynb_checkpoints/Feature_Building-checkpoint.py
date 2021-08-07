#%% Reading Files
import pandas as pd

input_file1 = "./ignore_folder/processed_reddit_v4_1min_amc_stock_comments.csv.zip"

input_file2 = "./ignore_folder/processed_reddit_v4_1min_tfidf_matrix.pkl"

f1 = pd.read_csv(input_file1)
X = pd.read_pickle(input_file2)

#%% Getting an average of prices of that minute as the target variable
S1 = pd.Series((f1["open"].values+ f1["close"].values+ f1["high"].values + f1["low"].values)/4)

#%% Off-shifting target variable 1 minute 
lst = []
lst.extend(S1[1:])
lst.append(lst[-1])
y = (S1/pd.Series(lst))-1
#%%
# %%
from sklearn.decomposition import TruncatedSVD
tsvd = TruncatedSVD(1000)
X_1000_tsvd = tsvd.fit_transform(X,y)

#%%
tsvd.explained_variance_.sum()
# %%
df = pd.DataFrame(X_1000_tsvd)
df["Time"] = f1["time"]
df["y"] = y
# %%
df.to_csv("1min_1000_tsvd", compression="zip")