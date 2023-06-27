# Compute the cumulative maximum
rates_frame['Peak'] = rates_frame['Cumulative_Returns'].cummax()

# Compute the Drawdown
rates_frame['Drawdown'] = ((rates_frame['Cumulative_Returns']-rates_frame['Peak'])/rates_frame['Peak'])

# Compute the maximum drawdown
performance_metrics['Maximum Drawdown'] =  "{0:.2f}%".format((rates_frame['Drawdown'].min())*100)
 
performance_metrics.T