# Limitations and Future Improvements

This document discusses some of the current limitations of the project as well as possible enhancements for future iterations.

---

## 1. Flexibility in the Pick Matrix (P)

- **Current Limitation:**  
  - Currently, the project uses an identity matrix as the pick matrix (P) in the Black-Litterman model. This approach assigns an absolute view for each asset.
  
- **Future Improvement:**  
  - **Flexible View Specification:** Allow for more general forms of the pick matrix.  
    - **Relative Views:** Enable users to specify views that compare assets (e.g., "Asset A will outperform Asset B by X%").
    - **Grouped Views:** Allow grouping of assets into clusters and expressing views on these clusters rather than on individual assets.
    - **Custom Views:** Provide an interface or configuration setting that lets users define their own P matrices tailored to different investment hypotheses.

- **Elaboration:**  
  - In the Black-Litterman framework, the pick matrix P plays a central role in encoding investor views. By moving beyond the identity matrix, you not only allow for absolute views but also relative and composite views. This flexibility can lead to a more nuanced and potentially more accurate formulation of the portfolio allocation problem.

---

## 2. Handling Outliers in the EDA Step

- **Current Observation:**  
  - The scatter plots that compare factors (momentum, volatility, average volume) with daily returns show many outliers and high-leverage points.
  
- **Future Improvement:**  
  - **Outlier Detection and Removal:** Implement methods to detect and potentially remove high-leverage points. This could include:
    - Statistical thresholds (e.g., using z-scores, IQR).
    - Visualization-based filtering.
  - **Robust Regression Techniques:**  
    - Explore using robust regression methods such as Huber Regression, RANSAC, or Theil–Sen estimators that reduce the influence of outliers on the model.
  
- **Elaboration:**  
  - Outliers can disproportionately influence ordinary least squares (OLS) estimates, leading to suboptimal portfolio adjustments. Applying robust regression techniques will help ensure that extreme values do not distort the expected return calculations and ultimately improve the reliability of the asset allocation decisions.

---

## 3. Hyperparameter Tuning for ML Models

- **Current Limitation:**  
  - The models (XGBoost and Random Forest) are used with fixed hyperparameters.  
  - A time series cross-validation split has not been implemented due to the short rebalance period (21 days), which may limit the available data for robust validation.

- **Future Improvement:**  
  - **Time Series Cross-Validation:**  
    - Use methods like rolling window or expanding window cross-validation specifically designed for time series data.  
    - Optimize hyperparameters with a focus on the end goal—for example, using the portfolio’s total return as the loss function.
  
- **Elaboration:**  
  - Although the short rebalance period poses challenges in terms of available observations, advanced time series CV techniques (such as a rolling or expanding window approach) can still be applied. This ensures that the models are well-calibrated to predict returns in a dynamic market environment. Even if the data is limited, a systematic evaluation of hyperparameters can further enhance model performance and, consequently, the portfolio optimization process.

---

## 4. Noise Filtering in the Covariance Matrix

- **Current Limitation:**  
  - The project uses a standard estimation of the covariance matrix from historical returns without filtering out noise.
  
- **Future Improvement:**  
  - **Application of the Marchenko-Pastur Theorem:**  
    - Use the Marchenko-Pastur distribution to filter out noisy eigenvalues from the covariance matrix.
    - This process can lead to a "denoised" covariance matrix that may better capture the underlying risk structure.
  
- **Elaboration:**  
  - The Marchenko-Pastur theorem describes the distribution of eigenvalues for a random covariance matrix. By comparing the empirical eigenvalue distribution to this theoretical distribution, one can identify and remove components largely attributed to noise. This denoising process can improve risk estimation and enhance the robustness of the portfolio optimization process.

---

Overall, these future improvements aim to enhance the flexibility, robustness, and accuracy of the model, addressing both statistical and operational limitations identified in the current implementation.
