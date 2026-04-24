# MS Progression Analytics System

## Overview
An end-to-end healthcare analytics pipeline built on synthetic Multiple Sclerosis 
clinical data. Designed to simulate the data infrastructure a healthcare analytics 
team would use to study MS disease progression, relapse patterns, MRI lesion burden, 
and symptom severity across patient cohorts.

This project demonstrates healthcare domain knowledge, ETL pipeline design, and 
clinical data visualization, applicable to healthcare data analyst and clinical 
operations roles.

## Tools
Python, pandas, SQL, Tableau

## Dataset
Synthetic clinical dataset generated programmatically using Python. Includes patient 
demographics, clinical visit records, MRI imaging data, and symptom logs across 
4 MS subtypes: RRMS, SPMS, PPMS, and PRMS.

## What Was Built
- Synthetic data generation engine producing patient, visit, MRI, and symptom 
  records across 4 MS types
- ETL pipeline to clean, merge, and transform multi-table clinical data into a 
  unified analytical dataset
- 6-chart Tableau dashboard visualizing key clinical metrics across MS subtypes

## Dashboard Visualizations
- EDSS Progression by MS Type
- Relapse Frequency by MS Type
- MRI Lesion Count & Volume Trends
- Symptom Score Trends (Fatigue & Mobility)
- Treatment Distribution Across Cohort
- EDSS vs MRI Lesions Correlation Plot

## Files
- `generate_data.py` — synthetic clinical data generation engine
- `clean_columns.py` — data cleaning and column standardization
- `load_clean_merge.py` — ETL pipeline merging patient, visit, symptom, and MRI tables
- `data/patients.csv` — synthetic patient demographics
- `data/visits.csv` — clinical visit records
- `data/symptom_logs.csv` — fatigue and mobility scores per visit
- `data/full_data.csv` — raw merged dataset
- `data/full_data_cleaned.csv` — cleaned analytical dataset
- `executive_summary.pdf` — project overview for non-technical stakeholders

## Tableau Dashboard
https://public.tableau.com/app/profile/kayden.williams2622/viz/MS_PIE/MS_PIE

## Clinical Variables Modeled
| Variable | Description |
|----------|-------------|
| edss | Disability level per Expanded Disability Status Scale |
| relapse_flag | Whether a relapse occurred at that visit |
| treatment | Disease-modifying therapy at time of visit |
| lesion_count / lesion_volume | MRI lesion burden |
| fatigue_score / mobility_score | Symptom severity scores |
| ms_type | RRMS, SPMS, PPMS, PRMS |
| age_at_dx | Patient age at diagnosis |

## Note on Data
All data is synthetically generated and does not represent real patients. 
This project was built to demonstrate healthcare analytics pipeline design 
and clinical data visualization skills.
