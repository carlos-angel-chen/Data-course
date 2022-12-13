import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = 'canada_income.csv'
canada_income = pd.read_csv(data)

years = canada_income.year
income = canada_income['per capita income (US$)']

plt.scatter(years, income, alpha=0.4)
plt.xlabel('year')
plt.ylabel('income per capita')

#creo el objeto model 
model = LinearRegression()
#hago reshape de mi variable X (sino la libreria me patea)
years = np.array(years)
years = years.reshape(-1, 1)
reg = model.fit(years, income)

#ploteo el modelo que predice una vez que se hizo el fit
plt.plot(years, reg.predict(years), color = 'r')
print(reg.predict([[2020]]))


plt.show()