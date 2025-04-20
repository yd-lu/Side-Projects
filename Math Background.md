# Modern Portfolio Model Explanation and Optimization Objective

Modern portfolio theory provides a framework for assembling a portfolio of assets in such a way as to maximize the expected return for a given level of risk. Developed by Harry Markowitz, it emphasizes the benefits of diversification by considering both the returns and the risks (covariances) of the assets.

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
  The term $\frac{q}{2}w^T \Sigma w$ quantifies the overall portfolio risk, with $w^T\Sigma w$ being the portfolio variance. The risk aversion parameter, $q$, scales this penalty—investors with higher risk aversion place more weight on minimizing variance.

This formulation encapsulates the trade-off between return and risk, where the goal is to choose portfolio weights $w$ that balance maximizing expected returns while minimizing risk. Constraints such as the sum of weights equaling 1 and non-negativity of weights (if short selling is not allowed) are often added depending on the investment strategy.

This modern portfolio model provides a systematic method for portfolio selection based on quantitative optimization of risk versus return.








# Black–Litterman Model Explanation and Optimization Objective

The Black–Litterman model provides a way to estimate $\mu$, by incorporating investor views. For $n$ stocks and $k$ investor views, the model involves the following elements:

## Equilibrium Components
- **$\pi$ (Equilibrium Returns):** An $n\times 1$ vector of market-implied expected returns.
- **$\delta$ (Risk Aversion Coefficient):** A scalar quantifying overall market risk aversion.
- **$\Sigma$ (Covariance Matrix):** An $n\times n$ matrix capturing the variances and covariances among stocks.
- **$\tau$ (Scaling Factor for Uncertainty):** A scalar that scales $\Sigma$ to reflect uncertainty in $\pi$.

## Investor Views Components
- **$P$:** A $k\times n$ matrix that indicates which stocks each investor view pertains to.
- **$Q$:** A $k\times 1$ vector where each element represents the return level (or difference) of the view.
- **$\Omega$ (Omega):** A $k\times k$ matrix specifying the uncertainty in the investor views (typically diagonal).

## Output Variables
- **$\mu$ (Posterior/Adjusted Expected Returns):** An $n\times 1$ vector obtained by blending the equilibrium returns $\pi$ with the investor views.
- **$w$ (Portfolio Weights):** The optimal $n\times 1$ vector of portfolio weights determined via optimization.

The Black–Litterman model blends the market equilibrium with the investor views using:

$$
\mu = \left[ (\tau \Sigma)^{-1} + P^T \Omega^{-1} P \right]^{-1} \left[ (\tau \Sigma)^{-1} \pi + P^T \Omega^{-1} Q \right]
$$

