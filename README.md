
# Option Pricing Comparison

This project compares option pricing using Geometric Brownian Motion (GBM) and Fractional Geometric Brownian Motion (fGBM) under different Hurst parameters.

## Files

1. `compare_fgbm_gbm_H_0_95.py`: Compares option pricing between GBM and fGBM for Hurst parameter \( H = 0.95 \).
2. `compare_fgbm_gbm_H_0_5.py`: Demonstrates that fGBM with \( H = 0.5 \) is equivalent to GBM.

## Instructions

1. **Run the comparison for \( H = 0.95 \)**:
   ```bash
   python compare_fgbm_gbm_H_0_95.py
   ```
   This will generate a CSV file (`option_pricing_comparison_H_0_95.csv`) and a plot (`option_prices_comparison_H_0_95.png`).

2. **Run the comparison for \( H = 0.5 \)**:
   ```bash
   python compare_fgbm_gbm_H_0_5.py
   ```
   This will generate a CSV file (`option_pricing_comparison_H_0_5.csv`) and a plot (`option_prices_comparison_H_0_5.png`).

## Results

The results demonstrate the following:
- For \( H = 0.95 \), fGBM captures long-term dependencies and yields different option prices compared to GBM.
- For \( H = 0.5 \), fGBM reduces to GBM, resulting in identical option prices.

## Plots

- `option_prices_comparison_H_0_95.png`: Comparison of GBM and fGBM Call Option Prices (H=0.95)
- `option_prices_comparison_H_0_5.png`: Comparison of GBM and fGBM Call Option Prices (H=0.5)

## Requirements

- Python 3.x
- numpy
- scipy
- pandas
- matplotlib
