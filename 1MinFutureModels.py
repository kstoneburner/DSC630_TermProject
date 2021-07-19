# %%
import pandas as pd

df = pd.read_csv("~/Documents/GitHub/Project/ignore_folder/1min_ml_1000_pca",compression="zip")

#%%
X,y = df[df.columns[1:1001]], df[df.columns[101]]

# %%
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

regr = MLPRegressor(hidden_layer_sizes = 5000, max_iter=50000)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33, shuffle=False)

regr.fit(X_train, y_train)

#%%
regr.score(X_test, y_test)

#%%
regr.c
# %%
score = cross_val_score(regr, X,y,n_jobs=-1,cv=3)
# %%
regr_predict = regr.predict(X_test)
# %%
import numpy as np
err2= np.sqrt(abs((np.square(regr_predict) - np.square(y_test.values)))).sum()
mean_err = err2/len(y_test)
rmse = np.sqrt(mean_err)

#%%
import matplotlib.pyplot as plt
plt.plot(range(len(regr_predict[0:200])), regr_predict[0:200])
plt.plot(range(len(y_test[0:200])), y_test[0:200])

# plot(x= range(len(y_test)), y=y_test)
# %%
