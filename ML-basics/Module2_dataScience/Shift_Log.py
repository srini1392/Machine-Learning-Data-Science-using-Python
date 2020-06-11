### Title           :   Shift_Log.py
### Author          :	Srinikethan M
### Date & Time     :	2019-12-30 15:36:18

# importing the required module 
import pandas as pd

# calculate stock price data
apple_finance = pd.read_csv('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\AppleFinData.csv', index_col='Date')
# print(apple_finance.shift(-1).head())

apple_finance['previous_closing_price'] = apple_finance['Close'].shift(1)
# print(apple_finance.head())


# delta price
apple_finance['closing_price_delta'] = apple_finance['Close'] -apple_finance['previous_closing_price']
# print(apple_finance.head())


#weekly returns
apple_finance['Weekly_returns'] = ((apple_finance['Close']-apple_finance['Close'].shift(7)) / apple_finance['Close']) * 100
# print(apple_finance)

#write your data to csv file
apple_finance.to_csv('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\AppleFinData1.csv',columns=['Volume','Weekly_returns','Close'])