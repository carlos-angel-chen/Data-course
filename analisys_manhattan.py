import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('rental.csv')

manhattan = df[df.borough == 'Manhattan']

x = manhattan[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

y = manhattan[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=6)

mlr = LinearRegression()

model = mlr.fit(x_train, y_train)

y_predict = mlr.predict(x_test)

plt.figure()
plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel('Prices: Yi')
plt.ylabel('Predicted prices: Yi')

plt.figure()
plt.scatter(x.min_to_subway, x.building_age_yrs, alpha=0.4)
plt.xlabel('min to subway')
plt.ylabel('building year')

plt.figure()
plt.scatter(y, x.bedrooms, alpha=0.4)
plt.ylabel('bedrooms')
plt.xlabel('rent')

plt.figure()
plt.scatter(x.min_to_subway, y, alpha=0.4)
plt.xlabel('min to subway')
plt.ylabel('rent')

plt.show()