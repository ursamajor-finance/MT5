# Set a risk-free rate
risk_free_rate = 0.02/252

# Calculate Sharpe ratio
performance_metrics['Sharpe Ratio'] = np.sqrt(252)*(np.mean(rates_frame.Strategy_Returns) -
                                                    (risk_free_rate))/np.std(rates_frame.Strategy_Returns)

performance_metrics.T