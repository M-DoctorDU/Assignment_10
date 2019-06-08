"""
**************************************************************
Author: Malachi Doctor

Description: Programming Assignment 10: Adding functionality of
				your own choice
			 Python Progamming ICT-4370
          
Last Revision: 6/07/2019
**************************************************************
"""
import matplotlib.pyplot as plt

class Stock():
	"""Represents my simple stock profile"""
	def __init__(self, symbol, open, high, low, volume, labels,
		values, colors, explode):
		self.symbol = symbol
		self.open = open
		self.high = high
		self.low = low
		self.volume = volume
		self.labels = labels
		self.values = values
		self.colors = colors
		self.explode = explode
		self.stockCloseList = []
		self.stockDateClosed = []
		
	def addClose(self, close, date):
		"""Adding information to my stock class"""
		self.stockCloseList.append(close)
		self.stockDateClosed.append(date)
        
	def describe_stock(self):
		print (self.symbol + ", " + str(self.open) + ", " + str(self.volume))
		
		"""Pie Chart graphing values of different stocks"""
labels = 'AIG', 'F', 'FB', 'GOOG', 'IBM', 'M', 'MSFT', 'RDS-A'
values = [65.27, 10.95, 172.45, 941.53, 145.30, 23.98, 73.04, 55.74]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'magenta',
	'red', 'cyan', 'blue']
explode = (0, 0, 0, 0.1, 0, 0, 0, 0)
plt.pie(values, explode=explode, labels=labels, colors=colors, 
	autopct='%1.1f%%', shadow=True, startangle=140)

plt.legend()
plt.title("Value Distribution", fontsize = 18)
plt.xlabel("For Stocks", fontsize = 18)
plt.axis('equal')
plt.show()



