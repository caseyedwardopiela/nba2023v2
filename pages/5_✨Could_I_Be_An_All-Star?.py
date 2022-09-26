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
        points_range = list(np.arange(0.0, 50.5, 0.5))
        points = st.slider('Points Per Game', min_value = float(0.0), max_value = float(50.0), step = float(0.1))
        assists = st.slider('Assists Per Game', min_value = float(0.0), max_value = float(20.0), step = float(0.1))
        rebounds = st.slider('Rebounds Per Game', min_value = float(0.0), max_value = float(20.0), step = float(0.1))
        steals = st.slider('Steals Per Game', min_value = float(0.0), max_value = float(5.0), step = float(0.1))
        blocks = st.slider('Blocks Per Game', min_value = float(0.0), max_value = float(5.0), step = float(0.1))
        record = st.slider('Team Record', min_value = float(0.0), max_value = float(1), step = float(0.05))
        submitted = st.form_submit_button(label = 'Determine All-Star Likelihood')

