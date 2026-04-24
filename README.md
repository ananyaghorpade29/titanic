<<<<<<< HEAD
# 🚢 Titanic Survival Prediction (Machine Learning Project)
🎯 Project Goal

The goal of this project is to predict whether a passenger survived the Titanic disaster using machine learning models based on demographic and travel-related features.

## Project structure

titanic-ml-project/ 
│ 
├── data/ 
│ └── Titanic-Dataset.csv  
│ 
├── models/ 
│ └── best_model.pkl 
│
├── notebooks/ 
│ ├── titanic01_eda.ipynb 
│ ├── titanic02_preprocessing.ipynb 
│ ├── titanic03_modelcompare.ipynb 
│ ├── titanic04_modelimprovement.ipynb 
│ ├── titanic05_pipeline.ipynb 
│ ├── titanic06_tuning.ipynb 
│ ├── titanic07_modelcomparison.ipynb 
│ ├── titanic08_explainability.ipynb 
│ └── titanic09_evaluation.ipynb 
│ 
├── src/ 
│ ├── pipeline.py 
│ ├── train.py 
│ └── evaluate.py 
│ 
├── models/ 
│ └── best_model.pkl 
│
├──venv/ 
│ └──Lib
│ └──.gitignore
│
├──app.py
├── README.mdrequirements.txt 
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
- XGBoost
- LightGBM ✅ (Best Model)
  
## 📈 Results
| Model                     | Accuracy | F1 Score |
|--------------------------|----------|----------|
| LightGBM                 | 0.82     | 0.75     |
| XGBoost                  | 0.80     | 0.73     |
| Random Forest (Baseline) | 0.79     | 0.72     |
| Random Forest (Tuned)    | 0.79     | 0.71     |
| Logistic Regression      | 0.79     | 0.70     |
| Decision Tree            | 0.75     | 0.67     |

## Hyperparameter Tuning
 Used GridSearchCV and RandomizedSearchCV
 Tuned parameters like:
 - n_estimators
 - max_depth
 - min_samples_split

## 🚀 How to Run
1. Install dependencies
pip install -r requirements.txt

2. Run notebooks
jupyter notebook

3. Train model (script)
python src/train.py

4. Evaluate model
python src/evaluate.py

## 📊 Visualizations
Survival by Sex

<img width="567" height="455" alt="image" src="https://github.com/user-attachments/assets/644d67dd-7d46-4426-a3b5-a8093936ecf5" />

Age Distribution by Survival

<img width="571" height="455" alt="image" src="https://github.com/user-attachments/assets/2a8fc59d-0a78-4cdd-8bae-3312cde28dd0" />

Feature Importance (Random Forest)

<img width="665" height="455" alt="image" src="https://github.com/user-attachments/assets/974c0136-37f6-4fc1-9d78-325cd86ef8f7" />

## 📊 Key Learnings
* Importance of end-to-end ML pipelines
* Model comparison and proper evaluation metrics
* Trade-offs between precision and recall
* Real-world importance of explainability (SHAP)

## 🔍 Key Findings
- Female passengers had significantly higher survival rates than males
- Higher-class passengers (Pclass=1) had better chances of survival
- Fare (a proxy for wealth) strongly influenced survival
- Age had moderate impact, with children having higher survival rates
- Model results aligned with EDA insights, indicating meaningful learning

## Dataset

Download from Kaggle and place in:
data/raw/

## Tech stack

Python, pandas, numpy, scikit-learn, matplotlib, seaborn

=======
# 🚢 Titanic Survival Prediction (Machine Learning Project)
🎯 Project Goal

The goal of this project is to predict whether a passenger survived the Titanic disaster using machine learning models based on demographic and travel-related features.

## Project structure

titanic-ml-project/   
│   
├── data/    
│ └── Titanic-Dataset.csv     
│     
├── models/     
│ └── best_model.pkl     
│     
├── notebooks/     
│ ├── titanic01_eda.ipynb      
│ ├── titanic02_preprocessing.ipynb      
│ ├── titanic03_modelcompare.ipynb     
│ ├── titanic04_modelimprovement.ipynb     
│ ├── titanic05_pipeline.ipynb      
│ ├── titanic06_tuning.ipynb     
│ ├── titanic07_modelcomparison.ipynb        
│ ├── titanic08_explainability.ipynb    
│ └── titanic09_evaluation.ipynb      
│     
├── src/     
│ ├── pipeline.py     
│ ├── train.py     
│ └── evaluate.py     
│     
├── models/      
│ └── best_model.pkl      
│      
├──venv/      
│ └──Lib      
│ └──.gitignore       
│      
├──app.py     
├── README.mdrequirements.txt      
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
- XGBoost
- LightGBM ✅ (Best Model)
  
## 📈 Results
| Model                     | Accuracy | F1 Score |
|--------------------------|----------|----------|
| LightGBM                 | 0.82     | 0.75     |
| XGBoost                  | 0.80     | 0.73     |
| Random Forest (Baseline) | 0.79     | 0.72     |
| Random Forest (Tuned)    | 0.79     | 0.71     |
| Logistic Regression      | 0.79     | 0.70     |
| Decision Tree            | 0.75     | 0.67     |

## Hyperparameter Tuning
 Used GridSearchCV and RandomizedSearchCV
 Tuned parameters like:
 - n_estimators
 - max_depth
 - min_samples_split

## 🚀 How to Run
1. Install dependencies
pip install -r requirements.txt

2. Run notebooks
jupyter notebook

3. Train model (script)
python src/train.py

4. Evaluate model
python src/evaluate.py

## 📊 Visualizations
Survival by Sex

<img width="567" height="455" alt="image" src="https://github.com/user-attachments/assets/644d67dd-7d46-4426-a3b5-a8093936ecf5" />

Age Distribution by Survival

<img width="571" height="455" alt="image" src="https://github.com/user-attachments/assets/2a8fc59d-0a78-4cdd-8bae-3312cde28dd0" />

Feature Importance (Random Forest)

<img width="665" height="455" alt="image" src="https://github.com/user-attachments/assets/974c0136-37f6-4fc1-9d78-325cd86ef8f7" />

## 📊 Key Learnings
* Importance of end-to-end ML pipelines
* Model comparison and proper evaluation metrics
* Trade-offs between precision and recall
* Real-world importance of explainability (SHAP)

## 🔍 Key Findings
- Female passengers had significantly higher survival rates than males
- Higher-class passengers (Pclass=1) had better chances of survival
- Fare (a proxy for wealth) strongly influenced survival
- Age had moderate impact, with children having higher survival rates
- Model results aligned with EDA insights, indicating meaningful learning

## Dataset

Download from Kaggle and place in:
data/raw/

## Tech stack

Python, pandas, numpy, scikit-learn, matplotlib, seaborn

>>>>>>> 5d05f8f181b17c7f41998b9e66f0bdf16a2ad6ef
