import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer
import joblib

# Read the data
df = pd.read_csv('Merged/Cleaned/merged_all.csv')

# Select features and target
features = df[['homeTeam.shortName', 'awayTeam.shortName']]
target = df['winnerCode']
print(features)

# Handle missing values
imputer = SimpleImputer(strategy='most_frequent')
features = pd.DataFrame(imputer.fit_transform(features), columns=features.columns)
print(features)

# Encode categorical variables
le = LabelEncoder()
features['homeTeam.shortName'] = le.fit_transform(features['homeTeam.shortName'])
features['awayTeam.shortName'] = le.fit_transform(features['awayTeam.shortName'])
print(features)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print('Model Accuracy:', accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'model.joblib')
joblib.dump(le, 'label_encoder.joblib')
