from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def build_pipeline(model):
    categorical_cols= ["Sex","Embarked"]
    numerical_cols= ["Age","Fare","Pclass","SibSp","Parch"]
    
    numeric_pipeline= Pipeline([
        ("imputer",SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])
    categorical_pipeline= Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder",OneHotEncoder(drop="first"))
    ])
    preprocessor= ColumnTransformer([
        ("num",numeric_pipeline, numerical_cols),
        ("cat", categorical_pipeline, categorical_cols)
    ])
    model_pipeline= Pipeline([
        ("preprocessing",preprocessor),
        ("model",model)
    ])
    return model_pipeline