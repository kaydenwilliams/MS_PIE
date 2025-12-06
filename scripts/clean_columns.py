import pandas as pd
import os

# Load the merged dataset
base_path = os.path.join(os.path.dirname(__file__), '../data')
full_df = pd.read_csv(os.path.join(base_path, 'full_data.csv'))

# -------------------- Step 1: Inspect columns --------------------
print("Original columns:\n", full_df.columns)

# -------------------- Step 2: Rename columns --------------------
full_df.rename(columns={
    'patient_id_x': 'patient_id',
    'patient_id_y': 'patient_id_mri',
    'patient_id': 'patient_id_symptoms'  # if needed
}, inplace=True)

# Optional: reorder columns for clarity
cols = ['visit_id', 'patient_id', 'visit_date', 'edss', 'relapse_flag', 'treatment',
        'mri_id', 'lesion_count', 'lesion_volume',
        'log_id', 'fatigue_score', 'mobility_score', 'sex', 'age_at_dx', 'ms_type', 'dx_date']
full_df = full_df[cols]

# -------------------- Step 3: Save cleaned CSV --------------------
full_df.to_csv(os.path.join(base_path, 'full_data_clean.csv'), index=False)
print("Cleaned dataset saved as full_data_clean.csv")
