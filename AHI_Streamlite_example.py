# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:03:29 2021

@author: ashle
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Streamlit Final Assingment')
st.write('Hello Everybody!') 

df_Hospital = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')



df_Outpatient = Outpatient_2015 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')

df_Inpatient = Inpatient_2015 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')

@st.cache
def load_hospitals():
    df_Hospital = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital.csv')
    return df_Hospital

@st.cache
def load_Inpatient():
    df_Inpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient.csv')
    return df_inpatient

@st.cache
def load_Outpatient():
    df_Outpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient.csv')
    return df_outpatient
  
st.header('Hospital Data')
st.dataframe(df_Hospital)

st.header('Outpatient Data')
st.dataframe(df_Outpatient)

st.header('Inpatient Data')
st.dataframe(df_Inpatient)

