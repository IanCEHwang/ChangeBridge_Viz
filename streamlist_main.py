import importlib

import os
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import Import_questionaire_data
import information
from pathlib import Path




### import all companies
company_dict = Import_questionaire_data.execute_company_data_import(information)


###---------------------------------Sidebar---------------------------------

### select company
st.sidebar.header("Customer filters")
company_selected= st.sidebar.selectbox(label = 'Select Company',
                                        options = np.asarray(list(company_dict.keys())))


company_df = company_dict[company_selected]
### select question


### select employee
employees_selected = st.sidebar.multiselect(label = 'Select Employees',
                                    options = np.asarray(company_df['Employee ID'].unique()))


def filter_df(df, employee_selected_list):
    ### if already select company
    if len(employee_selected_list) != 0:
        return df[df['Employee ID'].isin(employee_selected_list)]
    else:
        ### if no selection yet
        return  df

###------------------------------------Main------------------------------------

### Main
st.title("Questionaire responses")

company_df = company_dict[company_selected]

filtered_df = filter_df(company_df , employees_selected)

st.dataframe(data = filtered_df)


