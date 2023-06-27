# Define size of chart
plt.figure(figsize=(15, 7))

# Set the title and axis labels
plt.title('SMA Strategy with USDJPY Drawdown', fontsize=14)
plt.ylabel('Drawdown(%)', fontsize=12)
plt.xlabel('Year', fontsize=12)

# Plot max drawdown
plt.plot(rates_frame['Drawdown'], color='red')

# Fill in-between the drawdown
plt.fill_between(rates_frame['Drawdown'].index, rates_frame['Drawdown'].values, color='red')
plt.show()