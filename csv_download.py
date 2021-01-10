import math
import pandas_datareader as web
import pandas as pd
import numpy as np

# Use alphavantage.co data sets

df = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=NQOQHNF67BV7HLX4&datatype=csv&outputsize=full')


print(df.head(10))

print(df.tail(10))

# Save csv
df.to_csv('stock.csv')
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo&datatype=csv