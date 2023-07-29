import numpy as np
import pandas as pd
import pickle  # import pickle module
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
from imblearn.ensemble import BalancedRandomForestClassifier
from imblearn.pipeline import Pipeline as imPipeline

# Load the CSV file
df = pd.read_csv('Merged/merged_all.csv')

# Handle missing values
df.replace([np.inf, -np.inf], np.nan, inplace=True)  # replace infinities with NaN

# Identify numeric and categorical columns
num_cols = df.select_dtypes(include=[np.number]).columns
str_cols = df.select_dtypes(include=['object']).columns

# Fill numeric column NaNs with mean and categorical column NaNs with mode
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
df[str_cols] = df[str_cols].fillna(df[str_cols].mode().iloc[0])

# Encoding all non-numeric columns
le = LabelEncoder()
for column in str_cols:
    df[column] = le.fit_transform(df[column])

# Drop columns where all values are NaN
df = df.dropna(axis=1, how='all')

# Define features and target variable
X = df.drop('winnerCode', axis=1)
y = df['winnerCode']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the smallest class size
# You may want to compute this dynamically based on your data
smallest_class_size = 4  # replace with actual value

# Update the SMOTE initialization in your pipeline
pipe = imPipeline([
    ('scaler', StandardScaler()),
    ('smote', SMOTE(k_neighbors=smallest_class_size - 1, random_state=42)),
    ('clf', BalancedRandomForestClassifier(random_state=42))
])

# Hyperparameters grid
param_grid = {
    'clf__n_estimators': [50, 100, 200],
    'clf__max_depth': [None, 10, 20, 30],
    'clf__min_samples_split': [2, 5, 10],
    'clf__min_samples_leaf': [1, 2, 4]
}

# Grid search with cross-validation
grid = GridSearchCV(pipe, param_grid, cv=5, scoring='balanced_accuracy')
grid.fit(X_train, y_train)

print("Best parameters: ", grid.best_params_)
print("Cross-validated balanced accuracy: ", grid.best_score_)

# Evaluate on test set
y_pred = grid.predict(X_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the model
filename = 'finalized_model.sav'  # specify filename
pickle.dump(grid, open(filename, 'wb'))  # save the model to disk
