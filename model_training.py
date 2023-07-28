import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score

# Load the data
df = pd.read_csv('Merged/cleaned_merged_all.csv')

# Drop unnecessary columns
df.drop(['match_id', 'season.name', 'season.year'], axis=1, inplace=True)

# Select the categorical columns
cat_columns = df.select_dtypes(include=['object']).columns

# Apply One-Hot Encoding
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoded_features = pd.DataFrame(encoder.fit_transform(df[cat_columns]))
encoded_features.columns = encoder.get_feature_names_out(cat_columns)

# Replace the original categorical columns with the encoded ones
df.drop(cat_columns, axis=1, inplace=True)
df = pd.concat([df, encoded_features], axis=1)

# Define the target variable and the feature matrix
X = df.drop('winnerCode', axis=1)
y = df['winnerCode']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=60)

# Handle imbalanced classes using SMOTE
smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

# Define the models
models = {
    "RandomForest": RandomForestClassifier(n_estimators=100, random_state=80),
    #"GradientBoosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=80),
    #"SVC": SVC(random_state=80),
    "DecisionTree": DecisionTreeClassifier(random_state=80),
    #"KNN": KNeighborsClassifier(),
    "NaiveBayes": GaussianNB(),
    "AdaBoost": AdaBoostClassifier(random_state=80),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="logloss", random_state=80),
    "LightGBM": LGBMClassifier(random_state=80),
    #"CatBoost": CatBoostClassifier(verbose=0, random_state=80),
}

# Loop over models, fit to data, predict and print accuracy
for model_name, model in models.items():
    print(f"Training {model_name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{model_name} accuracy: {accuracy*100:.2f}%\n")
