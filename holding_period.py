import matplotlib.pyplot as plt
import pandas as pd
# Set the plot style to 'seaborn-darkgrid'
plt.style.use('seaborn-darkgrid')


## Visualise trading period
lookback_days = 200
# Plot the close prices of the last 100 days
close_plot = rates_frame.close[-lookback_days:].plot(figsize=(15, 7), color='blue')

# Plot the signal of the last 100 days
signal_plot = rates_frame.signal[-lookback_days:].plot(figsize=(15, 7),
                                       secondary_y=True, ax=close_plot, style='green')

# Highlight the holding periods of the long positions
plt.fill_between(rates_frame.close[-lookback_days:].index, 0, 1,
                 where=(rates_frame.signal[-lookback_days:] > 0), color='green', alpha=0.1, lw=0)

# Title of the plot
signal_plot.set_title('Holding Periods of The Trading Positions')

# Plot ylabels
close_plot.set_ylabel('Price ($)')
signal_plot.set_ylabel('Signal')

# Legend of the plot
plt.legend()

# Show the plot
plt.show()