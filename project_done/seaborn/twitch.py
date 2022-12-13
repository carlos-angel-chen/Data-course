import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]
viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]
labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]
countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]
hour = range(24)
viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

#grafico de barra
plt.figure()
ax = plt.subplot()
plt.bar(range(len(games)), viewers, color='violet')
plt.title('viewers vs games')
plt.xlabel('Games')
plt.ylabel('Viewers')
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation=30)

plt.legend(['Twitch'])

#grafico de torta
plt.figure(figsize=(12,7))
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']
plt.pie(countries, colors=colors, autopct='%d%%', explode=explode, shadow=True, startangle=345, pctdistance=1.15)
#plt.axis('equal')
plt.legend(labels)

#grafico de linea
plt.figure()
plt.plot(hour, viewers_hour)
err = 0.15
y_upper = [i + err*i for i in viewers_hour] 
y_lower = [i - err*i for i in viewers_hour]
plt.fill_between(hour, y_lower, y_upper, alpha=0.2)

plt.show()