# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:03:29 2021

@author: ashle
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Streamlit Final Assignment')
st.write('AshKate98 Dashboard!') 

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
  
st.header('Hospital Data Set')
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

st.markdown('The majority of hospitals in NY are acute care, followed by psychiatric which for all states overall is different since we see critical care has the 2nd most total number of hospitals')

st.header('NY Hospital type Breakdown')
st.subheader('PIE Chart:')
fig = px.pie(bar1, values='hospital_type', names='index')
st.plotly_chart(fig)

st.subheader('Hospital data Pivot Table')
dataframe_pivot = df_Hospital.pivot_table(index=['hospital_ownership','hospital_type'],values=['hospital_overall_rating'],aggfunc='count')
st.dataframe(dataframe_pivot)

st.subheader('Acute Care Hospitals in NY with 1 rating')
State_acute_1 = df_Hospital[df_Hospital['state'] == 'NY']
bar2 = State_acute_1['hospital_overall_rating'].value_counts().reset_index()
st.dataframe(bar2)

st.subheader('Bar chart displaying Acute Care Hopitals within NY with 1 rating:')
fig3 = px.bar(bar2, x='index', y='hospital_overall_rating')
st.plotly_chart(fig3)
st.markdown('Hospital Q: What are the most common hospital type in NY & what is the breakdown of acute care hospitals in NY tjat are 1 overall?')
st.markdown('Hospital A: The most common Hopsital type in NY is acute care hospitals with 144 acute care hospitals and the total number of 46 acute care hopsitals in ny have a 1 rating.')

st.header('Outpatient Data')
st.dataframe(df_Outpatient)

st.subheader('Number of Facilities by state')
bar1 = df_Outpatient['provider_state'].value_counts().reset_index()
st.dataframe(bar1)

st.subheader('Pie Chart of facilities by state')
fig = px.pie(bar1, values='provider_state', names='index')
st.plotly_chart(fig)

st.markdown('Outpatient Q: What states have the most outpatient facilities?')
st.markdown('A: From the above chart we can see that Texas has the most outpatient facilities with 2205, California 2nd with 2,113, and Pennsylvania 3rd with 1,667')
st.markdown('Lets see a comparison between NY and NC')

st.subheader('Map of NY Hospital Locations')

hospitals_ny_gps = hospitals_ny['location'].str.strip('()').str.split(' ', expand=True).rename(columns={0: 'Point', 1:'lon', 2:'lat'})  
hospitals_ny_gps['lon'] = hospitals_ny_gps['lon'].str.strip('(')
hospitals_ny_gps = hospitals_ny_gps.dropna()
hospitals_ny_gps['lon'] = pd.to_numeric(hospitals_ny_gps['lon'])
hospitals_ny_gps['lat'] = pd.to_numeric(hospitals_ny_gps['lat'])

st.map(hospitals_ny_gps)

st.subheader('Outpatient providers in the state of NY')
Outpatient_NY = df_Outpatient[df_Outpatient['provider_state'] == 'NY']
bar2 = Outpatient_NY['provider_name'].value_counts().reset_index()
st.dataframe(bar2)

st.subheader('Bar chart displaying different outpatient providers in NY:')
fig3 = px.bar(bar2, x='index', y='provider_name')
st.plotly_chart(fig3)

st.subheader('Outpatient providers in the state of North Carolina')

Outpatient_nc = df_Outpatient[df_Outpatient['provider_state'] == 'NC']

bar3 = Outpatient_nc['provider_name'].value_counts().reset_index()
st.dataframe(bar3)

st.subheader('Bar chart displaying different outpatient providers in North Carolina:')
fig3 = px.bar(bar3, x='index', y='provider_name')
st.plotly_chart(fig3)

st.header('Inpatient Data')
st.dataframe(df_Inpatient)

st.subheader('Inpatient Facility')
bar1 = df_Inpatient['provider_state'].value_counts().reset_index()
st.dataframe(bar1)

st.subheader('Pie Chart of Inpatient Facilities by state')
fig = px.pie(bar1, values='provider_state', names='index')
st.plotly_chart(fig)

st.header('Breakdown of each state with each drg definition with total payments average')
costs_condition_hospital = df_Inpatient.groupby(['provider_state', 'drg_definition'])['average_total_payments'].sum().reset_index()

st.header("Costs by Condition and Hospital - Average Total Payments")
st.dataframe(costs_condition_hospital)

st.header('The total average payments for provider State, drg definitions, and each total average payment')
st.dataframe(costs_condition_hospital)

st.markdown('Here we can see the total breakdown of each drg definition by state and average total payments')
st.markdown('Inpatient Q: What is New york states Top average drg payment?')
st.markdown('A: Here we can see that for NY NY drg_definition 003 - ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH & NECK W MAJOR had the largest total payment of $5,509,499.3400')
st.markdown('CA leads the most for total averge discharge payments for 853 - INFECTIOUS & PARASITIC DISEASES W O.R. PROCEDURE W MCC $8,380,247.9500')








