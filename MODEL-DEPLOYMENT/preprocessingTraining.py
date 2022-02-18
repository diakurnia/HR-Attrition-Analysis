import streamlit as st

def app():
    
    # Title for page
    st.markdown("<h1 style='text-align: center;'>Pre-processing, Training and Evaluation Model</h1>", unsafe_allow_html=True)

    # part-2 Objective
    st.header('Pre-processing')
    st.markdown('- Feature Selection')
    st.markdown('- Scalling')
    st.markdown('- One Hot Encoding')
    st.markdown('- Handling Imbalance (SMOTE)')
    col1, col2 = st.columns([1,3])
    with col1:
        st.image("imbalance.png")
    with col2: 
        st.write("")

    # part-3 Data Understanding
    st.header('Training Model')
    st.write('- Base Model')
    st.write('- Model with Hyperparameter Tunning')
    
    # part-4 methodology 
    st.header('''Model Evaluation''')
    col1, col2 = st.columns(2)
    with col1:
        st.image("accuracy.png")
    with col2:
        st.image("precision.png")
    
    col3, col4 = st.columns(2)
    with col3:
        st.image("recall.png")
    with col4:
        st.image("f1-score.png")
    
