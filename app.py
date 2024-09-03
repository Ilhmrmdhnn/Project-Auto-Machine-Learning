import streamlit as st
import os
import plotly.express as px
from pycaret.classification import setup, compare_models, pull, save_model, load_model
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import operator as index
from ydata_profiling import ProfileReport
from lazypredict.Supervised import LazyClassifier
from sklearn.model_selection import train_test_split
import io
import sys

# --- FUNCTION TO LOAD DATA (CACHED) ---
@st.cache_data
def load_data(uploaded_file):
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        else:
            return None, "Unsupported file format. Please upload a CSV or Excel file."
        return df, f"File '{uploaded_file.name}' uploaded and loaded successfully."
    except Exception as e:
        return None, f"An error occurred while reading the file: {e}"

# --- INITIALIZE SESSION STATE ---
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()
if 'show_data' not in st.session_state:
    st.session_state.show_data = False
if 'profile_generated' not in st.session_state:
    st.session_state.profile_generated = False
    st.session_state.profile_report = None

# --- SIDEBAR ---
with st.sidebar:
    st.image("C:/Users/ILHAM RAMADHAN/Downloads/DATA JUPY/portoo/AutoML/asset/automl.png")
    st.title("Project Auto Machine Learning")
    choice = st.radio("Navigation", ["Upload", "Profiling", "AutoML", "Download"])
    st.info("This project application helps you build and explore your data")

# --- UPLOAD ---
if choice == "Upload":
    st.title("Upload Your Dataset")
    uploaded_file = st.file_uploader("Upload Your Dataset", type=['csv', 'xlsx']) 
    if uploaded_file:
        st.session_state.df, message = load_data(uploaded_file)
        if st.session_state.df is not None:
            st.success(message)
            st.session_state.show_data = True  # Show data after upload
        else:
            st.error(message)

    if st.session_state.show_data:
        st.dataframe(st.session_state.df)

# --- PROFILING ---
if choice == "Profiling":
    st.title("Exploratory Data Analysis")
    if st.session_state.df.empty:
        st.warning("Please upload a dataset first.")
    else:
        st.subheader("Data Overview")
        st.write(st.session_state.df.describe().T)
        
        if st.button("Generate Profile Report"):
            profile_df = ProfileReport(st.session_state.df)
            st.session_state.profile_report = profile_df
            st_profile_report(st.session_state.profile_report)
        elif st.session_state.profile_report is not None:
            st_profile_report(st.session_state.profile_report)

# --- AUTOML ---
if choice == "AutoML":
    st.title("Auto Machine Learning")
    if st.session_state.df.empty:
        st.warning("Please upload a dataset and perform profiling first.")
    else:
        target = st.selectbox("Select Your Target", st.session_state.df.columns)
        if st.button("Train model"):
            setup(st.session_state.df, target=target, session_id=123)
            setup_df = pull()
            st.info("This is the ML Experiment settings")
            st.dataframe(setup_df)
            best_model = compare_models()
            compare_df = pull()
            st.info("This is the ML Model")
            st.dataframe(compare_df)
            st.write(best_model)
            save_model(best_model, 'best_model')

# --- DOWNLOAD ---
if choice == "Download": 
    st.title("Download Your Model")
    if os.path.exists('best_model.pkl'):
        with open('best_model.pkl', 'rb') as f: 
            st.download_button('Download Model', f, file_name="best_model.pkl")
    else:
        st.warning("No trained model available for download. Train a model first.")