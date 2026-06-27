# Fraud Transaction Detection using Machine Learning

## Project Overview

This project focuses on developing a machine learning-based Fraud Transaction Detection system to classify transactions as fraudulent or legitimate.
A Random Forest classifier was trained to learn transaction patterns and identify suspicious activities effectively.


## Objective

The primary objective of this project is to develop a machine learning-based fraud detection system that can accurately classify transactions as fraudulent or legitimate while addressing the challenges posed by highly imbalanced transaction data.


## Dataset Information

* Total Transactions: **1,754,155**
* Target Variable: **TX_FRAUD**

  * `0` → Legitimate Transaction
  * `1` → Fraudulent Transaction

### Features Used for Training

* CUSTOMER_ID
* TERMINAL_ID
* TX_AMOUNT
* TX_TIME_SECONDS
* TX_TIME_DAYS


## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Imbalanced-learn
* Jupyter Notebook


## Methodology

The following steps were followed during the development of the project:

1. Data Collection
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Train-Test Split
5. Random Forest Model Training
6. Model Evaluation
7. Handling Class Imbalance

   * Balanced Random Forest
   * SMOTE Oversampling
8. Model Comparison
9. Final Model Selection


## Model Performance

| Model                  | Accuracy | Precision | Recall | F1 Score |
| ---------------------- | -------- | --------- | ------ | -------- |
| Random Forest          | 99.36%   | 1.00      | 0.24   | 0.39     |
| Balanced Random Forest | 99.00%   | 1.00      | 0.23   | 0.37     |
| Random Forest + SMOTE  | 94.00%   | 0.04      | 0.31   | 0.08     |


## Final Model Selection

Based on the model comparison results, the original **Random Forest** model achieved accuracy, precision, and reliability and was selected as the final model.


## Conclusion

* A Fraud Transaction Detection system was successfully developed to classify transactions as fraudulent or legitimate.
* The Random Forest model achieved the best overall performance and was selected as the final model.
* The developed system can assist in improving fraud detection efficiency in real-world financial systems.



