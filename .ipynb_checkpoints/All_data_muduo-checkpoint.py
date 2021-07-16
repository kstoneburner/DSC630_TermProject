## This loads a small test file of the first 5k comments with stock values ##
# The tfidf is two files. I'm not sure if they are the same thing or not.

# One contains the sparse matrix, the other has the vocabulary and parameters.

# Scikit Learn tfidf: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

import pickle
import pandas as pd

#//*** Load the tfidf sparse matrix
output_filename = "./data/processed_reddit_v4_1min_testdata_tfidf_matrix.pkl"
infile = open(output_filename,'rb')
t_tfidf_matrix = pickle.load(infile)
infile.close()

#//*** Load the tfidf that contains parameters and vocabulary
output_filename = "./data/processed_reddit_v4_1min_testdata_tfidf.pkl"
infile = open(output_filename,'rb')
t_tfidf = pickle.load(infile)
infile.close()

#//*** Load the test dataset
input_filename = "./data/processed_reddit_v4_1min_amc_stock_comments_test.pkl"
test_df = pd.read_pickle(input_filename)

input_file1 = "./ignore_folder/processed_reddit_v4_1min_amc_.pkl.zip"
input_file2 = "./ignore_folder/processed_reddit_v4_amc_1min_uncompressed.pkl"
input_file3 = "./ignore_folder/processed_reddit_v4_amc_1min_csv.zip"
#big_df = pd.read_pickle(input_file)
big_df = pd.read_csv(input_file3)

t_tfidf_dense = pd.DataFrame(t_tfidf_matrix.todense())