# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:03:29 2021

@author: ashle
"""
!pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
!pip install matplotlib
import matplotlib.pyplot as plt

st.title('Hospital Data')

df_Hospital = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')
df_Outpatient = Outpatient_2015 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
df_Inpatient = Inpatient_2015 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')

