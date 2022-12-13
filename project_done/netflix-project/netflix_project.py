from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

netflix_stocks = pd.read_csv('NFLX.csv')
dowjones_stocks = pd.read_csv('DJI.csv')
netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')

#split year-month-day
netflix_stocks['year'] = netflix_stocks.Date.apply(lambda x : x.split('-')[0])
netflix_stocks['month'] = netflix_stocks.Date.apply(lambda x : x.split('-')[1])
netflix_stocks['day'] = netflix_stocks.Date.apply(lambda x : x.split('-')[2])

dowjones_stocks['year'] = netflix_stocks.Date.apply(lambda x : x.split('-')[0])
dowjones_stocks['month'] = netflix_stocks.Date.apply(lambda x : x.split('-')[1])
dowjones_stocks['day'] = netflix_stocks.Date.apply(lambda x : x.split('-')[2])

netflix_stocks_quarterly['year'] = netflix_stocks.Date.apply(lambda x : x.split('-')[0])
netflix_stocks_quarterly['month'] = netflix_stocks.Date.apply(lambda x : x.split('-')[1])
netflix_stocks_quarterly['day'] = netflix_stocks.Date.apply(lambda x : x.split('-')[2])

#change name, 'Adj Close'--->'Price'
netflix_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)
dowjones_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)
netflix_stocks_quarterly.rename(columns={'Adj Close': 'Price'}, inplace=True)


#violin plot
ax = sns.violinplot(
    x = netflix_stocks_quarterly['Quarter'], 
    y = netflix_stocks_quarterly['Price'],
    data = netflix_stocks_quarterly
)
ax.set_title('Distributionof 2017 Netflix Stock Price by Quarter')
ax.set_ylabel('Closing Stock Price')
ax.set_xlabel('Business Quarters in 2017')


#EPS earning per share with a violinplot 
plt.figure()
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]

plt.scatter(x_positions, earnings_actual, color='red', alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color='blue', alpha=0.5)
plt.legend(['Actual', 'Estimate'])
plt.xticks(x_positions, chart_labels)
plt.title('Earnings Per Share in Cents')


#barchart side by side revenue by quarter and xvalues
plt.figure()
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]
#first set of x values
n = 1
t = 2
d = len(revenue_by_quarter)
w = 0.8
bars1_x = [t*element + w*n for element in range(d)]
plt.bar(bars1_x, revenue_by_quarter, label='Revenue')
#second set of x values
n = 2
t = 2
d = len(earnings_by_quarter)
w = 0.8
bars2_x = [t*element + w*n for element in range(d)]
plt.bar(bars2_x, earnings_by_quarter, label='Earnings')
plt.legend()
plt.title('Revenue and Earning per Quarter')

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]
plt.xticks(middle_x, quarter_labels)


#Comparison between Netflix stock to Dow Jones Insdustrial Average
plt.figure()
ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])
ax1.set_title('Netflix')
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price')

ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])
ax2.set_title('Dow Jones')
ax2.set_xlabel('Date')
ax2.set_ylabel('Stock Price')

plt.subplots_adjust(wspace=.5)

plt.show()

#print(netflix_stocks)
#print(dowjones_stocks)
#print(netflix_stocks_quarterly)