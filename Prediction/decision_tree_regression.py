"""
@author: Vivsvaan Sharma
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error 


dataset = pd.read_csv('2014_trainingSet2.csv')
X = dataset.iloc[:, 0:4].values
Y = dataset.iloc[:, 4:6].values
dataset2 = pd.read_csv('2014_testSet.csv')
X2 = dataset2.iloc[:,0:4].values
Y2 = dataset2.iloc[:,4:6].values
#encoding data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
X2[:, 0] = labelencoder_X.fit_transform(X2[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
X2 = onehotencoder.fit_transform(X2).toarray()
#avoiding dummy variable trap
X = X[:, 1:]
X2 = X2[:, 1:]

#train and test set   1213
#from sklearn.model_selection import train_test_split
#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state = 0)
#X_test = X[1143:1283,:]
#Y_test = Y[1143:1283,:]
#X_train = X[:,:]
#Y_train = Y[:,:]
#for i in range(1143,1284):
#    X_train = np.delete(X_train,i,0)
#    Y_train = np.delete(Y_train,i,0)
X_train = X
Y_train = Y
X_test = X2
Y_test = Y2

# feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_Y = StandardScaler()
Y_train = sc_Y.fit_transform(Y_train)
Y_test = sc_Y.transform(Y_test)

# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)

#Mean Squarred Error and Score
print("mse: ", mean_squared_error(Y_pred, Y_test))
print("score: ", regressor.score(X_test, Y_test))

# Visualising the Decision Tree Regression results

#total valid votes polled in state
plt.scatter(range(2569), dataset.iloc[:,4], color = 'red')
plt.plot(range(2569), dataset.iloc[:,4], color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('States')
plt.ylabel('Total votes polled in state')
plt.show()

#total valid votes polled by party
plt.scatter(range(35), dataset.iloc[:,5], color = 'red')
plt.plot(range(2569), dataset.iloc[:,5], color = 'red')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('States')
plt.ylabel('Total votes polled by party')
plt.show()
