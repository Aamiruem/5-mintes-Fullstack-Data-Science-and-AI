# Import necessary libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load sample data (e.g., the Iris dataset)
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Create a Decision Tree Classifier object
clf = DecisionTreeClassifier()

# Train the Decision Tree Classifier
clf = clf.fit(X_train, y_train)

# Make predictions (optional)
y_pred = clf.predict(X_test)

# Visualize the tree (optional)
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=feature_names, class_names=target_names, filled=True, rounded=True)
plt.show()
