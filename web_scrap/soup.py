from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html').content

soup = BeautifulSoup(webpage, "html.parser")
#print(soup)

rate = soup.find_all(attrs={"class": "Rating"})
rating = []
for i in rate[1:]:
  data = float(i.get_text())
  rating.append(data)

company = soup.select(".Company")
company_name =[]
for k in company[1:]:
  data = k.get_text()
  company_name.append(data)

cocoa_percent = []
cocoa = soup.select(".CocoaPercent")
for j in cocoa[1:]:
    data = float(j.get_text().strip("%"))
    cocoa_percent.append(data)

print(len(rating), len(company_name), len(cocoa_percent))
d = {"Company": company_name, "Rating": rating, "CocoaPercentage":cocoa_percent}
df = pd.DataFrame.from_dict(d)

mean_values = df.groupby("Company").Rating.mean()
ten_best = mean_values.nlargest(10)
#print(ten_best)

plt.scatter(df.Rating, df.CocoaPercentage)
plt.xlabel('Rating')
plt.ylabel('Cocoa %')

z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")

#plt.hist(rating)
plt.show()