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

