import pandas as pd
# import numpy as np
import pickle


class ModelHelper():
    def __init__(self):
        pass

    def make_predictions(self, Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
        df = pd.DataFrame()
        df["Pregnancies"] = [Pregnancies]
        df["Glucose"] = [Glucose]
        df["BloodPressure"] = [BloodPressure]
        df["SkinThickness"] = [SkinThickness]
        df["Insulin"] = [Insulin]
        df["BMI"] = [BMI]
        df["DiabetesPedigreeFunction"] = [DiabetesPedigreeFunction]
        df["Age"] = [Age]
        
        # Load model
        model = pickle.load(open("diabetes_model.h5", 'rb'))

        preds = model.predict_proba(df)
        has_diabetes = preds[0][1]

        return(has_diabetes)
