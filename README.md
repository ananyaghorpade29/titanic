# 🚢 Titanic Survival Prediction (Machine Learning Project)
🎯 Project Goal

The goal of this project is to predict whether a passenger survived the Titanic disaster using machine learning models based on demographic and travel-related features.

## Project structure

ml-titanic/
├── data/
├── notebooks/
├── src/
├── README.md
└── requirements.txt

## 📊 Dataset
Source: Titanic dataset (Kaggle)
Features include:
 - Age
 - Sex
 - Passenger Class (Pclass)
 - Fare
 - Number of family members (SibSp, Parch)
 - Embarked port
   
## ⚙️ Models Used
- Logistic Regression
- Decision Tree
- Random Forest
  
## 📈 Results
Model	Accuracy	Precision	Recall	F1 Score
Decision Tree	0.82	0.82	0.82	0.82
Logistic Regression	0.82	0.81	0.82	0.81
Random Forest	0.80	0.80	0.80	0.80

## 🔍 Key Findings
- Female passengers had significantly higher survival rates than males
- Higher-class passengers (Pclass=1) had better chances of survival
- Fare (a proxy for wealth) strongly influenced survival
- Age had moderate impact, with children having higher survival rates
- Model results aligned with EDA insights, indicating meaningful learning

## How to run

1. Install dependencies:
pip install -r requirements.txt

2. Open notebooks:
jupyter notebook
## 📊 Visualizations
Survival by Sex

<img width="567" height="455" alt="image" src="https://github.com/user-attachments/assets/644d67dd-7d46-4426-a3b5-a8093936ecf5" />

Age Distribution by Survival

<img width="571" height="455" alt="image" src="https://github.com/user-attachments/assets/2a8fc59d-0a78-4cdd-8bae-3312cde28dd0" />

Feature Importance (Random Forest)

<img width="665" height="455" alt="image" src="https://github.com/user-attachments/assets/974c0136-37f6-4fc1-9d78-325cd86ef8f7" />

## Dataset

Download from Kaggle and place in:
data/raw/

## Tech stack

Python, pandas, numpy, scikit-learn, matplotlib, seaborn

## 📌 Conclusion

Although the Decision Tree achieved the highest test accuracy, it may be prone to overfitting. Random Forest provides a more robust and generalizable solution. Overall, the project demonstrates how machine learning can uncover meaningful patterns from structured data.
