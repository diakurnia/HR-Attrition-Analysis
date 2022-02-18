import streamlit as st
import pandas as pd
import joblib

def app():
    st.header('HR Attrition Model Deployment')

    @st.cache
    def fetch_data():
        df = pd.read_csv('attrition.csv')
        return df

    df = fetch_data()

    def user_input():
        st.markdown("<h4 style='text-align: center;'>Personal Information</h4>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            Gender  = st.selectbox('Gender', df['Gender'].unique())     
        with col2:
            MaritalStatus   = st.selectbox('MaritalStatus', df['MaritalStatus'].unique())  
        with col3:
            Education  = st.selectbox('Education', df['Education'].unique())
        with col4:
            EducationField  = st.selectbox('Education Field', df['EducationField'].unique()) 

        col5, col6 = st.columns(2)
        with col5:
            Age = st.slider('Age', 18, 70, 18)
        with col6:
            DistanceFromHome  = st.slider('Distance From Home', 1, 50, 1)  
        
        st.markdown("<h4 style='text-align: center;'>Job Related Information</h4>", unsafe_allow_html=True)
        col5, col6, col7, col18 = st.columns(4)
        with col5:
            JobRole  = st.selectbox('JobRole', df['JobRole'].unique())
        with col6:
            Department  = st.selectbox('Department', df['Department'].unique()) 
        with col7:
            BusinessTravel = st.selectbox('Business Travel', df['BusinessTravel'].unique())
        with col18:
            OverTime     = st.selectbox('OverTime', df['OverTime'].unique())

        col9, col10, col11 = st.columns(3)
        with col9:
            TotalWorkingYears     = st.slider('Total Working Years', 1, 50, 1)
        with col10:
            YearsSinceLastPromotion   = st.slider('Years Since Last Promotion', 1, 20, 1)
        with col11:
            TrainingTimesLastYear    = st.slider('TrainingTimesLastYear', 1, 20, 1)

        col8, col22 = st.columns(2)
        with col8: 
            YearsAtCompany            = st.slider('Years At Company', 1, 30, 1)
        with col22:
            NumCompaniesWorked  = st.slider('NumCompaniesWorked', 1, 20, 1)
               
        st.markdown("<h4 style='text-align: center;'>Employee Satisfaction Survey</h4>", unsafe_allow_html=True)
        col13, col14, col15 = st.columns(3)
        with col13:
            EnvironmentSatisfaction  = st.selectbox('Environment Satisfaction', df['EnvironmentSatisfaction'].unique())
        with col14:
            JobInvolvement  = st.selectbox('JobInvolvement', df['JobInvolvement'].unique())  
        with col15:
            JobSatisfaction = st.selectbox('JobSatisfaction', df['JobSatisfaction'].unique())
        
        col17, col16 = st.columns(2)
        with col17:
            RelationshipSatisfaction  = st.selectbox('RelationshipSatisfaction', df['RelationshipSatisfaction'].unique())
        with col16:
            WorkLifeBalance         = st.selectbox('WorkLifeBalance', df['WorkLifeBalance'].unique())  
        
        st.markdown("<h4 style='text-align: center;'>Salary Related Information</h4>", unsafe_allow_html=True)
        col23, col24 = st.columns(2)
        with col23:
            MonthlyIncome   = st.slider('MonthlyIncome', 100, 20000, 1000)
        with col24:
            PercentSalaryHike   = st.slider('PercentSalaryHike', 0, 100, 10)

        data = {
            'Age':Age, 
            'BusinessTravel': BusinessTravel,  
            'Department':Department, 
            'DistanceFromHome':DistanceFromHome, 
            'Education':Education,
            'EducationField':EducationField, 
            'EnvironmentSatisfaction':EnvironmentSatisfaction, 
            'Gender':Gender, 
            'JobInvolvement':JobInvolvement, 
            'JobRole':JobRole, 
            'JobSatisfaction':JobSatisfaction, 
            'MaritalStatus':MaritalStatus, 
            'MonthlyIncome':MonthlyIncome, 
            'NumCompaniesWorked':NumCompaniesWorked,
            'OverTime':OverTime, 
            'PercentSalaryHike':PercentSalaryHike,  
            'RelationshipSatisfaction':RelationshipSatisfaction, 
            'TotalWorkingYears':TotalWorkingYears, 
            'TrainingTimesLastYear':TrainingTimesLastYear, 
            'WorkLifeBalance':WorkLifeBalance, 
            'YearsAtCompany':YearsAtCompany, 
            'YearsSinceLastPromotion':YearsSinceLastPromotion, 
        }
        features = pd.DataFrame(data, index=[0])
        return features


    input_data = user_input()

    st.markdown("<h4 style='text-align: center;'>Prediction Result</h4>", unsafe_allow_html=True)
   
    load_model = joblib.load("model/model_logreg.pkl")

    prediction = load_model.predict(input_data)


    if prediction == 1:
        prediction = 'Attrition'
    else:
        prediction = 'Not Attrition'

    st.write('Based on user input, the employee is predicted: ')
    if st.button('Predict'):
        st.write(prediction)
    else:
        st.write('Waiting for input data')