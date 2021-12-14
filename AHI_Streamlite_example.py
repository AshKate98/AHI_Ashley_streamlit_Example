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

st.subheader('Hospital Type')
bar1 = df_Hospital['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)

st.subheader('Pie Chart of Hospital Type')
fig = px.pie(bar1, values='hospital_type', names='index')
st.plotly_chart(fig)

st.markdown('Variable explored- Hospital type for the total number of hospitals')
st.markdown('below is a Hospital_type_def created with the Hospital_df once cleaned displaying the type of hospitals labeled as Acute, critical care, children care, department of defense, and pyschiatric hospitals.')
st.markdown('As we can answer the following question that Acute care hospitals are the most frequent hospitals, while leading into the next question!')
st.markdown('1. Acute 3256')
st.markdown('2. Critical 1355')
st.markdown('3. Pyschiatric 573')

hospitals_ny = df_Hospital[df_Hospital['state'] == 'NY']
st.subheader('Hospital Type - NY')
bar1 = hospitals_ny['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)

st.markdown('The majority of hospitals in NY are acute care, followed by psychiatric which for all states overall is different since we see critical care has the wnd most total number of hospitals')

st.header('NY Hospital type Breakdown')
st.subheader('With a PIE Chart:')
fig = px.pie(bar1, values='hospital_type', names='index')
st.plotly_chart(fig)


st.markdown('Pivot Table')

st.subheader('Hospital data Pivot Table')
dataframe_pivot = df_Hospital.pivot_table(index=['hospital_ownership','hospital_type'],values=['hospital_overall_rating'],aggfunc='count')
st.dataframe(dataframe_pivot)

st.header('Outpatient Data')
st.dataframe(df_Outpatient)

st.title('OUTPATIENT Dataframe')
st.subheader('Outpatient providers in the state of NY')
Outpatient_NY = df_Outpatient[df_Outpatient['provider_state'] == 'NY']
bar2 = Outpatient_NY['provider_name'].value_counts().reset_index()
st.dataframe(bar2)

st.subheader('Bar chart displaying different outpatient providers in NY:')
fig3 = px.bar(bar2, x='index', y='provider_name')
st.plotly_chart(fig3)

st.header('Inpatient Data')
st.dataframe(df_Inpatient)
          
