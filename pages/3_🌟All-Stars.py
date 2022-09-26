import streamlit as st
import pandas as pd
#import base64
#import matplotlib.pyplot as plt
import numpy as np

east_stars = pd.read_csv('Data/v1_east_allstar_predictions.csv').drop(['Unnamed: 0'], axis = 1)
west_stars = pd.read_csv('Data/v1_west_allstar_predictions.csv').drop(['Unnamed: 0'], axis = 1)
 
st.title('All-Star Predictions')

st.markdown("""
Expected team record and individual stats have been used to determine each player's likelihood of making the 2023 All-Star game.
Each conference is only allowed 12 players; however, replacements can be made in case of an injury. The 20 most likely players
and their respective probabilities are shown on this page.
""")

rows = st.columns(2)
rows[0].markdown("### Western Conference")
rows[0].dataframe(west_stars)
rows[1].markdown("### Eastern Conference")
rows[1].dataframe(east_stars)
