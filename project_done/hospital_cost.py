import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG__-_FY2011.csv')

#cost_mean = np.mean(data[' Average Covered Charges '])
cost_mean = data[' Average Covered Charges '].mean()
cost_median = np.median(data[' Average Covered Charges '])

cost_min = np.amin(data[' Average Covered Charges '])
cost_max = data[' Average Covered Charges '].max()
cost_range = cost_max - cost_min

plt.hist(data[' Average Covered Charges '], range = (cost_min, cost_max), bins = 10000)
plt.show()