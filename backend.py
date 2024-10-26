import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier

# Load the dataset
heart_data = pd.read_csv('heart.csv')

# check for missing values
print(heart_data.isnull().sum())

# statistical measures about the data
print(heart_data.describe())

# Checking the distribution of Target Variable
print(heart_data['target'].value_counts())

# separating features and target
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

# standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# splitting the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, stratify=Y, random_state=2)

# Initialize the models
logistic_model = LogisticRegression(max_iter=1000)
random_forest_model = RandomForestClassifier(random_state=2)

# define parameter grids for hyperparameter tuning
logistic_param_grid = {
    'C': [0.1, 1, 10],
    'solver': ['liblinear', 'lbfgs']
}

rf_param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

#perform grid search for hyperparameter tuning
logistic_grid_search = GridSearchCV(logistic_model, logistic_param_grid, cv=5, scoring='accuracy')
rf_grid_search = GridSearchCV(random_forest_model, rf_param_grid, cv=5, scoring='accuracy')

#fit the grid search models
logistic_grid_search.fit(X_train, Y_train)
rf_grid_search.fit(X_train, Y_train)

# get the best models
best_logistic_model = logistic_grid_search.best_estimator_
best_rf_model = rf_grid_search.best_estimator_

# accuracy on training data
logistic_train_prediction = best_logistic_model.predict(X_train)
logistic_training_data_accuracy = accuracy_score(logistic_train_prediction, Y_train)
print('Best Logistic Regression Accuracy on Training data:', logistic_training_data_accuracy)

random_forest_train_prediction = best_rf_model.predict(X_train)
random_forest_training_data_accuracy = accuracy_score(random_forest_train_prediction, Y_train)
print('Best Random Forest Accuracy on Training data:', random_forest_training_data_accuracy)

#accuracy on test data
logistic_test_prediction = best_logistic_model.predict(X_test)
logistic_test_data_accuracy = accuracy_score(logistic_test_prediction, Y_test)
print('Best Logistic Regression Accuracy on Test data:', logistic_test_data_accuracy)

random_forest_test_prediction = best_rf_model.predict(X_test)
random_forest_test_data_accuracy = accuracy_score(random_forest_test_prediction, Y_test)
print('Best Random Forest Accuracy on Test data:', random_forest_test_data_accuracy)

#combining predictions using Voting Classifier with tuned models
voting_model = VotingClassifier(estimators=[('lr', best_logistic_model), ('rf', best_rf_model)], voting='hard')
voting_model.fit(X_train, Y_train)

voting_prediction = voting_model.predict(X_test)
voting_test_data_accuracy = accuracy_score(voting_prediction, Y_test)
print('Voting Classifier Accuracy on Test data:', voting_test_data_accuracy)

#


