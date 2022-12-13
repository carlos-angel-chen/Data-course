import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv('tennis_stats.csv')
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')


# perform exploratory analysis here:

aces = df['Aces']
wins = df['Wins']
losses = df['Losses']
tpointwon = df['TotalPointsWon']
tservicewon = df['TotalServicePointsWon']

#plt.subplot(221)
plt.scatter(aces, wins, alpha=0.4)
plt.xlabel('aces')
plt.ylabel('wins')

#plt.subplot(222)
#plt.scatter(aces, losses, alpha=0.4)
#plt.xlabel('aces')
#plt.ylabel('losses') 


#plt.subplot(223)
#plt.scatter(tpointwon, wins, alpha=0.4, color='g')
#plt.xlabel('win')
#plt.ylabel('total point won')


#plt.subplot(224)
#plt.scatter(tservicewon, wins, alpha=0.4, color='r')
#plt.xlabel('win')
#plt.ylabel('total service point won')


#ax.scatter(wins, losses, aces, c='r', marker='o', s=20, alpha=0.4)
#ax.set_xlabel('wins')
#ax.set_ylabel('losses')
#ax.set_zlabel('aces')





## perform single feature linear regressions here:

model = LinearRegression()
aces = np.array(aces)
aces = aces.reshape(-1,1)
reg = model.fit(aces, wins)
plt.plot(aces, reg.predict(aces), color='r')





plt.figure()
tservicewon = np.array(tservicewon)
tservicewon = tservicewon.reshape(-1,1)
service_train, service_test, point_train, point_test = train_test_split(tservicewon, tpointwon, train_size =0.8)
reg2 = model.fit(service_train, point_train)

print(reg2.predict(service_test))
print(point_test)
print(reg2.score(service_test, point_test))

plt.tight_layout()
plt.show()







## perform two feature linear regressions here:






















## perform multiple feature linear regressions here:
