from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

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
training_data = pd.read_csv("data\Training.csv")
all_symptoms = training_data.columns[:-1]

# 🔹 Function to Predict Disease
def predict_disease(symptoms):
    input_data = np.zeros(len(all_symptoms))

    for symptom in symptoms:
        symptom = symptom.strip().lower().replace(' ', '_')
        if symptom in all_symptoms:
            input_data[list(all_symptoms).index(symptom)] = 1

    input_data = scaler.transform([input_data])
    predicted_disease = rf_model.predict(input_data)[0]
    
    return predicted_disease

# 🔹 Function to Retrieve Disease Information
def get_disease_info(disease):
    description = description_df.loc[description_df['Disease'] == disease, 'Description'].values
    precautions = precautions_df.loc[precautions_df['Disease'] == disease, ['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values
    medications = medications_df.loc[medications_df['Disease'] == disease, 'Medication'].values
    diet = diets_df.loc[diets_df['Disease'] == disease, 'Diet'].values
    workout = workouts_df.loc[workouts_df['disease'] == disease, 'workout'].values

    return {
        "disease": disease,
        "description": description[0] if len(description) > 0 else "No description available",
        "precautions": precautions[0].tolist() if len(precautions) > 0 else ["No precautions available"],
        "medications": medications.tolist() if len(medications) > 0 else ["No medications available"],
        "diet": diet[0] if len(diet) > 0 else "No diet available",
        "workout": workout[0] if len(workout) > 0 else "No workout available",
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        symptoms = [sym.strip().lower().replace(' ', '_') for sym in data.get('symptoms', '').split(',')]

        if not symptoms:
            return jsonify({'error': 'No symptoms provided'}), 400

        predicted_disease = predict_disease(symptoms)
        disease_info = get_disease_info(predicted_disease)

        return jsonify(disease_info)

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to make prediction"}), 500

if __name__ == "__main__":
    app.run(debug=True)
