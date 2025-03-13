import numpy as np
import pandas as pd
import joblib

# 🔹 Load the trained model and scaler
rf_model = joblib.load("D:\\Med_Insight\\symptom_analysis\\utils\\optimized_random_forest_model.pkl")
scaler = joblib.load("D:\\Med_Insight\\symptom_analysis\\utils\\random_scaler.pkl")

# 🔹 Load Datasets
description_df = pd.read_csv("data\description.csv")[['Disease', 'Description']]
precautions_df = pd.read_csv("data\precautions_df.csv")[['Disease', 'Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
medications_df = pd.read_csv("data\medications.csv")[['Disease', 'Medication']]
diets_df = pd.read_csv("data\diets.csv")[['Disease', 'Diet']]
workouts_df = pd.read_csv("data\workout_df.csv")[['disease', 'workout']]

# 🔹 Load Symptoms Dataset for Features
training_data = pd.read_csv("data\Training.csv")  # Ensure this matches the training dataset
all_symptoms = training_data.columns[:-1]  # Exclude the 'prognosis' column

# 🔹 Function to Predict Disease
def predict_disease(symptoms):
    input_data = np.zeros(len(all_symptoms))  # Initialize input array with zeros

    for symptom in symptoms:
        if symptom in all_symptoms:
            input_data[list(all_symptoms).index(symptom)] = 1  # Set 1 for present symptoms

    input_data = scaler.transform([input_data])  # Scale input
    predicted_disease = rf_model.predict(input_data)[0]  # Get the predicted disease

    return predicted_disease

# 🔹 Function to Retrieve Disease Information
def get_disease_info(disease):
    description = description_df.loc[description_df['Disease'] == disease, 'Description'].values
    precautions = precautions_df.loc[precautions_df['Disease'] == disease, ['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values
    medications = medications_df.loc[medications_df['Disease'] == disease, 'Medication'].values
    diet = diets_df.loc[diets_df['Disease'] == disease, 'Diet'].values
    workout = workouts_df.loc[workouts_df['disease'] == disease, 'workout'].values

    # Format Results
    return {
        "Description": description[0] if len(description) > 0 else "No description available",
        "Precautions": precautions[0].tolist() if len(precautions) > 0 else ["No precautions available"],
        "Medications": medications.tolist() if len(medications) > 0 else ["No medications available"],
        "Diet": diet[0] if len(diet) > 0 else "No diet available",
        "Workout": workout[0] if len(workout) > 0 else "No workout available",
    }

# 🔹 Get User Input
user_input = input("Enter symptoms (comma-separated, e.g., itching, skin_rash, nausea): ")
symptoms_list = [sym.strip() for sym in user_input.split(',')]

# 🔹 Predict Disease & Retrieve Details
predicted_disease = predict_disease(symptoms_list)
disease_info = get_disease_info(predicted_disease)

# 🔹 Display Results
print(f"\n🩺 Predicted Disease: {predicted_disease}\n")
print(f"📖 Description: {disease_info['Description']}\n")
print(f"⚕️ Medications: {', '.join(disease_info['Medications'])}\n")
print(f"🛑 Precautions: {', '.join(disease_info['Precautions'])}\n")
print(f"🥗 Recommended Diet: {disease_info['Diet']}\n")
print(f"🏋️ Workout Suggestions: {disease_info['Workout']}\n")
