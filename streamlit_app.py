import streamlit as st

# Sidebar navigation
st.sidebar.title("Explore the dashboard")
selection = st.sidebar.radio(
    "Choose a section",
    ["Introduction", "Election data", "boomlive news data"]
)

#Display content based on selection
if selection == "Introduction":
    import introduction as intro
    intro.myfun()
elif selection == "Election data":
    import election as elect
    # awards.show()
elif selection == "boomlive news data":
    import boomdata as boomd
    boomd.news_api_page()
    