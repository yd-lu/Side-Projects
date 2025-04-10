# Limitations and Future Improvements

I want to discusses some of the current limitations of the project as well as possible enhancements I expect for the future.

---

## 1. Flexibility in the Pick Matrix (P)

- **Current Limitation:**  
  - Currently, the project uses an identity matrix as the pick matrix (P) in the Black-Litterman model. This approach assigns an absolute view for each asset.
  
- **Future Improvement:**  
  - Allow for more general forms of the pick matrix. For exmaple enable investor to specify views that compare assets (e.g., "Asset A will outperform Asset B by X%") or even group assets into clusters.
    
---

## 2. Handling Outliers and high-leverage points in the EDA Step

- **Current Observation:**  
  - The scatter plots that compare factors (momentum, volatility, average volume) with daily returns show many outliers and high-leverage points.
  
- **Future Improvement:**  
  - Implement methods to detect and potentially remove outliers and high-leverage points on the model.
  
---

## 3. Hyperparameter Tuning for ML Models

- **Current Limitation:**  
  - The models (XGBoost and Random Forest) are used with fixed hyperparameters.  
  - A time series split cross-validation has not been implemented due to the short rebalance period (21 days), which may limit the available data for robust validation.

- **Future Improvement:**  
  - Tune hyperparameters using a time series split cross-validation. Use the portfolio's total return as the loss function.
  
---

## 4. Noise Filtering in the Covariance Matrix

- **Current Limitation:**  
  - The project uses a standard estimation of the covariance matrix from historical returns without filtering out noise.
  
- **Future Improvement:**  
  - Use the Marchenko-Pastur distribution to filter out noisy eigenvalues from the covariance matrix. This process can lead to a "denoised" covariance matrix.

---

