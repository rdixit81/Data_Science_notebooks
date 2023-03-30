# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 12:30:27 2021

@author: win 10
"""

import matplotlib as plt
import sklearn as sk
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
import numpy as np

df_diabitic = datasets.load_diabetes()

#print(df_diabitic.keys())
#['data', 'target', 'DESCR', 'feature_names']

#print(df_diabitic.data)

#print(df_diabitic.DESCR)


#Taking one lablea nad one feature for simple linear regression


df_diabitic_X = df_diabitic.data
#print(df_diabitic_X)
#df_diabitic.reset_index(level=0, inplace=True)
#df_diabitic=featuredfs_reduced.drop(['index'], axis = 1)
df_diabitic_X_train = df_diabitic_X[:-30]
print(df_diabitic_X_train)
df_diabitic_X_test = df_diabitic_X[-30:]
print(df_diabitic_X_test)

df_diabitic_Y_train = df_diabitic.target[:-30]
df_diabitic_Y_test = df_diabitic.target[-30:]

model = linear_model.LinearRegression()

model.fit(df_diabitic_X_train, df_diabitic_Y_train)

df_diabitic_Y_predict = model.predict(df_diabitic_X_test)

print("Meanin sqaure error is: ", mean_squared_error(df_diabitic_Y_test, df_diabitic_Y_predict))
