import seaborn as sns
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 

dataset = pd.read_csv('dataset.csv')

set_one = dataset[dataset.label=='set_one']
set_two = dataset[dataset.label=='set_two']
set_three = dataset[dataset.label=='set_three']
set_four = dataset[dataset.label=='set_four']

print(set_one)
#sns.kdeplot(set_one, shade=True)
#sns.kdeplot(set_two, shade=True)
#sns.kdeplot(set_three, shade=True)
#sns.kdeplot(set_four, shade=True)

plt.show()