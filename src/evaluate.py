import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, f1_score

# Load model
model = joblib.load("models/best_model.pkl")

# Load data
df = pd.read_csv("data/Titanic-Dataset.csv")

X = df.drop("Survived", axis=1)
y = df["Survived"]

# Predict
y_pred = model.predict(X)

print("Accuracy:", accuracy_score(y, y_pred))
print("F1 Score:", f1_score(y, y_pred))