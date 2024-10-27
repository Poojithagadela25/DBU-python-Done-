# Objective: Apply data science concepts on a dataset of your choice.

# Tasks:
    

# Step 1.) ---> Acquire, clean, and preprocess data.

# Required Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (Example: Kaggle dataset 'Heart Disease UCI')
data = pd.read_csv('heart.csv')

# Data cleaning: Handling missing values (if any)
data.fillna(data.mean(), inplace=True)

# Label Encoding for categorical features
le = LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])

# Feature Scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data.drop('target', axis=1))

# Splitting the dataset into train and test sets
X = scaled_features
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Step 2 ---> Perform EDA and visualize key insights.

# EDA: Exploratory Data Analysis :-

# Visualization 1: Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Visualization 2: Target distribution
plt.figure(figsize=(6,4))
sns.countplot(x='target', data=data)
plt.title('Target Distribution')
plt.show()

# Visualization 3: Boxplot of age vs target
plt.figure(figsize=(6,4))
sns.boxplot(x='target', y='age', data=data)
plt.title('Age vs Target')
plt.show()


# Step 3.) ---> Build and evaluate a machine learning model.

from sklearn.linear_model import LogisticRegression

# Building the model: Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
classification_report_result = classification_report(y_test, y_pred)

# Print evaluation results
print(f'Accuracy: {accuracy * 100:.2f}%')
print('Classification Report:\n', classification_report_result)

# Additional Evaluation Metric: Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')



# Requirements:
    # Work on this as a group (Same team as the previous GIT exercise).
    # Use a dataset that is not used in the class.
    # Use at least 3 different visualization techniques.
    # Use at least 1 different machine learning algorithms.
    # Use at least 2 different evaluation metrics.
    # Use at least 2 different preprocessing techniques.

# Submission Timeline:
    # Submit the code and a report in 3 weeks.
    # The report should include:
        # Introduction to the dataset.
        # Data cleaning and preprocessing steps.
        # EDA and key insights.
        # Machine learning model building and evaluation.
        # Conclusion.
        # References (if any).
