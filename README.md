# Mid-Frequency ML-Based Bitcoin Trading Strategy

This project implements a mid-frequency Bitcoin trading strategy that combines **principal component analysis (PCA)** with an **ensemble of regressors** (Ridge, Random Forest, LightGBM) to forecast short-term returns. It integrates **realistic execution constraints**, including transaction costs, bid-ask spread impact, and stochastic order success rates.

---

## Key Highlights

- **ML Voting Strategy**: Executes trades only when 2 or more models agree on market direction, with increased size when all models agree.
- **Execution Modeling**: Incorporates slippage, spread-based entry/exit prices, and probabilistic execution (`transaction_success_rate`).
- **Dimensionality Reduction**: Uses PCA on engineered features to reduce noise and improve signal stability.
- **Order Flow Awareness**: Filters trades using order flow imbalance for directional confirmation.
- **Backtest Metrics**: Includes Sharpe/Sortino ratios, profit factor, drawdown analysis, and comparison with BTC buy-and-hold.

---

## Performance Summary (Backtest over ~4 years)

| Metric                      | Strategy               | BTC Buy & Hold         |
|----------------------------|------------------------|------------------------|
| Total PnL                  | $167,275               | $67,166                |
| Max Drawdown               | $50,440                | $52,949                |
| Drawdown Duration (hrs)    | 246                    | 20,377                 |
| Sharpe Ratio (annualized)  | 0.92                   | 0.47                   |
| Sortino Ratio (annualized) | 0.19                   | 0.60                   |
| Profit Factor              | 1.44                   | N/A                    |

