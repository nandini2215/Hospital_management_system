import pandas as pd
import os

# FIXED: Hardcoded absolute path to the data folder
data_folder = r'D:\Med_Insight\data'  # Adjust this to your exact data folder path

# Dataset file names
datasets = {
    'description': 'description.csv',
    'diets': 'diets.csv',
    'medications': 'medications.csv',
    'precautions': 'precautions_df.csv',
    'symptom_severity': 'Symptom-severity.csv',
    'symptoms': 'symptoms_df.csv',# Confirmed the corrected name
    'training': 'Training.csv',
    'workouts': 'workout_df.csv' 
}

# Function to load a dataset
def load_dataset(name):
    file_path = os.path.join(data_folder, datasets.get(name, ''))
    print(f"🔍 Looking for file at: {file_path}")  # Debug line
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            print(f"✅ Successfully loaded {name}")
            return df
        except Exception as e:
            print(f"❌ Error loading {name}: {e}")
            return None
    else:
        print(f"❌ File not found: {file_path}")
        return None

# Function to inspect the datasets
def inspect_data(name):
    df = load_dataset(name)
    if df is not None:
        print(f"\n🔍 Inspecting {name} dataset:")
        print(f"Shape: {df.shape}")
        print(df.info())
        print(df.head(), "\n")

# Example usage
if __name__ == "__main__":
    print(f"🗂️ Data folder absolute path: {data_folder}")
    print("🚀 Starting data inspection")
    for dataset in datasets:
        inspect_data(dataset)
