import matplotlib.pyplot as plt
import pandas as pd
# Set the plot style to 'seaborn-darkgrid'
plt.style.use('seaborn-darkgrid')

# Create subplots with 3 rows and 1 column
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10, 8))

# Plot the 'close' column in the first chart
ax1.plot(rates_frame.index, rates_frame['close'])
ax1.set_ylabel('Close')

# Calculate the percentage change of the 'close' column
pct_change = rates_frame['close'].pct_change()

# Plot the percentage change in the second chart
ax2.plot(rates_frame.index, pct_change)
ax2.set_ylabel('Percentage Change')

# Plot the 'spread' column in the third chart
ax3.plot(rates_frame.index, rates_frame['tick_volume'])
ax3.set_ylabel('Tick volume')
ax3.set_xlabel('Time')

# Adjust spacing between subplots
plt.subplots_adjust(hspace=0.3)

# Show the plot
plt.show()
