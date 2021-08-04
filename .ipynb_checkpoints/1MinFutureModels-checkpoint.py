# %%
import pandas as pd

df = pd.read_csv("~/Documents/GitHub/Project/ignore_folder/1min_ml_1000_tsvd",compression="zip")

#%%


#%%
X,y = df[df.columns[1:1001]], df[df.columns[1001]]

# %%
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

regr = MLPRegressor(hidden_layer_sizes = 5000, max_iter=50000)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33, shuffle=False)

regr.fit(X_train, y_train)

#%%
regr.score(X_test, y_test)