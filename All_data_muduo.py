import pandas as pd

input_file1 = "GitHub/Project/ignore_folder/processed_reddit_v4_1min_amc_stock_comments.csv.zip"

input_file2 = "GitHub/Project/ignore_folder/processed_reddit_v4_1min_tfidf_matrix.pkl"

f1 = pd.read_csv(input_file1)
f2 = pd.read_pickle(input_file2)
df = pd.DataFrame(f2.toarray(),index = f1["time"])

lst1 = list((f1["open"].values + f1["close"].values + f1["high"].values + f1["low"].values)/4)

lst2 = []
lst2.extend(df.price[1:])
lst2.append(df.price[-1])
lst2 = (lst1/lst2)-1
y = lst2.values

X = df[df.columns[~df.columns.isin(['price'])]]