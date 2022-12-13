import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

fifa_matches = pd.read_csv('WorldCupMatches.csv')
fifa_player = pd.read_csv('WorldCupPlayers.csv')
fifa_cups = pd.read_csv('WorldCups.csv')

#suma total de goles en cada partido
fifa_matches['Total Goals'] = fifa_matches['Home Team Goals'] + fifa_matches['Away Team Goals']
#print(fifa_matches.head())
fifa_matches.to_csv('WorldCupMatches.csv')

plt.figure(figsize=(12,7))
ax = plt.subplot()
#f.figsize(12,7)
sns.set_style('whitegrid')
sns.set_context("poster", font_scale=0.5)
ax = sns.barplot(
  		data = fifa_matches,
  		x = 'Year',
  		y = 'Total Goals'
		)

ax.set_title('Promedio de goles de FIFA World Cup')

plt.figure(figsize=(12,7))
ax2 = plt.subplot()
sns.set_palette('Spectral')
ax2 = sns.boxplot(
	data = fifa_matches,
	x = 'Total Goals',
	y = 'Year'
	)
#print(fifa_cups.head())

plt.show()