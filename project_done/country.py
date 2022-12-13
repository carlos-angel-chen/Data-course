import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('country_data.csv')

life_expectancy = data['Life Expectancy']
life_expectancy_quartile = np.quantile(life_expectancy, [0.25, 0.5, 0.75])

gdp = data['GDP']
median_gdp = np.median(gdp)
low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] > median_gdp]

low_gdp_quartile = np.quantile(low_gdp['Life Expectancy'], [0.25, 0.5, 0.75])
high_gdp_quartile = np.quantile(high_gdp['Life Expectancy'], [0.25, 0.5, 0.75])


plt.figure(1)
ax1 = plt.subplot(211)
plt.hist(life_expectancy, edgecolor = '#000000')
plt.axvline(life_expectancy_quartile[0], color='red', label = 'Q1')
plt.axvline(life_expectancy_quartile[1], color='orange', label = 'Q2')
plt.axvline(life_expectancy_quartile[2], color='green', label = 'Q3')
ax1.set_title('Expectancy LIFE')
ax1.set_xlabel('Years')
ax1.set_ylabel('Quantity')


ax2 = plt.subplot(212)
plt.hist(high_gdp['Life Expectancy'], alpha=0.5, label='High GDP', edgecolor = '#000000')
plt.hist(low_gdp['Life Expectancy'], alpha=0.5, label='Low GDP', edgecolor = '#000000')


plt.tight_layout()
plt.legend()
plt.show()