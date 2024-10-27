# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Exercise 4: generate a scatter plot between two features

x = df['sepal length (cm)']
y = df['sepal width (cm)']

# Creating Scatter Plot
plt.scatter(x, y)

# Adding title and labels
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')

# Plot Display
plt.show()
