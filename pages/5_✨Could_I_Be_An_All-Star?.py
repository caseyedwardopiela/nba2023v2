import streamlit as st
import pandas as pd
#import base64
#import matplotlib.pyplot as plt
import numpy as np

allstar_data = pd.read_csv('Data/raw_data_for_allstars.csv').drop(['Unnamed: 0'], axis = 1)
 
st.title('Team Standings Predictions')

st.markdown("""
Based on player personnel and my best educated guess, expected standings for both conferences have been assigned to help in calculations
on subsequent pages.
""")

st.dataframe(allstar_data)

