import streamlit as st

st.set_page_config(
  page_title="All in One Basketball Predictions"
)

st.sidebar.success("Select a page above to continue...")

st.title('2022-2023 NBA Fantasy Score Predictions')

st.markdown("""
This app uses the results of a few Python scripts that scraped historic data and used it to predict this NBA season. Historical data was pulled 
from Basketball-Reference.com, including college, international, and regular season stats. After compiling everything,
the scripts ran a combination of several machine learning algorithms to estimate all of the traditional stats for each player. In addition, 
award predictions have been added based on players' expected stats and the teams' expected records.

##### Last Updated: 26 September 2022
""")
