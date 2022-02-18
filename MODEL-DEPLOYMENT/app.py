import streamlit as st
import pandas as pd
import joblib

st.header('HR Attrition Model Deployment')

@st.cache
def fetch_data():
    df = pd.read_csv('attrition.csv')
    return df

df = fetch_data()

def user_input():
    st.write('Personal Information')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        Age = st.slider('Age', 18, 70, 18)   
    with col2:
        Gender  = st.selectbox('Gender', df['Gender'].unique())  
    with col3:
        Education  = st.selectbox('Education', df['Education'].unique())
    with col4:
        DistanceFromHome  = st.slider('Distance From Home', 1, 50, 1) 
    col20, col21, col22 = st.columns(3)
    with col20:
        EducationField  = st.selectbox('Education Field', df['EducationField'].unique())
    with col21:
        MaritalStatus   = st.selectbox('MaritalStatus', df['MaritalStatus'].unique())  
    with col22:
        NumCompaniesWorked  = st.slider('NumCompaniesWorked', 1, 20, 1)
    
    st.write('Job Related Information')
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        JobRole  = st.selectbox('JobRole', df['JobRole'].unique())
    with col6:
        Department  = st.selectbox('Department', df['Department'].unique()) 
    with col7:
        TotalWorkingYears     = st.slider('Total Working Years', 1, 50, 1)
    with col8: 
        YearsAtCompany            = st.slider('Years At Company', 1, 30, 1)
    col9, col10, col11= st.columns(3)
    with col9:
        YearsInCurrentRole        = st.slider('Years In Current Role', 1, 30, 1)
    with col10:
        YearsSinceLastPromotion   = st.slider('Years Since Last Promotion', 1, 20, 1)
    with col11:
        YearsWithCurrManager      = st.slider('Years With Current Manager', 1, 30, 1)
    col29, col30 = st.columns(2)
    with col29:
        TrainingTimesLastYear    = st.slider('TrainingTimesLastYear', 1, 20, 1)
    with col30:
        BusinessTravel = st.selectbox('Business Travel', df['BusinessTravel'].unique())
    
    st.write('Employee Satisfaction Survey')
    col13, col14, col15, col16 = st.columns(4)
    with col13:
        EnvironmentSatisfaction  = st.selectbox('Environment Satisfaction', [1,2,3,4])
    with col14:
        JobInvolvement  = st.selectbox('JobInvolvement', df['JobInvolvement'].unique())  
    with col15:
        JobSatisfaction = st.selectbox('JobSatisfaction', df['JobSatisfaction'].unique())
    with col16:
        WorkLifeBalance         = st.selectbox('WorkLifeBalance', df['WorkLifeBalance'].unique())  
    col17, col18, col19 = st.columns(3)
    with col17:
        PerformanceRating   = st.selectbox('PerformanceRating', [1,2,3,4])
    with col18:
        RelationshipSatisfaction  = st.selectbox('RelationshipSatisfaction', df['RelationshipSatisfaction'].unique())
    with col19:
        OverTime     = st.selectbox('OverTime', df['OverTime'].unique())
    
    st.write('Salary Related')
    col23, col24, col25, col26 = st.columns(4)
    with col23:
        MonthlyIncome   = st.slider('MonthlyIncome', 100, 20000, 1000)
    with col24:
        HourlyRate  = st.slider('HourlyRate', 100, 5000, 100)
    with col25:
        MonthlyRate    = st.slider('MonthlyRate', 100, 5000, 500)
    with col26:
        DailyRate = st.slider('Daily Rate', 1, 5000, 200)
    col27, col28 = st.columns(2)
    with col27:
        StockOptionLevel    = st.selectbox('StockOptionLevel', df['StockOptionLevel'].unique())
    with col28:
        PercentSalaryHike   = st.slider('PercentSalaryHike', 0, 100, 1)

    data = {
        'Age':Age, 
        'BusinessTravel': BusinessTravel, 
        'DailyRate':DailyRate, 
        'Department':Department, 
        'DistanceFromHome':DistanceFromHome, 
        'Education':Education,
        'EducationField':EducationField, 
        'EnvironmentSatisfaction':EnvironmentSatisfaction, 
        'Gender':Gender, 
        'HourlyRate':HourlyRate, 
        'JobInvolvement':JobInvolvement, 
        'JobRole':JobRole, 
        'JobSatisfaction':JobSatisfaction, 
        'MaritalStatus':MaritalStatus, 
        'MonthlyIncome':MonthlyIncome, 
        'MonthlyRate':MonthlyRate, 
        'NumCompaniesWorked':NumCompaniesWorked,
        'OverTime':OverTime, 
        'PercentSalaryHike':PercentSalaryHike, 
        'PerformanceRating':PerformanceRating, 
        'RelationshipSatisfaction':RelationshipSatisfaction, 
        'StockOptionLevel':StockOptionLevel,
        'TotalWorkingYears':TotalWorkingYears, 
        'TrainingTimesLastYear':TrainingTimesLastYear, 
        'WorkLifeBalance':WorkLifeBalance, 
        'YearsAtCompany':YearsAtCompany, 
        'YearsInCurrentRole':YearsInCurrentRole,
        'YearsSinceLastPromotion':YearsSinceLastPromotion, 
        'YearsWithCurrManager':YearsWithCurrManager
    }
    features = pd.DataFrame(data, index=[0])
    return features


input_data = user_input()

st.subheader('User Input')
# st.write(input_data)

load_scaling = joblib.load("model/model_preparation.pkl")
load_model = joblib.load("model/model_algo.pkl")

scaled_input = load_scaling.transform(input_data)
prediction = load_model.predict(scaled_input)


if prediction == 1:
    prediction = 'Attrition'
else:
    prediction = 'Not Attrition'

st.write('Based on user input, the employee model predicted: ')
if st.button('Predict'):
     st.write(prediction)
else:
     st.write('Waiting for prediction')