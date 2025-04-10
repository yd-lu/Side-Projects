# Project Roadmap

This document outlines the structure and workflow of the project, from data acquisition to performance evaluation and sensitivity analysis.

---

## 0. Libraries

```
math
NumPy
pandas
yfinance
XGBoost
matplotlib
SciPy.
scikit-learn
```

---

## 1. Data Acquisition and Preparation

- **Import Libraries:**  
  Load all necessary Python libraries for data manipulation, modeling, and visualization.

- **Define Asset Universe:**  
  Specify the tickers for U.S. equities, international equities, fixed income, and commodities.

- **Download Data:**  
  Fetch historical market data (prices and volumes) from Yahoo Finance for the selected tickers, and additionally download benchmark data (S&P500).

---

## 2. Feature Engineering and Factor Calculation

- **Compute Returns:**  
  Calculate daily price returns and log returns using adjusted close prices.

- **Compute Factors:**  
  - **Momentum:**  
    Calculate momentum as the percentage change over a specified window.
  - **Volatility:**  
    Compute rolling volatility using the standard deviation of log returns.
  - **Average Volume:**  
    Determine the rolling average volume over the lookback period.

- **Compile Factors:**  
  Organize these computed factors into a consolidated DataFrame for each asset.

---

## 3. Exploratory Data Analysis (EDA)

- **Correlation Matrix:**  
  Visualize the correlation between computed factors and daily returns.

- **Histograms:**  
  Plot histograms to explore the distribution of daily returns for each asset.

- **Scatter Plots:**  
  Examine the relationship between each factor (momentum, volatility, average volume) and the respective asset returns, identifying outliers or patterns.

---

## 4. Constructing Investor Views via Black-Litterman Framework

- **Define Functions for Black-Litterman Adjustments:**  
  - `compute_Omega`: Calculate the view uncertainty (diagonal matrix).
  - `compute_mu_BL`: Compute Black-Litterman adjusted expected returns.

- **Generate Views:**  
  - **Machine Learning (ML)-Based Views (`Q_ml`):**  
    Use historical features with ML models (XGBoost and Random Forest) to predict future asset returns.
  - **Rule-Based Views:**  
    Create signals based on relative average trading volumes.
  - **Combine Views:**  
    Merge ML-based predictions and rule-based signals to form the final view vector (`Q`) using an identity matrix as the pick matrix (`P`).

- **Adjust Views:**  
  Modify the combined view vector (`Q`) based on changes in portfolio performance over time.

---

## 5. Portfolio Optimization

- **Optimization Setup:**  
  Formulate an optimization problem targeting the maximization of the portfolio Sharpe ratio.

- **Constraints:**  
  - **Budget Constraint:**  
    The sum of portfolio weights equals 1.
  - **No Short-Selling:**  
    Each weight is within the interval [0, 1].
  - **Variance Constraint:**  
    The portfolio variance must be below a specified target.

- **Solve the Optimization:**  
  Optimize portfolio weights using the derived adjusted expected returns and computed covariance matrix.

---

## 6. Machine Learning-Based Return Forecasting

- **XGBoost Model:**  
  Train an XGBoost regressor to predict forward returns based on historical features.

- **Random Forest Model:**  
  Similarly, train a Random Forest regressor for return prediction.

- **Ensemble Prediction:**  
  Combine predictions from both models to enhance the forecast's robustness.

---

## 7. Backtesting and Rolling Simulation

- **Define Rebalancing Dates:**  
  Establish a rolling window for rebalancing based on historical data.

- **Rolling Backtest Process:**  
  For each rebalancing period:
  - Compute the covariance matrix and equilibrium returns.
  - Construct investor views and compute adjusted expected returns.
  - Optimize portfolio weights.
  - Account for transaction costs.
  - Evaluate performance in the following period.
  - Store performance metrics and update portfolio weights.

---

## 8. Performance Evaluation and Metrics Calculation

- **Cumulative Returns:**  
  Compute and visualize cumulative returns for both the portfolio and the benchmark.

- **Additional Metrics:**  
  Calculate:
  - Annualized return and volatility.
  - Sharpe Ratio.
  - Maximum drawdown.
  - Value at Risk (VaR) and Conditional Value at Risk (CVaR).

---

## 9. Regression Analysis for Alpha/Beta Estimation

- **Excess Returns Calculation:**  
  Compute daily excess returns for both the portfolio and the benchmark (subtracting the risk-free rate).

- **Linear Regression:**  
  Fit a regression model to derive portfolio beta and daily alpha.

- **Annualize Alpha:**  
  Convert daily alpha estimates into an annualized figure.

---

## 10. Hypothesis Testing for Outperformance

- **Return Differences:**  
  Calculate the daily return differences between the portfolio and the S&P500 benchmark.

- **Statistical Testing:**  
  Employ a one-sample t-test on the daily differences to evaluate if the mean difference is statistically significant.

---

## 11. Sensitivity Analysis with Monte Carlo Simulation

- **Tau Parameter Sampling:**  
  Sample the tau parameter (view uncertainty) from a range using Monte Carlo iterations.

- **Simulate Portfolio Returns:**  
  Run the simulation for each tau value to derive annualized return distributions.

- **Visualization and Summary:**  
  Plot a histogram of simulated annualized returns and calculate summary statistics (mean, standard deviation, minimum, and maximum).

---
