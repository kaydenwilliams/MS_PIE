# MS_PIE
# 🧠 MS Progression Analytics  
**An Analytical Case Study Using Synthetic Multiple Sclerosis (MS) Clinical Data**

This project analyzes a synthetic clinical dataset to explore **MS progression patterns**, **relapse frequency**, **MRI lesion burden**, and **symptom trends**.  
It demonstrates analytical rigor, data storytelling, and the ability to generate insights that support clinical or operational decision-making.

The dataset includes:  
`visit_id, patient_id, visit_date, edss, relapse_flag, treatment, mri_id, lesion_count, lesion_volume, log_id, fatigue_score, mobility_score, sex, age_at_dx, ms_type, dx_date`

---

## 📌 Project Overview

This project simulates how a healthcare analytics team might study MS disease activity across different patient types. The analysis focuses on:

- Disability progression (via **EDSS** scores)  
- Relapse frequency  
- MRI lesion burden  
- Symptom severity (fatigue & mobility)  
- Treatment distribution patterns  

The goal is to highlight how structured clinical data can be transformed into **insights and visualizations** that inform decisions.

---

## 🔍 Key Findings & Insights

### 1️⃣ EDSS Progression Varies by MS Type  
Across the synthetic dataset:
- **SPMS and PPMS** patients show more consistent upward EDSS trends.  
- **RRMS** patients show fluctuating EDSS patterns due to relapses and partial recovery.  

**Interpretation:** Different MS types show distinct progression behaviors, underscoring the importance of type-specific monitoring strategies.

---

### 2️⃣ Relapse Frequency is Highest in RRMS  
The “relapse_flag” analysis shows:
- RRMS patients exhibit **more frequent relapses**, as expected.  
- Progressive types (SPMS/PPMS) show fewer relapses but higher baseline disability.  

**Interpretation:** Relapse monitoring and early symptom reporting are particularly critical in RRMS care pathways.

---

### 3️⃣ MRI Lesion Trends Align with MS Type & Severity  
MRI visualizations indicate:
- RRMS shows **periodic increases** in lesion count/volume around relapse periods.  
- Progressive forms show **stable but elevated lesion burden**.  

**Interpretation:** MRI remains a valuable tool for tracking inflammatory activity and validating clinical changes.

---

### 4️⃣ Symptom Scores Track Well With Disability Levels  
Fatigue and mobility scores demonstrate:
- Positive correlation with EDSS (higher disability = worse symptoms).  
- Progressive MS patients generally exhibit higher symptom burden.  

**Interpretation:** Symptom tracking could help identify early changes before EDSS increases.

---

### 5️⃣ Treatment Distribution Shows Variation Across MS Types  
The dataset’s treatment patterns suggest:
- RRMS patients are the most widely treated.  
- Progressive types have fewer available therapies (reflected in distribution).  

**Interpretation:** Treatment allocation reflects real-life clinical practice where RRMS has the largest treatment portfolio.

---

## 📊 Visualizations Included

This project includes the following Tableau / Python plots:

- **EDSS Progression by MS Type**
- **Relapse Frequency by MS Type**
- **MRI Lesion Count & Volume Trends**
- **Symptom Score Trends (Fatigue & Mobility)**
- **Treatment Distribution Across Cohort**
- **EDSS vs. MRI Lesions Correlation Plot**

These visualizations are designed to communicate **patterns, disparities, and relationships** in disease activity.

---

## 📁 Dataset Details (Synthetic)

The dataset simulates routine clinical encounters, including:

| Variable | Description |
|---------|-------------|
| edss | Disability level per EDSS scale |
| relapse_flag | Whether a relapse occurred at that visit |
| treatment | Current therapy at visit |
| lesion_count / lesion_volume | MRI lesion burden |
| fatigue_score / mobility_score | Symptom severity |
| ms_type | RRMS, SPMS, PPMS |
| age_at_dx | Age at diagnosis |
| visit_date | Time progression for each patient |

All data is **synthetic** and does **not represent real patients**.

---

## 🧰 What’s Included in the Repository

- **Synthetic MS dataset** (CSV)
- **SQL scripts** for structured views and basic transformations  
- **Python analysis notebooks** containing:
  - Data cleaning  
  - Progression analysis  
  - Visualization creation  
- **Tableau dashboards** illustrating key patterns  
- **Summary insights and interpretation** (this README)

---

## 🎯 Project Value (for Recruiters)

This case study highlights your ability to:

- Analyze **realistic clinical datasets**  
- Build **meaningful, insight-driven visualizations**  
- Interpret healthcare data in a business/clinical context  
- Communicate findings clearly for stakeholders  
- Demonstrate domain understanding of chronic disease progression  
- Apply SQL, Python, and BI tools to structured datasets  

---

## 📌 Recommended Extensions (Future Work)

- Patient-level forecasting (EDSS or relapse)  
- Cohort clustering for phenotype identification  
- Treatment effectiveness analysis  
- Integration into an interactive dashboard with filters  

---

## 📫 Contact

For questions or collaboration opportunities, feel free to reach out or explore my GitHub profile.

---

