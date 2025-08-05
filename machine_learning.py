import pandas as pd
from feature_extraction import feature_names

df = pd.read_csv("features.csv")

# Display the first few rows of the DataFrame
print(df.head())

# Display the DataFrame's structure
print(df.info())     

# Use all the features from the shared feature extraction
X = df[feature_names]  

Y = df["type"]  # We want y values to be the type of URL (benign(1) or malicious(0))
print(df["type"].unique())
print(df['type'].value_counts())

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=200, random_state=42)

model.fit(X_train, Y_train)
print("✅ Training complete.")

from sklearn.metrics import classification_report, accuracy_score
Y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(Y_test, Y_pred))
print(classification_report(Y_test, Y_pred))

import joblib
joblib.dump((model, feature_names), "url_model.pkl")
print("Model and feature names saved as 'url_model.pkl'")

df['type'].value_counts()
print("Type counts:\n", df['type'].value_counts())

print("Training feature columns:", list(X.columns))
print("Expected feature names:", feature_names)



