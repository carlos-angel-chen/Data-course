import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

healthcare = pd.read_csv('healthcare.csv')
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']

alabama_chest_pain = chest_pain[chest_pain['Provider State'] == 'AL']
cost_alabama_chest_pain = alabama_chest_pain[' Average Covered Charges '].values

states = chest_pain['Provider State'].unique()
data_sets = []
for i in states:
    data_sets.append( chest_pain[chest_pain['Provider State'] == i][' Average Covered Charges '].values )

plt.figure(figsize=(20,6))
plt.boxplot(data_sets, labels=states)


plt.legend()
plt.show()