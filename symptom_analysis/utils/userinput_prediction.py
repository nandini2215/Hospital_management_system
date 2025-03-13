import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings("ignore")

# 🔹 Load the trained and optimized model
rf_model = joblib.load('symptom_analysis/utils/optimized_random_forest_model.pkl')

# 🔹 Load the training data to get feature names
training_data = pd.read_csv('data/Training.csv')

# 🔹 Split data into features and target
X = training_data.drop('prognosis', axis=1)
y = training_data['prognosis']

# 🔹 Fit a scaler on the training data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 🔹 Predict disease based on user symptoms
def predict_disease(symptoms):
    input_data = np.zeros(len(X.columns))  # Initialize with zeros

    for symptom in symptoms:
        if symptom in X.columns:
            input_data[X.columns.get_loc(symptom)] = 1  # Mark symptom presence

    # Scale input data
    input_data = scaler.transform([input_data])

    # Predict disease
    prediction = rf_model.predict(input_data)[0]
    print(f"🩺 Predicted Disease: {prediction}")

# 🔹 Get User Input
user_input = input("Enter symptoms (comma-separated, e.g., itching, skin_rash, nausea): ")
symptoms_list = [sym.strip() for sym in user_input.split(',')]
predict_disease(symptoms_list)
