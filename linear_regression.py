from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

line_fitter = LinearRegression()
#metodo .fit() nos da el coef de la pendiente y de la ordenada
line_fitter.fit(temperature, sales)

#metodo .predict() le doy el X y me devuelve los Y que predice
sales_predict = line_fitter.predict(temperature)

plt.plot(temperature, sales_predict)
plt.plot(temperature, sales, 'o')
plt.show()