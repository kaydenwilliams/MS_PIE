import pandas as pd
import os

# -------------------- Step 0: Set paths --------------------
base_path = os.path.join(os.path.dirname(__file__), '../data')

patients_path = os.path.join(base_path, 'patients.csv')
visits_path = os.path.join(base_path, 'visits.csv')
mri_path = os.path.join(base_path, 'mri_findings.csv')
symptoms_path = os.path.join(base_path, 'symptom_logs.csv')

# -------------------- Step 1: Load CSVs --------------------
df_patients = pd.read_csv(patients_path)
df_visits = pd.read_csv(visits_path)
df_mri = pd.read_csv(mri_path)
df_symptoms = pd.read_csv(symptoms_path)

# -------------------- Step 2: Convert Columns --------------------
df_patients['dx_date'] = pd.to_datetime(df_patients['dx_date'])
df_visits['visit_date'] = pd.to_datetime(df_visits['visit_date'])
df_mri['scan_date'] = pd.to_datetime(df_mri['scan_date'])
df_symptoms['log_date'] = pd.to_datetime(df_symptoms['log_date'])

# Numeric columns
df_visits['edss'] = df_visits['edss'].astype(float)
df_visits['relapse_flag'] = df_visits['relapse_flag'].astype(int)
df_mri['lesion_count'] = df_mri['lesion_count'].astype(int)
df_mri['lesion_volume'] = df_mri['lesion_volume'].astype(float)
df_symptoms['fatigue_score'] = df_symptoms['fatigue_score'].astype(int)
df_symptoms['mobility_score'] = df_symptoms['mobility_score'].astype(int)

# -------------------- Step 3: Inspect & Clean --------------------
print("Patients head:\n", df_patients.head())
print("Visits head:\n", df_visits.head())
print("MRI head:\n", df_mri.head())
print("Symptoms head:\n", df_symptoms.head())

df_patients.drop_duplicates(inplace=True)
df_visits.drop_duplicates(inplace=True)
df_mri.drop_duplicates(inplace=True)
df_symptoms.drop_duplicates(inplace=True)

# -------------------- Step 4: Merge Tables per patient --------------------
# Merge visits with patients
visits_patients = pd.merge(df_visits, df_patients, on='patient_id', how='left')

merged_list = []

for pid, group in visits_patients.groupby('patient_id'):
    group = group.sort_values('visit_date')

    mri_group = df_mri[df_mri['patient_id'] == pid].sort_values('scan_date')
    symptoms_group = df_symptoms[df_symptoms['patient_id'] == pid].sort_values('log_date')

    group_mri = pd.merge_asof(group, mri_group, left_on='visit_date', right_on='scan_date', direction='nearest')
    group_full = pd.merge_asof(group_mri, symptoms_group, left_on='visit_date', right_on='log_date',
                               direction='nearest')

    merged_list.append(group_full)

full_df = pd.concat(merged_list, ignore_index=True)
full_df = full_df.drop(columns=['scan_date', 'log_date'])

print("\nFull merged data head:\n", full_df.head())

# -------------------- Step 5: Save Cleaned, Merged CSV --------------------
full_data_path = os.path.join(base_path, 'full_data.csv')
full_df.to_csv(full_data_path, index=False)
print(f"\nMerged dataset saved as {full_data_path}")
