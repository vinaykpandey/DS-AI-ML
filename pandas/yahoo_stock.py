import pandas_datareader as web
#Importing the Pyplot module from the Matplotlib Library which we will using to plot our graphs
from matplotlib import pyplot as plt

# 'plt' is a naming convention but you can name pyplot as per your wish too.

#Getting the stock data
stock_data = web.DataReader('MSFT', data_source='yahoo', start='2015-06-20', end='2020-06-20')

#display data
print(stock_data)

stock_data['Open']


#Visualize Closing Price History of Microsoft

#AutoStyle our Graph
#plt.style.use('fivethirtyeight')

# Increasing the size of our Canvas
plt.figure(figsize=(16,8))

#Giving Title to our Graph
plt.title("Closing Stock Price of Microsoft for Past 5 Years")

#Plotting the data
plt.plot(stock_data['Close'], color='red', linewidth=0.8, label="Close")

#Labelling our axis
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')

#Displaying Legend
plt.legend()

#Displaying the Plot
plt.show()

#Visualize Opening Price History of Microsoft

#Increased the size of our canvas
plt.figure(figsize=(16,8))

#If you pass only one list to your plot function then it will become the values for the y axis and the default indexes will be taken
#as your x-axis values.

#Plotting our graph for opening price
plt.plot(stock_data['Open'],color='#FBFB05',linewidth=2, label="Open")

#Label and Title your Graph
plt.xlabel('TimeSpan')
plt.ylabel('Opening Price')

plt.title("Opening Stock Price of Microsoft for Past 5 years")

#Provide a legend to our graph
plt.legend(loc="upper left")

#Display our graph
plt.show()