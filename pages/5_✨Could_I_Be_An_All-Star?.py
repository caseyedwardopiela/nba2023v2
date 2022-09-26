import streamlit as st
import pandas as pd
#import base64
#import matplotlib.pyplot as plt
import numpy as np

mvps = pd.read_csv('Data/v1_mvp_predictions.csv').drop(['Unnamed: 0'], axis = 1)
dpoy = pd.read_csv('Data/v1_dpoy_predictions.csv').drop(['Unnamed: 0'], axis = 1)
roys = pd.read_csv('Data/v1_roy_predictions.csv').drop(['Unnamed: 0'], axis = 1)
 
st.title('Award Winners Predictions')

st.markdown("""
Additional models have been run to assign each player's likelihood of winning the league's Most Valuable Player (MVP), Defensive Player of the Year (DPOY),
and Rookie of the Year (ROY) awards.
""")

award_options = ['MVP', 'DPOY', 'ROY']
selected_award = st.sidebar.selectbox('For which award would you like to see the most likely players to win it?', award_options) 

if selected_award == 'MVP':
  st.dataframe(mvps)
elif selected_award == 'DPOY':
  st.dataframe(dpoy)
else:
  st.dataframe(roys)
