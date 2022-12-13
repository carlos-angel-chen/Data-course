import seaborn as sns
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 

df = pd.read_csv('survey.csv')

plt.figure()
sns.barplot(
	data = df,
	x = 'Gender',
	y = 'Response',
	estimator = len
	)

plt.figure()
sns.barplot(
	data = df,
	x = 'Gender',
	y = 'Response',
	estimator = np.median
	)

plt.figure()
sns.barplot(
	data = df,
	x = 'Age Range',
	y = 'Response',
	hue = 'Gender'
	)

plt.figure()
sns.barplot(
	data = df,
	x = 'Gender',
	y = 'Response',
	hue = 'Age Range'
	)

plt.show()