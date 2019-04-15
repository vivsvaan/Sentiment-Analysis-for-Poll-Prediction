"""
@author: vivs
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error 

dataset = pd.read_csv('2014_trainingSet.csv')
X = dataset.iloc[:, 0:4].values
Y = dataset.iloc[:, 4:6].values
dataset2 = pd.read_csv('2014_testSet.csv')
X2 = dataset.iloc[:,0:4].values
Y2 = dataset.iloc[:,4:6].values

#encoding data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
X2[:, 0] = labelencoder_X.transform(X2[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
X2 = onehotencoder.transform(X2).toarray()
#avoiding dummy variable trap
X = X[:, 1:]
X2 = X2[:, 1:]

#train and test set
#from sklearn.model_selection import train_test_split
#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
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
#for i in range(144):
#    Y_test[i,0] = Y_test[i,0]/1000
#    Y_test[i,1] = Y_test[i,1]/1000

#for i in range(2569):
#    Y_train[i,0] = Y_train[i,0]/1000
#    Y_train[i,1] = Y_train[i,1]/1000

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

#Mean Squarred Error and Score
print("mse: ", mean_squared_error(Y_pred, Y_test))
print("score: ", linear_reg.score(X_test, Y_test))

#total valid votes polled in state

# y is bjp actual, z is bjp pred, k is cong actual, m is cong pred
Y_test = sc_Y.inverse_transform(Y_test)
Y_pred = sc_Y.inverse_transform(Y_pred)
ytest = list(Y_test[:,1])
ypred = list(Y_pred[:,1])

xloc = list(dataset2.iloc[:,0].values)
xpar = list(dataset2.iloc[:,1].values)
Y_test_pred = zip(ytest,ypred,xloc,xpar)
pred_list = [[0,0], [0,0], [0,0]]
actual_list = [[0,0], [0,0], [0,0]]
cong = 0
bjp = 1
# andaman=0, andhra=1, aruna=2
for ya,yp,xl,xp in Y_test_pred:
    if xl == "Andaman & Nicobar Islands":
        if int(xp) == cong:
            pred_list[0][cong] = pred_list[0][cong] + int(yp)
            actual_list[0][cong] = actual_list[0][cong] + int(ya)
        else:
            pred_list[0][bjp] = pred_list[0][bjp] + int(yp)
            actual_list[0][bjp] = actual_list[0][bjp] + int(ya)
    elif xl == "Andhra Pradesh":
        if int(xp) == cong:
            pred_list[1][cong] = pred_list[1][cong] + int(yp)
            actual_list[1][cong] = actual_list[1][cong] + int(ya)
        else:
            pred_list[1][bjp] = pred_list[1][bjp] + int(yp)
            actual_list[1][bjp] = actual_list[1][bjp] + int(ya)
    else:
        if int(xp) == cong:
            pred_list[2][cong] = pred_list[2][cong] + int(yp)
            actual_list[2][cong] = actual_list[2][cong] + int(ya)
        else:
            pred_list[2][bjp] = pred_list[2][bjp] + int(yp)
            actual_list[2][bjp] = actual_list[2][bjp] + int(ya)
zipped = zip(pred_list,actual_list) 
bjp_pred = []
bjp_act = []
cong_pred = []
cong_act = []       
N = 3
ind = np.arange(N)
width = 0.1
fig = plt.figure()
ax = fig.add_subplot(111)
for i,j in zipped:
    bjp_pred.append(abs(int(i[1])))
    bjp_act.append(abs(int(j[1])))
    cong_pred.append(abs(int(i[0])))
    cong_act.append(abs(int(j[0])))
rects1 = ax.bar(ind, bjp_pred, width, color='r')
rects2 = ax.bar(ind+width, bjp_act, width, color='g')
rects3 = ax.bar(ind+width*2, cong_pred, width, color='b')
rects4 = ax.bar(ind+width*3, cong_act, width, color='y')

ax.set_ylabel('Total votes polled by party')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Andaman', 'Andhra', 'Arunachal') )
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('bjp_P', 'bjp_A', 'cong_P', 'cong_A') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

plt.show()

#plt.scatter(range(35), dataset.iloc[:,5], color = 'red')
#plt.plot(range(3), bjp_pred,bjp_act)
#plt.plot(range(3), cong_pred,cong_act)
plt.plot(range(3), bjp_pred,cong_pred)
#plt.plot(range(3), bjp_act,cong_act)
plt.title('Total votes polled in states')
plt.legend(['BJP', 'Cong'])
plt.xlabel('States (andaman=0, andhra pradesh=1, arunachal pradesh=2)')
plt.ylabel('Total votes polled by party')
plt.show()





