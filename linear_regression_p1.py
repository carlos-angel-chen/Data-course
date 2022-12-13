import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("honeyproduction.csv")

prod_per_year = df.groupby('year').totalprod.mean()

x = df.year 
x = x.values.reshape(-1, 1)

y = df["totalprod"]

regr = linear_model.LinearRegression()
regr.fit(x,y)

y_predict = regr.predict(x)

print(regr.coef_)
print(regr.intercept_)

x_future = np.array(range(2013, 2051))
x_future = x_future.reshape(-1,1)
future_predict = regr.predict(x_future)

print(x_future)

plt.plot(x_future, future_predict)
plt.plot(x, y_predict)
plt.scatter(x,y)
plt.show()

