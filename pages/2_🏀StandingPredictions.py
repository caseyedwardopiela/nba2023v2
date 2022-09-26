import streamlit as st
import pandas as pd
#import base64
#import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Data/v1_2023_player_predictions.csv').drop(['Unnamed: 0'], axis = 1).sort_values('Fantasy Score', ascending = False)
 
st.title('Team Standings Predictions')

st.markdown("""
Based on player personnel and my best educated guess, expected standings for both conferences have been assigned to help in calculations
on subsequent pages.
""")
