import joblib
import pandas as pd
from sklearn.impute import SimpleImputer

# Load the model and the label encoder from the files
model = joblib.load('model.joblib')
le = joblib.load('label_encoder.joblib')

# Example new data
new_data = pd.DataFrame({
    'homeTeam.shortName': ['China'],
    'awayTeam.shortName': ['Denmark']
})

# Handle missing values (if any)
imputer = SimpleImputer(strategy='most_frequent')
new_data = pd.DataFrame(imputer.fit_transform(new_data), columns=new_data.columns)

# Encode the team names
new_data['homeTeam.shortName'] = le.transform(new_data['homeTeam.shortName'])
new_data['awayTeam.shortName'] = le.transform(new_data['awayTeam.shortName'])
print(new_data)
# Use the model to predict the 'winnerCode'
prediction = model.predict(new_data)

print('Predicted winnerCode:', prediction[0])
