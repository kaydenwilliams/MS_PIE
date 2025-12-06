import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuration
num_patients = 20
years_of_data = 5
treatments = ['Interferon', 'Ocrelizumab', 'Fingolimod', 'Natalizumab', 'Ofatumumab']
ms_types = ['RRMS', 'PPMS', 'SPMS', 'PRMS']

def random_date(start_year, end_year):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))

# Patients
patients = []
for pid in range(1, num_patients+1):
    sex = random.choice(['M','F'])
    age = random.randint(18,60)
    ms_type = random.choices(ms_types, weights=[0.7, 0.1, 0.15, 0.05], k=1)[0]
    dx_date = random_date(2008,2023).strftime('%Y-%m-%d')
    patients.append([pid, sex, age, ms_type, dx_date])

df_patients = pd.DataFrame(patients, columns=['patient_id','sex','age_at_dx','ms_type','dx_date'])
df_patients.to_csv('patients.csv', index=False)

# Visits
visits = []
visit_id = 1
for pid in df_patients['patient_id']:
    start_date = datetime.strptime(df_patients.loc[df_patients['patient_id']==pid,'dx_date'].values[0], '%Y-%m-%d')
    for year in range(years_of_data):
        num_visits = random.randint(2,4)
        for _ in range(num_visits):
            visit_date = start_date + timedelta(days=random.randint(0,365))
            edss = round(random.uniform(0,7),1)
            relapse_flag = np.random.choice([0,1], p=[0.85,0.15])
            treatment = random.choice(treatments)
            visits.append([visit_id, pid, visit_date.strftime('%Y-%m-%d'), edss, relapse_flag, treatment])
            visit_id += 1
        start_date += timedelta(days=365)

df_visits = pd.DataFrame(visits, columns=['visit_id','patient_id','visit_date','edss','relapse_flag','treatment'])
df_visits.to_csv('visits.csv', index=False)

# MRI
mri = []
mri_id = 1
for pid in df_patients['patient_id']:
    start_date = datetime.strptime(df_patients.loc[df_patients['patient_id']==pid,'dx_date'].values[0], '%Y-%m-%d')
    for year in range(years_of_data):
        num_scans = random.randint(1,2)
        for _ in range(num_scans):
            scan_date = start_date + timedelta(days=random.randint(0,365))
            lesion_count = random.randint(0,30)
            lesion_volume = round(random.uniform(0,20),2)
            mri.append([mri_id, pid, scan_date.strftime('%Y-%m-%d'), lesion_count, lesion_volume])
            mri_id += 1
        start_date += timedelta(days=365)

df_mri = pd.DataFrame(mri, columns=['mri_id','patient_id','scan_date','lesion_count','lesion_volume'])
df_mri.to_csv('mri_findings.csv', index=False)

# Symptom logs
symptoms = []
log_id = 1
for pid in df_patients['patient_id']:
    start_date = datetime.strptime(df_patients.loc[df_patients['patient_id']==pid,'dx_date'].values[0], '%Y-%m-%d')
    num_logs = years_of_data * 12  # monthly logs
    for i in range(num_logs):
        log_date = start_date + timedelta(days=i*30)
        fatigue_score = random.randint(1,10)
        mobility_score = random.randint(1,10)
        symptoms.append([log_id, pid, log_date.strftime('%Y-%m-%d'), fatigue_score, mobility_score])
        log_id += 1

df_symptoms = pd.DataFrame(symptoms, columns=['log_id','patient_id','log_date','fatigue_score','mobility_score'])
df_symptoms.to_csv('symptom_logs.csv', index=False)

print("Synthetic CSVs generated: patients.csv, visits.csv, mri_findings.csv, symptom_logs.csv")
