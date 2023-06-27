import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd

# connect to MetaTrader 5
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 500)      # max table width to display
# import pytz module for working with time zone
import pytz
 
# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# set time zone to UTC
timezone = pytz.timezone("Asia/Bangkok")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2023, 6, 24, tzinfo=timezone)
# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
rates = mt5.copy_rates_from("USDJPY", mt5.TIMEFRAME_H4, utc_from,4000)
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
rates_frame.set_index('time', inplace=True)
                           
# display data
print("\nDisplay dataframe with data")
rates_frame

## Setup Indicators
# Set 9 as the lookback period of the short-term moving average
short_ma = 8

# Set 21 as the lookback period of the long-term moving average
long_ma = 20

# Store short-term moving average values in the column 'ma_short'
rates_frame['ma_short'] = rates_frame.close.rolling(short_ma).mean()

# Store long-term moving average values in the column 'ma_long'
rates_frame['ma_long'] = rates_frame.close.rolling(long_ma).mean()

rates_frame.tail()

# Create a column 'signal' to store the trading signal
rates_frame['signal'] = np.where(rates_frame.ma_short > rates_frame.ma_long, 1, 0)


# Calculate strategy returns
strategy_returns = rates_frame.signal.shift(1)*rates_frame.close.pct_change()

# Total strategy returns
print(f'Total strategy returns: {strategy_returns.sum():.2f} %')