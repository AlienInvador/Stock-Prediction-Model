# Libraries
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb
import yfinance as yf 

# Variables to fetch the stock prices
ticker = 'NVDA'
start_date = '2010-01-01'
end_date = '2024-06-01'

# Get stock prices for the specificed period 
data = yf.download(ticket, start_date, end_date)

# Print stock price data
print(data)