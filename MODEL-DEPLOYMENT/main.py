import prediction, projectOverview, insight, preprocessingTraining
import streamlit as st

PAGES = {
    'Project Overview': projectOverview,
    'Insight': insight,
    'Pre-processing and Training Model': preprocessingTraining,
    'Prediction': prediction
}

st.set_page_config(page_title="HR Attrition Analysis and Prediction", layout="wide")

select_page = st.sidebar.radio('Outline', list(PAGES.keys())) 
page = PAGES[select_page]
page.app()
