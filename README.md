# XGBoost Classifier for Predicting Customer Behavior and Product Likeability
Repository for our solution for the Alkemy Spa hackaton in collaboration with PMDS, which we won second place.

This project implements an XGBoost classifier for predicting customer behavior and product likeability based on a dataset of features and target labels. The workflow includes data preprocessing, hyperparameter tuning, model training, evaluation, and feature importance analysis using SHAP values.


## Overview

This project uses the XGBoost classifier to predict customer behavior and product likeability. The code performs the following tasks:

1. Load preprocessed data.
2. Create data transformation pipelines for numerical and categorical features.
3. Initialize and train an XGBoost classifier.
4. Perform hyperparameter tuning using `GridSearchCV`.
5. Evaluate the model using confusion matrices, classification reports, and ROC AUC scores.
6. Use the SHAP library to analyze feature importance.

## Data Loading

The project loads two CSV files:

- **X_train.csv**: Contains the training feature data.
- **y_train.csv**: Contains the target labels.
- **test_en2.csv**: Contains new test data for predictions.
