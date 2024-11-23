# **Cardiovascular Risk Prediction**

This project focuses on predicting the likelihood of an individual developing cardiovascular diseases (CVD). Using a variety of machine learning algorithms, the goal is to classify individuals into risk categories based on several health-related features.

## **Project Overview**

Cardiovascular disease is one of the leading causes of death worldwide. Early prediction and intervention can significantly reduce mortality rates. In this project, we used various machine learning models to predict cardiovascular risk based on a set of health and lifestyle features.

## **Data Overview**

The dataset used in this project consists of health-related data for individuals, such as age, gender, blood pressure, cholesterol levels, and lifestyle factors. These features are used to predict the likelihood of having cardiovascular disease (CVD). The data is split into two classes: risk (CVD positive) and no risk (CVD negative).

## **Tasks Performed**

### **1. Exploratory Data Analysis (EDA)**
Data Cleaning: Handled missing values, outliers, and inconsistent data.
Visualization: Used bar plots, histograms, and heatmaps to analyze feature distributions, correlations, and trends in the data.
Feature Distribution: Examined the distribution of key features like age, cholesterol, and blood pressure.
Class Distribution: Analyzed the class imbalance and performed visualizations of the target variable (CVD risk).

### **2. Feature Engineering**
Feature Creation: Generated new features based on existing ones to enhance model performance (e.g., BMI from height and weight).
Handling Missing Data: Used techniques like mean/median imputation and removal of rows with excessive missing values.
Normalization/Scaling: Applied standard scaling to numerical features to ensure uniformity and faster model convergence.
Categorical Encoding: Applied One-Hot Encoding to convert categorical variables into numerical format.

### **3. Model Training, Validation and Hyperparameter Tuning**
Split the data: Divided the dataset into training and testing sets (80/20 split).
Model Evaluation: Used a variety of performance metrics like accuracy, precision, recall, F1-score, and ROC-AUC to evaluate the models.
Models Used

The following machine learning models were used for training and prediction:

### **1. Logistic Regression**
A simple linear model used for binary classification.
Performance: Good baseline model for comparison with more complex models.
### **2. Decision Tree**
A tree-based model that uses a set of decision rules to classify the data.
Performance: Handles both categorical and numerical data, but prone to overfitting.
### **3. Random Forest**
An ensemble of decision trees that improves prediction accuracy by averaging multiple decision trees.
Performance: This model performed the best overall, balancing accuracy and recall of the minority class.
### **4. Gradient Boosting**
An ensemble technique that builds trees sequentially to minimize errors made by previous models.
Performance: Improved performance over random forests but computationally expensive.
### **5. AdaBoost**
Another ensemble method that focuses on correcting the errors made by weak learners, emphasizing hard-to-classify examples.
Performance: Good for improving weak models like decision trees.
### **6. XGBoost**
An optimized implementation of gradient boosting that is efficient and often produces state-of-the-art results in classification tasks.
Performance: Performed well, but Random Forest outperformed it in terms of balancing recall for the minority class.

### ** Class Imbalance Handling**
The dataset suffers from class imbalance, with significantly fewer cases of cardiovascular risk compared to those without. To address this, we applied the following techniques:

### **1. Under-Sampling**
Randomly reducing the majority class (no-risk) to balance the dataset.
### **2. Over-Sampling**
Randomly duplicating the minority class (risk) to achieve balance.
### **3. SMOTE (Synthetic Minority Over-sampling Technique)**
Generates synthetic samples for the minority class to improve model learning.
### **4. SMOTE Tomek**
Combines SMOTE with Tomek links, which removes noisy and borderline examples from the dataset.

### **Hyperparameter Tuning**
To optimize the performance of the models, hyperparameter tuning was performed, particularly to improve the recall of the minority class. Random Forest benefited significantly from tuning the following hyperparameters:

n_estimators: The number of trees in the forest.
max_depth: The maximum depth of the trees.
min_samples_split: The minimum number of samples required to split an internal node.
min_samples_leaf: The minimum number of samples required to be at a leaf node.
These adjustments helped enhance the recall of the minority class (CVD positive) without sacrificing too much precision, leading to a better model for predicting individuals at risk of cardiovascular disease.

## **Model Performance**

The following key metrics were used to evaluate model performance:

Accuracy: The overall correctness of the model.
Precision: The proportion of positive predictions that were actually correct.
Recall: The proportion of actual positive cases correctly identified.
F1-Score: A balance between precision and recall.
ROC-AUC: A measure of how well the model distinguishes between classes.
Random Forest emerged as the best-performing model after hyperparameter tuning, with an improved recall score for the minority class, making it the most effective for identifying high-risk individuals.

## **Conclusion**

This project demonstrates how to use various machine learning algorithms to predict cardiovascular risk based on health-related features. Several techniques were employed to address class imbalance, and Random Forest emerged as the best-performing model after hyperparameter tuning, particularly for optimizing recall for the minority class. Future work could explore further hyperparameter optimization, feature selection, and deep learning models.
