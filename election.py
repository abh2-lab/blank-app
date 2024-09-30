import streamlit as st
import requests
import pandas as pd

# Define the API endpoint
# api_url = "https://script.google.com/macros/s/AKfycbyyiBp9D0kQHoV1uVXJKtryaOMUCYvgXSNk33G3IxAKOb_jXL6JfCNq-witRPmssLHD/exec"


df = pd.DataFrame({
    'Column B': [4, 3, 2, 1],
    'Column A': ['sund', 'mond', 'tue', 'wed']
})

# Plot the DataFrame
st.line_chart(df)
