import importlib
import os
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # data web app development
import Import_questionaire_data
import information
from pathlib import Path
from util import filter_df


### import all companies
company_dict = Import_questionaire_data.execute_company_data_import(information)


###---------------------------------Sidebar---------------------------------

### select company
st.sidebar.header("Client filters")
company_selected= st.sidebar.selectbox(label = 'Select Company',
                                        options = np.asarray(list(company_dict.keys())))


### default company (when first log onto page, and haven't selected target company)
company_df = company_dict[company_selected]

### select question
questions_selected = st.sidebar.multiselect(label = 'Select Questions',
                                    options = np.asarray(company_df['Question #'].unique()))

### select role
roles_selected = st.sidebar.multiselect(label = 'Select Roles',
                                    options = np.asarray(company_df['Role'].unique()))

### select tier
tiers_selected = st.sidebar.multiselect(label = 'Select Employees by Tiers',
                                    options = np.asarray(company_df['Tier'].unique()))


### select employee
employees_selected = st.sidebar.multiselect(label = 'Select Employees',
                                    options = np.asarray(company_df['Employee ID'].unique()))

###------------------------------------Main------------------------------------

### Main
st.title("Questionaire responses")

company_df = company_dict[company_selected]

filtered_df = filter_df(company_df , questions_selected , roles_selected , tiers_selected , employees_selected)

st.dataframe(data = filtered_df)


st.sidebar.download_button(
    label = "Download CSV",
    data = filtered_df.to_csv().encode('utf-8'),
    file_name = f'{company_selected}.csv',
    mime = 'csv',
)



