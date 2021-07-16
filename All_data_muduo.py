import pandas as pd

input_file1 = "./ignore_folder/processed_reddit_v4_1min_amc_stock_comments.csv.zip"

input_file2 = "./ignore_folder/processed_reddit_v4_1min_tfidf_matrix.pkl"
input_file3 = "./ignore_folder/processed_reddit_v4_1min_tfidf.pkl"

f1 = pd.read_csv(input_file1)
f2 = pd.read_pickle(input_file2)
df = pd.DataFrame(f2.toarray(),index = f1["time"])
f1 = f1.drop("token", axis = 1)