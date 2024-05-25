
import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate European call option price using Black-Scholes model
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * stats.norm.cdf(d1) - K * np.exp(-r * T) * stats.norm.cdf(d2)
    return call_price

# Function to calculate European call option price using Fractional Black-Scholes model
def fractional_black_scholes_call(S, K, T, r, sigma, H):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2 * T ** (2 * H - 1))) / (sigma * T ** H)
    d2 = d1 - sigma * T ** H
    call_price = S * stats.norm.cdf(d1) - K * np.exp(-r * T) * stats.norm.cdf(d2)
    return call_price

# Parameters
S = 100  # Underlying asset price
K = 100  # Strike price
T = 1    # Time to maturity in years
r = 0.05 # Risk-free rate
H = 0.5  # Hurst parameter for fGBM, setting to 0.5 to compare with GBM

# Volatility range
volatilities = np.linspace(0.1, 0.5, 10)

# Initialize results DataFrame
results_comparison = pd.DataFrame(columns=['Volatility', 'GBM Call Price', 'fGBM Call Price'])

# Calculate option prices for different volatilities
for sigma in volatilities:
    gbm_price = black_scholes_call(S, K, T, r, sigma)
    fgbm_price = fractional_black_scholes_call(S, K, T, r, sigma, H)
    results_comparison = results_comparison.append({'Volatility': sigma, 'GBM Call Price': gbm_price, 'fGBM Call Price': fgbm_price}, ignore_index=True)

# Save the results to a CSV file
results_comparison.to_csv('option_pricing_comparison_H_0_5.csv', index=False)

# Plotting the comparison
plt.figure(figsize=(10, 6))
plt.plot(results_comparison['Volatility'], results_comparison['GBM Call Price'], label='GBM Call Price', marker='o', linestyle='-')
plt.plot(results_comparison['Volatility'], results_comparison['fGBM Call Price'], label='fGBM Call Price (H=0.5)', marker='x', linestyle='--')
plt.xlabel('Volatility')
plt.ylabel('Call Option Price')
plt.title('Comparison of GBM and fGBM Call Option Prices (H=0.5)')
plt.legend()
plt.grid(True)
plt.savefig('option_prices_comparison_H_0_5.png')
plt.show()
