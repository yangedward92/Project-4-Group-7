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


if __name__ == "__main__":
    # Create an instance of ModelHelper
    model_helper = ModelHelper()

    # Provide sample inputs
    Pregnancies = 2
    Glucose = 120
    BloodPressure = 70
    SkinThickness = 20
    Insulin = 85
    BMI = 25.5
    DiabetesPedigreeFunction = 0.5
    Age = 30

    # Call the make_predictions method
    try:
        result = model_helper.make_predictions(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        print(f"Predicted probability of diabetes: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")