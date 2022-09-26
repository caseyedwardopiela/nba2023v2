import streamlit as st
import pandas as pd
#import base64
#import matplotlib.pyplot as plt
import numpy as np

allstar_data = pd.read_csv('Data/raw_data_for_allstars.csv').drop(['Unnamed: 0'], axis = 1)
 
st.title('Customized All-Star Predictions')

st.markdown("""
Are you thinking these predictions might be off? Maybe you were wondering how likely your MyCareer player in NBA 2k23
is to be an All-Star. You can input your own stats here for your favorite player to see how likely he is
to make the All-Star game based on your own beliefs.
""")

st.dataframe(allstar_data)

with st.form(key ='Form1'):
    with st.sidebar:
        points_range = range(0, 50.5, 0.5)
        points = st.select_slider('Points Per Game', options = point_range, value = 15)
        assists = st.number_input('Assists Per Game', 100)
        rebounds = st.number_input('Rebounds Per Game', 100)
        steals = st.number_input('Steals Per Game', 100)
        blocks = st.number_input('Blocks Per Game', 100)
        record = st.number_input('Team Record', 100)
        submitted = st.form_submit_button(label = 'Determine All-Star Likelihood')

