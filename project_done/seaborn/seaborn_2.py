import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np
import seaborn as sns

gradebook = pd.read_csv('gradebook.csv')

assignment1 = gradebook[gradebook.assignment_name == 'Assignment 1']
assignment2 = gradebook[gradebook.assignment_name == 'Assignment 2']

asn1_median = np.median(assignment1.grade)
asn2_median = np.median(assignment2.grade)

sns.barplot(
	data = gradebook,
	x = 'assignment_name',
	y = 'grade'
	)

plt.show()