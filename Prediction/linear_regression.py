"""
@author: Vivsvaan Sharma
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error 

dataset = pd.read_csv('2014_trainingSet.csv')
X = dataset.iloc[:, 0:4].values
Y = dataset.iloc[:, 4:6].values
dataset2 = pd.read_csv('2019_testSet.csv')
X2 = dataset2.iloc[:,0:4].values
#Y2 = dataset2.iloc[:,4:6].values
locations = dataset.iloc[:,0].values
locations = set(locations)
locations = list(locations)
locations.sort()

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


X_train = X
Y_train = Y
X_test = X2
#Y_test = Y2
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
#Y_test = sc_Y.transform(Y_test)

#linear regression
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(X_train, Y_train)
Y_pred = linear_reg.predict(X_test)

#Mean Squarred Error and Score
#print("mse: ", mean_squared_error(Y_pred, Y_test))
#print("score: ", linear_reg.score(X_test, Y_test))

#total valid votes polled in state

# y is bjp actual, z is bjp pred, k is cong actual, m is cong pred
#Y_test = sc_Y.inverse_transform(Y_test)
Y_pred = sc_Y.inverse_transform(Y_pred)
#ytest = list(Y_test[:,1])
ypred = list(Y_pred[:,1])
for i in range(len(ypred)):
    ypred[i] = str(abs(int(ypred[i])))
xloc = list(dataset2.iloc[:,0].values)
xpar = list(dataset2.iloc[:,1].values)
#Y_test_pred = zip(ytest,ypred,xloc,xpar)
Y_test_pred = zip(ypred,xloc,xpar)
pred_list = []
for _ in locations:
    pred_list.append([0,0])
#actual_list = [[0,0], [0,0], [0,0]]
cong = 0
bjp = 1
# andaman=0, andhra=1, aruna=2
# assam=0, bihar=1, chandigarh=2
for yp,xl,xp in Y_test_pred:
    if xl in locations:
        index = locations.index(xl)
        if int(xp) == cong:
            pred_list[index][cong] = pred_list[index][cong] + int(yp)
            #actual_list[0][cong] = actual_list[0][cong] + int(ya)
        else:
            pred_list[index][bjp] = pred_list[index][bjp] + int(yp)
            #actual_list[0][bjp] = actual_list[0][bjp] + int(ya)
    '''elif xl == "Kerala":
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
            actual_list[2][bjp] = actual_list[2][bjp] + int(ya)'''
#zipped = zip(pred_list,actual_list) 
bjp_pred = []
bjp_act = []
cong_pred = []
cong_act = []       

'''N = 3
ind = np.arange(N)
width = 0.1

fig = plt.figure()
ax = fig.add_subplot(111)

#for i,j in zipped:'''
for i in pred_list:
    bjp_pred.append(abs(int(i[1])))
    #bjp_act.append(abs(int(j[1])))
    cong_pred.append(abs(int(i[0])))
    #cong_act.append(abs(int(j[0])))
    '''
rects1 = ax.bar(ind, bjp_pred, width,color='r')
rects2 = ax.bar(ind+width, bjp_act, width, color='g')
rects3 = ax.bar(ind+width*2, cong_pred, width, color='b')
rects4 = ax.bar(ind+width*3, cong_act, width, color='y')

ax.set_ylabel('Total votes polled by party')

ax.set_xticks(ind+width)
ax.set_xticklabels( ('Goa', 'Kerala', 'Odisha') )
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
plt.get_backend()
plt.show()'''

#plt.scatter(range(35), dataset.iloc[:,5], color = 'red')
#plt.plot(range(3), bjp_pred,bjp_act)
#plt.plot(range(3), cong_pred,cong_act)
plt.plot(range(35), bjp_pred,cong_pred)
#plt.plot(range(3), bjp_act,cong_act)
plt.title('Total votes polled in states by BJP & Cong in 2019')
plt.legend(['BJP', 'Cong'])
#plt.xlabel('States (goa=0, kerala=1, odisha=2)')
plt.xlabel('States')
plt.ylabel('Total votes polled by party')
plt.show()

#printing location table
print('|' + '--------|' + '------------------------------|')
print('|{:^8}|'.format("index") + '{:^30}|'.format("Locations"))
print('|' + '--------|' + '------------------------------|')
for i in range(len(locations)):
    print('|{:^8}|'.format(str(i)), end="")
    print('{:^30}|'.format(locations[i]))
print('|' + '--------|' + '------------------------------|')

#total votes....
total_bjp = 0
total_cong = 0
for i in range(len(bjp_pred)):
    total_bjp = total_bjp + int(bjp_pred[i])
    total_cong = total_cong + int(cong_pred[i])
print('|' + '--------|' + '------------------------------|')
print('|{:^8}|'.format("party") + '{:^30}|'.format("Total Votes"))
print('|' + '--------|' + '------------------------------|')
print('|{:^8}|'.format("BJP"), end="")
print('{:^30}|'.format(str(total_bjp)))
print('|' + '--------|' + '------------------------------|')
print('|{:^8}|'.format("Cong"), end="")
print('{:^30}|'.format(str(total_cong)))
print('|' + '--------|' + '------------------------------|')
