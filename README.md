# Fraud Transaction Detection

## Project Overview

This project focuses on developing a machine learning-based Fraud Transaction Detection system to classify transactions as fraudulent or legitimate. A Random Forest classifier was trained to learn transaction patterns and identify suspicious activities effectively.

## Objective

The primary objective of this project is to develop a machine learning-based fraud detection system that can accurately classify transactions as fraudulent or legitimate while addressing the challenges posed by highly imbalanced transaction data.

## Dataset Information

- Total Transactions: **1,754,155**
- Target Variable: **TX_FRAUD**

### Target Classes

- `0` → Legitimate Transaction
- `1` → Fraudulent Transaction

### Features Used for Training

- CUSTOMER_ID
- TERMINAL_ID
- TX_AMOUNT
- TX_TIME_SECONDS
- TX_TIME_DAYS

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- Streamlit
- Joblib
- Jupyter Notebook

## Methodology

The following steps were followed during the development of the project:

1. Data Overview
2.Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Train-Test Split
5. Random Forest Model Training
6. Model Evaluation
7. Handling Class Imbalance
   - Random Forest with Class Weights
   - SMOTE Oversampling
8. Model Comparison
9. Final Model Selection

## Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Random Forest | 99.36% | 100.00% | 24.00% | 39.00% |
| Random Forest with Class Weights | 99.00% | 100.00% | 23.00% | 37.00% |
| Random Forest + SMOTE | 94.00% | 4.00% | 31.00% | 8.00% |

## Final Model Selection

Random Forest, Random Forest with Class weights, and Random Forest with SMOTE Oversampling models were trained and evaluated for fraud transaction detection.

Among all the models, the original Random Forest classifier achieved the highest overall performance by maintaining excellent accuracy and perfect precision while producing reliable fraud detection results.

Although SMOTE improved recall performance, it significantly reduced precision and overall reliability. Similarly, Random Forest with Class Weights did not provide any considerable improvement over the original Random Forest model.

Since minimizing false fraud alerts is extremely important in financial applications, **the Random Forest classifier** was selected as the final model for Fraud Transaction Detection.

## Streamlit Web Application

A Streamlit-based web application was developed to provide an interactive interface for Fraud Transaction Detection.

The application allows users to enter transaction information and instantly predicts whether the transaction is fraudulent or legitimate using the trained machine learning model.

## Project Files

- `Fraud Transaction Detection.ipynb` - Complete notebook containing data preprocessing, model training, and evaluation.
- `app.py` - Streamlit web application for fraud transaction detection.
- `fraud_detection_model.pkl` - Saved trained Random Forest model.
- `requirements.txt` - Required Python packages for running the application and reproducing the project environment.
- `README.md` - Project documentation.

## Conclusion

A Fraud Transaction Detection system was successfully developed to classify transactions as fraudulent or legitimate.

The Random Forest model achieved the best overall performance and was selected as the final model.

The developed system can assist in improving fraud detection efficiency in real-world financial systems.



