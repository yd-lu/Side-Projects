# Modern Portfolio Model Explanation and Optimization Objective

Modern portfolio theory (MPT) provides a framework for assembling a portfolio of assets in such a way as to maximize the expected return for a given level of risk. Developed by Harry Markowitz, it emphasizes the benefits of diversification by considering both the returns and the risks (covariances) of the assets.

## Key Components
- **$\mu$ (Expected Returns):** An $n\times 1$ vector representing the estimated returns of $n$ assets.
- **$\Sigma$ (Covariance Matrix):** An $n\times n$ matrix that captures the variances of each asset's returns along with the covariances between them.
- **$w$ (Portfolio Weights):** An $n\times 1$ vector indicating the proportion of the portfolio invested in each asset.
- **$q$ (Risk Aversion Parameter):** A scalar that reflects the investor's tolerance for risk. A higher value of $q$ implies that the investor is more risk-averse.

## Optimization Objective
In the modern portfolio framework, the optimal portfolio is typically determined by maximizing a risk-adjusted utility function. One common approach is to maximize the difference between the portfolio's expected return and a penalty for risk:

$$
\text{maximize } \mu^T w - \frac{q}{2} w^T \Sigma w
$$

### Elaboration of the Objective Equation

- **Expected Return Component:**  
  The term $\mu^T w$ represents the weighted sum of expected returns for the portfolio.
  
- **Risk (Variance) Penalty:**  
  The term $\frac{q}{2}w^T \Sigma w$ quantifies the overall portfolio risk, with $w^T\Sigma w$ being the portfolio variance. The risk aversion parameter, *q*, scales this penalty—investors with higher risk aversion place more weight on minimizing variance.

This formulation encapsulates the trade-off between return and risk, where the goal is to choose portfolio weights *w* that balance maximizing expected returns while minimizing risk. Constraints such as the sum of weights equaling 1 and non-negativity of weights (if short selling is not allowed) are often added depending on the investment strategy.

This modern portfolio model provides a systematic method for portfolio selection based on quantitative optimization of risk versus return.








# Black–Litterman Model Explanation and Optimization Objective

This document outlines the key components of the Black–Litterman model for portfolio construction. For *n* stocks and *n* investor views, the model involves the following elements:

## Equilibrium Components
- **π (Equilibrium Returns):** An *n×1* vector of market-implied expected returns.
- **δ (Risk Aversion Coefficient):** A scalar quantifying overall market risk aversion.
- **Σ (Covariance Matrix):** An *n×n* matrix capturing the variances and covariances among stocks.
- **wₘ (Market Weights):** An *n×1* vector of market portfolio weights.
- **τ (Scaling Factor for Uncertainty):** A scalar that scales Σ to reflect uncertainty in π.

## Investor Views Components
- **P:** A *k×n* matrix that indicates which stocks each investor view pertains to.
- **Q:** A *k×1* vector where each element represents the return level (or difference) of the view.
- **Ω (Omega):** A *k×k* matrix specifying the uncertainty in the investor views (typically diagonal).

## Output Variables
- **μ (Posterior/Adjusted Expected Returns):** An *n×1* vector obtained by blending the equilibrium returns π with the investor views.
- **w (Portfolio Weights):** The optimal *n×1* vector of portfolio weights determined via optimization.
- **q (Risk Aversion Parameter in Optimization):** A scalar (akin to δ) used in the portfolio optimization process.

The Black–Litterman model first blends the market equilibrium with the investor views using:

$$
\mu = \left[ (\tau \Sigma)^{-1} + P^T \Omega^{-1} P \right]^{-1} \left[ (\tau \Sigma)^{-1} \pi + P^T \Omega^{-1} Q \right]
$$

Once μ has been determined, the typical portfolio optimization formulation aims to maximize the risk-adjusted return:

$$
\text{maximize } \mu^T w - \frac{q}{2} w^T \Sigma w
$$

subject to any portfolio constraints (e.g., weights summing to 1, non-negativity).

This objective function balances the expected return (\(\mu^T w\)) against the risk (represented by the quadratic penalty on portfolio variance, \(\frac{q}{2} w^T \Sigma w\)).
