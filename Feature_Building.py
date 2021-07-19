#%%
import pandas as pd

input_file1 = "./ignore_folder/processed_reddit_v4_1min_amc_stock_comments.csv.zip"

input_file2 = "./ignore_folder/processed_reddit_v4_1min_tfidf_matrix.pkl"

f1 = pd.read_csv(input_file1)
X = pd.read_pickle(input_file2)

S1 = pd.Series((f1["open"].values+ f1["close"].values+ f1["high"].values + f1["low"].values)/4)

lst = []
lst.extend(S1[1:])
lst.append(lst[-1])
y = (S1/pd.Series(lst))-1

# %%
from sklearn.decomposition import TruncatedSVD
tsvd = TruncatedSVD(100)
X = tsvd.fit_transform(X,y)

# %%
df = pd.DataFrame(X)
df["y"] = y
# %%
df.to_csv("1min_ml", compression="zip")