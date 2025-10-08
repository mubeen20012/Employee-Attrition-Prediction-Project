# ---------------------------------
# Employee Attrition Prediction App
# ---------------------------------
import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load("employee_attrition.pk1")

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("👨‍💼 Employee Attrition Prediction Dashboard")
st.markdown("Enter employee details to predict if they are likely to **Stay** or **Leave**.")

# -----------------------------
# User Inputs
# -----------------------------
age = st.number_input("Age", min_value=18, max_value=65, value=30)
daily_rate = st.number_input("Daily Rate", min_value=100, max_value=1500, value=500)
distance = st.number_input("Distance From Home (km)", min_value=0, max_value=50, value=5)
education = st.selectbox("Education", [1, 2, 3, 4, 5])
gender = st.selectbox("Gender", ["Male", "Female"])
hourly_rate = st.number_input("Hourly Rate", min_value=10, max_value=100, value=50)
job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=20000, value=5000)
monthly_rate = st.number_input("Monthly Rate", min_value=1000, max_value=30000, value=10000)
num_companies = st.number_input("Num Companies Worked", min_value=0, max_value=20, value=2)
overtime = st.selectbox("OverTime", ["Yes", "No"])
percent_hike = st.slider("Percent Salary Hike (%)", 5, 25, 15)
performance = st.selectbox("Performance Rating", [1, 2, 3, 4])
stock = st.selectbox("Stock Option Level", [0, 1, 2, 3])
total_years = st.number_input("Total Working Years", min_value=0, max_value=40, value=5)
training = st.number_input("Training Times Last Year", min_value=0, max_value=10, value=2)
worklife = st.selectbox("WorkLife Balance", [1, 2, 3, 4])
years_company = st.number_input("Years at Company", min_value=0, max_value=40, value=5)
years_role = st.number_input("Years in Current Role", min_value=0, max_value=20, value=3)
years_promo = st.number_input("Years Since Last Promotion", min_value=0, max_value=20, value=1)
years_mgr = st.number_input("Years With Current Manager", min_value=0, max_value=20, value=2)

# Dummies (BusinessTravel, Department, EducationField, MaritalStatus, JobRole)
business_travel = st.selectbox("Business Travel", ["Travel_Frequently", "Travel_Rarely", "Non-Travel"])
dept = st.selectbox("Department", ["Research & Development", "Sales", "HR"])
edu_field = st.selectbox("Education Field", ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Other"])
marital = st.selectbox("Marital Status", ["Married", "Single", "Divorced"])
job_role = st.selectbox("Job Role", [
    "Human Resources", "Laboratory Technician", "Manager",
    "Manufacturing Director", "Research Director", "Research Scientist",
    "Sales Executive", "Sales Representative"
])

# Engineered Features
satisfaction = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
years_ratio = st.slider("Years at Company Ratio", 0.0, 1.0, 0.5)
promotion_ratio = st.slider("Promotion Years Ratio", 0.0, 1.0, 0.2)
long_commute = st.selectbox("Long Commute (1=Yes, 0=No)", [0, 1])
is_senior = st.selectbox("Is Senior (1=Yes, 0=No)", [0, 1])

# -----------------------------
# Build input DataFrame
# -----------------------------
input_data = pd.DataFrame({
    "Age": [age],
    "DailyRate": [daily_rate],
    "DistanceFromHome": [distance],
    "Education": [education],
    "Gender": [1 if gender == "Male" else 0],
    "HourlyRate": [hourly_rate],
    "JobLevel": [job_level],
    "MonthlyIncome": [monthly_income],
    "MonthlyRate": [monthly_rate],
    "NumCompaniesWorked": [num_companies],
    "OverTime": [1 if overtime == "Yes" else 0],
    "PercentSalaryHike": [percent_hike],
    "PerformanceRating": [performance],
    "StockOptionLevel": [stock],
    "TotalWorkingYears": [total_years],
    "TrainingTimesLastYear": [training],
    "WorkLifeBalance": [worklife],
    "YearsAtCompany": [years_company],
    "YearsInCurrentRole": [years_role],
    "YearsSinceLastPromotion": [years_promo],
    "YearsWithCurrManager": [years_mgr],
    "BusinessTravel_Travel_Frequently": [1 if business_travel == "Travel_Frequently" else 0],
    "BusinessTravel_Travel_Rarely": [1 if business_travel == "Travel_Rarely" else 0],
    "Department_Research & Development": [1 if dept == "Research & Development" else 0],
    "Department_Sales": [1 if dept == "Sales" else 0],
    "EducationField_Life Sciences": [1 if edu_field == "Life Sciences" else 0],
    "EducationField_Marketing": [1 if edu_field == "Marketing" else 0],
    "EducationField_Medical": [1 if edu_field == "Medical" else 0],
    "EducationField_Other": [1 if edu_field == "Other" else 0],
    "EducationField_Technical Degree": [1 if edu_field == "Technical Degree" else 0],
    "MaritalStatus_Married": [1 if marital == "Married" else 0],
    "MaritalStatus_Single": [1 if marital == "Single" else 0],
    "JobRole_Human Resources": [1 if job_role == "Human Resources" else 0],
    "JobRole_Laboratory Technician": [1 if job_role == "Laboratory Technician" else 0],
    "JobRole_Manager": [1 if job_role == "Manager" else 0],
    "JobRole_Manufacturing Director": [1 if job_role == "Manufacturing Director" else 0],
    "JobRole_Research Director": [1 if job_role == "Research Director" else 0],
    "JobRole_Research Scientist": [1 if job_role == "Research Scientist" else 0],
    "JobRole_Sales Executive": [1 if job_role == "Sales Executive" else 0],
    "JobRole_Sales Representative": [1 if job_role == "Sales Representative" else 0],
    "SatisfactionLevel": [satisfaction],
    "YearsAtCompanyRatio": [years_ratio],
    "PromotionYearsRatio": [promotion_ratio],
    "LongCommute": [long_commute],
    "IsSenior": [is_senior]
})

# -----------------------------
# Predict button
# -----------------------------
if st.button("Predict Attrition"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ This employee is likely to **Leave**.")
    else:
        st.success("✅ This employee is likely to **Stay**.")
