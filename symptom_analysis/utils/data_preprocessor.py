import pandas as pd
import os
from data_loader import load_dataset

# Function to clean a dataset
def clean_dataset(df, name):
    print(f"\n🧹 Cleaning {name} dataset")

    # Handling missing values
    missing_values = df.isnull().sum()
    print(f"Missing values:\n{missing_values}")

    # Filling or dropping missing values (customize per dataset)
    df = df.dropna()  # We can also use fillna() depending on requirements

    # Removing duplicates
    duplicates = df.duplicated().sum()
    if duplicates:
        print(f"Found {duplicates} duplicate rows — removing them")
        df = df.drop_duplicates()

    # Standardizing column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Ensuring data types are consistent
    print(f"Updated data types:\n{df.dtypes}")

    print(f"✅ {name} dataset cleaned successfully!")
    return df

if __name__ == "__main__":
    datasets = ['description', 'diets', 'medications', 'precautions', 'symptom_severity', 'symptoms', 'training', 'workouts']

    for dataset in datasets:
        df = load_dataset(dataset)
        if df is not None:
            cleaned_df = clean_dataset(df, dataset)
            print(cleaned_df.head())
