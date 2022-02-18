import streamlit as st

def app():
    
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.write("")

    with col2:
        st.image('bg.jpg')

    with col3:
        st.write("")
    
    # Title for page
    st.markdown("<h1 style='text-align: center;'>HR Attrition Analysis and Prediction</h1>", unsafe_allow_html=True)

    # part-1 Problem Statement
    st.header('Problem Statement')
    st.write('''Employee attrition is defined as the natural process by which employees leave the workforce 
                — for example, through resignation for personal reasons or retirement — and are not immediately replaced.
                Attrition has always been a major concern in any organization. 
                The time, money and effort invested in training new employees, 
                and other factors leads to a massive overall loss 
                to the company when an employee leaves. 
                ''')

    # part-2 Objective
    st.header('Objective')
    st.markdown('- Get insight about factors that influence employee attrition.')
    st.markdown('- Find the best and proper model to predict employee attrition')


    # part-3 Data Understanding
    st.header('Data Understanding')
    st.write('''The dataset used to examine the trends related to Employee Attrition is a fictional data set created by IBM data scientists that can be found 
                <a href="https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset">here</a>.
                It contains of 1470 rows and 34 columns.''',unsafe_allow_html=True)
    st.write('Columns of this dataset can be categorized into four types:')
    st.write('- Personal informations')
    st.write('- Salary related informations')
    st.write('- Job related informations')
    st.write('- Employee performance and satisfaction survey')

    
    # part-4 methodology 
    st.header('''Methodology''')
    st.markdown('- Problem Statement and Identify Objective')
    st.markdown('- Data Understanding')
    st.markdown('- Data Cleaning')
    st.markdown('- Exploratory Data Analysis')
    st.markdown('- Data Pre-processing')
    st.markdown('- Training and Evaluation Model')
    st.markdown('- Model Deployment')
