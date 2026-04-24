import pandas as pd
import joblib
from lightgbm import LGBMClassifier
from pipeline import build_pipeline

# Load data
df = pd.read_csv("data/Titanic-Dataset.csv")

x = df.drop("Survived", axis=1)
y = df["Survived"]

# Build pipeline
model = LGBMClassifier(random_state=42)
pipeline = build_pipeline(model)

# Train
pipeline.fit(x, y)

# Save model
joblib.dump(pipeline, "models/best_model.pkl")

print("Model trained and saved!")