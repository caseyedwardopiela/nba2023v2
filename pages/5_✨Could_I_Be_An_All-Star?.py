import streamlit as st
import pandas as pd
#import base64
#import matplotlib.pyplot as plt

# https://www.youtube.com/watch?v=nF-PQj0k5-o&ab_channel=PythonTutorialsforDigitalHumanities
import numpy as np

import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

allstar_data = pd.read_csv('Data/raw_data_for_allstars.csv').drop(['Unnamed: 0'], axis = 1)
 
st.title('Customized All-Star Predictions')

st.markdown("""
Are you thinking these predictions might be off? Maybe you were wondering how likely your MyCareer player in NBA 2k23
is to be an All-Star. You can input your own stats here for your favorite player to see how likely he is
to make the All-Star game based on your own beliefs.
""")

# User Input
with st.form(key ='Form1'):
    with st.sidebar:
        points = st.slider('Points Per Game', min_value = float(0.0), max_value = float(50.0), step = float(0.1))
        rebounds = st.slider('Rebounds Per Game', min_value = float(0.0), max_value = float(20.0), step = float(0.1))
        assists = st.slider('Assists Per Game', min_value = float(0.0), max_value = float(20.0), step = float(0.1))     
        steals = st.slider('Steals Per Game', min_value = float(0.0), max_value = float(5.0), step = float(0.1))
        blocks = st.slider('Blocks Per Game', min_value = float(0.0), max_value = float(5.0), step = float(0.1))
        record = st.slider('Team Record', min_value = float(0.0), max_value = float(1), step = float(0.05))
        submitted = st.form_submit_button(label = 'Determine All-Star Likelihood')


# Modeling

# Separate Data
training = allstar_data[allstar_data['Season'] < 2023]

# Determine which columns to use
training_columns = list(training.columns)[3:9]
output_column = 'Allstar'

# Run Models
y = list(training[output_column])
x = training.loc[:,training_columns]

df_temp = pd.DataFrame({'Points': [points], 'Rebounds': [rebounds], 'Assists': [assists], 'Steals': [steals], 'Blocks': [blocks], 'Record': [record]})

# Random Forest
rf_allstar = RandomForestClassifier()

rf_allstar.fit(x, y)

rf_allstar_results = rf_allstar.predict_proba(df_temp)
rf_allstar_results = [i[1] for i in rf_allstar_results]

# XGBoost
xgb_allstar = xgb.XGBClassifier()

xgb_allstar.fit(x, y)

xgb_allstar_results = xgb_allstar.predict_proba(df_temp)
xgb_allstar_results = [i[1] for i in xgb_allstar_results]

# Logistic
logistic_allstar = LogisticRegression()

logistic_allstar.fit(x, y)

logistic_allstar_results = logistic_allstar.predict_proba(df_temp)
logistic_allstar_results = [i[1] for i in logistic_allstar_results]

allstar_prediction = round((rf_allstar_results + xgb_allstar_results + logistic_allstar_results) / 3, 3)

st.write('The likelihood of your player making the NBA All-Star Game Roster is: ', allstar_prediction)

