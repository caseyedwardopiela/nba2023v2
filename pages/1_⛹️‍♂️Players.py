import streamlit as st
import pandas as pd
#import base64
#import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Data/v1_2023_player_predictions.csv').drop(['Unnamed: 0'], axis = 1).sort_values('Yahoo', ascending = False)
 
st.title('Individual Player Stat Predictions')

st.markdown("""
Three classes of algorithms are used to predict traditional stats and related percentages. Assigned class is dependent on whether a player is a 
rookie, second year player, or multi-year veteran. 

""")

st.sidebar.header('User Selection')

# Sidebar - Name Selection
sorted_players_unique = list(df['Name'].unique())
sorted_players_unique = sorted(sorted_players_unique)
sorted_players_unique.insert(0,'All Players')
selected_player = st.sidebar.selectbox('Which player would you like to see?',
    sorted_players_unique) 

# Sidebar - Team Selection
sorted_team_unique = list(df['Team'].unique())
sorted_team_unique = sorted(sorted_team_unique)
sorted_team_unique.insert(0,'All Teams')
selected_team = st.sidebar.selectbox('Which team would you like to see?',
    sorted_team_unique)

# Sidebar - Position Selection
sorted_position_unique = list(df['Position'].unique())
sorted_position_unique = sorted(sorted_position_unique)
sorted_position_unique.insert(0,'All Positions')
selected_position = st.sidebar.selectbox('Which position would you like to see?',
    sorted_position_unique) 

# Sidebar - Position Selection
sorted_stat_unique = list(df.columns)[3:]
sorted_stat_unique.insert(0,'All Stats')
selected_stat = st.sidebar.selectbox('Which stat would you like to see?',
    sorted_stat_unique) 

# Filtering data - Name
if selected_player == 'All Players':
    df_selected = df
else:
   selected_team = 'All Teams'
   selected_position = 'All Positions'
   df_selected = df[df['Name'] == selected_player]

# Filtering data - Team
if selected_team == 'All Teams':
    df_selected = df_selected
else:
    df_selected = df_selected[df_selected['Team'] == selected_team]
  
# Filtering data - Position
if selected_position == 'All Positions':
    df_selected = df_selected
else:
    df_selected = df_selected[df_selected['Position'] == selected_position]
  
# Filtering data - Stat
if selected_stat == 'All Stats':
    df_selected = df_selected
else:
    stats_list = ['Name', 'Team', 'Position', selected_stat]
    df_selected = df_selected.loc[:,stats_list].sort_values(selected_stat, ascending = False)


st.header('Displaying Player(s)...')
st.write('Data Dimension: ' + str(df_selected.shape[0]) + ' rows and ' + str(df_selected.shape[1]) + ' columns.')
st.dataframe(df_selected)
