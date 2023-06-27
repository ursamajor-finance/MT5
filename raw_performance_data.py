# Create a dataframe to store performance metrics
performance_metrics = pd.DataFrame(index=['Strategy'])

# Calculate strategy returns
rates_frame['Strategy_Returns'] = rates_frame.signal.shift(1) * rates_frame.close.pct_change()

# Calculate cumulative strategy returns
rates_frame['Cumulative_Returns'] = (rates_frame['Strategy_Returns'] + 1.0).cumprod()

# Plot the cumulative strategy returns
(rates_frame['Cumulative_Returns'].plot(figsize=(15, 7), color='blue'))
plt.title('Equity Curve', fontsize=14)
plt.ylabel('Cumulative Returns')
plt.show()