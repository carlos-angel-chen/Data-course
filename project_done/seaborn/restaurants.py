import pandas as pd
from matplotlib import pyplot as plt

restaurants = pd.read_csv('restaurants.csv')
#print(restaurants.head())

cuisine_options_count = restaurants.cuisine.nunique()
#print(cuisine_options_count)

cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()
#print(cuisine_counts)

cuisines = cuisine_counts['cuisine'].values
counts = cuisine_counts.name.values
print(cuisines)
print(counts)

plt.pie(counts, labels=cuisines, autopct='%d%%')
plt.axis('equal')
plt.title('Number of Cuisines')
plt.show()