"""
Created on Thu Jan 24 11:37:51 2019

@author: vivs
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error 

dataset = pd.read_csv('2014_ml_trainingSet.csv')
X = dataset.iloc[:, 0:4].values
Y = dataset.iloc[:, 4:6].values

#encoding data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

#avoiding dummy variable trap
X = X[:, 1:]


#train and test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_Y = StandardScaler()
Y_train = sc_Y.fit_transform(Y_train)
Y_test = sc_Y.transform(Y_test)

#linear regression
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(X_train, Y_train)
Y_pred = linear_reg.predict(X_test)



Y_poly_pred = linear_reg2.predict(poly_reg.fit_transform(X_test))


print("mse: ", mean_squared_error(Y_pred, Y_test))
print("score: ", linear_reg.score(X_test, Y_test))







