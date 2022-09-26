import streamlit as st

st.set_page_config(
  page_title="All in One Basketball Predictions"
)

st.sidebar.success("Select a page above to continue...")

st.title('2022-2023 NBA Fantasy Score Predictions')

st.markdown("""
This app pulls historical data from Basketball-Reference.com, including college, international, and regular season stats. After compiling everything,
it runs a combination of several machine learning algorithms to predict all of the traditional stats for each player this coming season. In addition, 
award predictions have been added as well based on players' expected stats.

##### Last Updated: 25 September 2022
""")
