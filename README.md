# SmartAppraise AI  
### Predictive Employee Performance Appraisal using SMART KPI & Non-Linear Machine Learning


## 📌 Project Overview
Traditional employee performance appraisals rely heavily on subjective judgement, leading to inconsistencies and bias. Organizations introduced SMART KPI frameworks to standardize evaluation; however, SMART data often contains weak correlations and complex non-linear relationships that are difficult to interpret using conventional statistical methods.

**SmartAppraise AI** addresses this challenge by integrating non-linear machine learning with a web-based analytics dashboard to objectively predict employee performance classes based on SMART KPI data. The system provides HR departments with a one-stop platform for fair, transparent, and data-driven appraisal.


## 🎯 Objectives
- Eliminate subjectivity in performance appraisal  
- Utilize SMART KPI metrics as predictive variables  
- Capture non-linear relationships using XGBoost  
- Provide interpretable dashboards for HR decision-making  
- Enable automated performance prediction through FastAPI  


## 🧠 Machine Learning Approach
| Component | Description |
|----------|-------------|
| Model | XGBoost Multi-Class Classifier |
| Objective Function | Softmax |
| Classes | Low, Below Average, Average, Above Average, High |
| Feature Type | SMART KPI indicators |
| Validation | Stratified Cross-Validation |
| Evaluation | Accuracy, Precision, Recall, F1, ROC-AUC |


## 🔁 ML Pipeline Flow
| Pipeline | Purpose |
|----------|---------|
| A | Raw Data Cleaning & Missing Handling |
| B | Outlier Detection & Normalization |
| C | Feature Engineering (Salary/Hour, Attendance Rate) |
| D | SMART KPI Variable Selection (Fair Predictors) |
| E | Hyperparameter Optimization (XGBoost) |


## 🌐 System Architecture
SmartAppraise AI integrates analytics and web technologies:
- SMART KPI Dataset → Data Preprocessing → XGBoost Model
- ↓
- FastAPI Backend
- ↓
- Interactive Dashboard


## 📊 Dashboard Features
- Employee performance distribution  
- Department-level analytics  
- Prediction confidence visualization  
- Filtering & downloadable results  
- Real-time API-based prediction updates  


## 🛠 Tech Stack
**Machine Learning**
- Python  
- XGBoost  
- Scikit-learn  
- Pandas / NumPy  

**Backend**
- FastAPI  
- Uvicorn  

**Frontend & Dashboard**
- Plotly Dash  
- HTML / CSS / JavaScript  


## 📈 Model Performance (Pipeline E)
- Accuracy: **94.25%**  
- Multi-Class ROC-AUC: ~**0.99 avg**  
- Strong separation across all 5 performance classes  
- Stable training with minimal overfitting  


## 🌱 ESG Impact
| Aspect | Contribution |
|--------|--------------|
| Environmental | Reduces inefficient workforce planning |
| Social | Ensures fair and bias-free evaluation |
| Governance | Transparent KPI-based decision system |


## 🚀 Key Contribution
SmartAppraise AI bridges the gap between SMART KPI frameworks and advanced non-linear analytics by transforming scattered performance indicators into an intelligent prediction and visualization platform for HR.
