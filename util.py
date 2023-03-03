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


def filter_df(df, questions_selected_list , roles_selected_list , tiers_selected_list , employee_selected_list):
    filtered_df = df
    ### if already select company
    if len(employee_selected_list) != 0:
        filtered_df = filtered_df[filtered_df['Employee ID'].isin(employee_selected_list)]
    ### if already select question
    if len(questions_selected_list) != 0:
        filtered_df = filtered_df[filtered_df['Question #'].isin(questions_selected_list)]
    ### if already select role
    if len(roles_selected_list) != 0:
        filtered_df = filtered_df[filtered_df['Role'].isin(roles_selected_list)]
    ### if already select tier
    if len(tiers_selected_list) != 0:
        filtered_df = filtered_df[filtered_df['Tier'].isin(tiers_selected_list)]
    else:
        ### if no selection yet
        return  filtered_df
    return filtered_df


