# %%
import pandas as pd

df = pd.read_csv("~/Documents/GitHub/Project/ignore_folder/1min_ml",compression="zip")

#%%
X,y = df[df.columns[1:101]], df[df.columns[101]]

# %%
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

regr = MLPRegressor(max_iter=1000)

X_train, X_test, y_train, y_test = train_test_split(X,y)

regr.fit(X_train, y_train)

scores

