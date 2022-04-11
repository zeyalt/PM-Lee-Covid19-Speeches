import streamlit as st
from streamlit_timeline import timeline

# Page configuration
st.set_page_config(initial_sidebar_state="collapsed", page_title="Singapore's COVID-19 Story", layout="wide")

# Sidebar interface
st.sidebar.image('https://github.com/zeyalt/SG-Covid19-Story/blob/master/Images/SGUnited%20Logo.png?raw=true', use_column_width=True)
st.sidebar.header("About this app")
st.sidebar.info("This app presents a timeline of Singapore's COVID-19 story, as told through key phrases extracted from PM Lee's speeches. This timeline is built with the awesome [`streamlit_timeline`](https://github.com/innerdoc/streamlit-timeline) package! :blue_heart:")
st.sidebar.header("How were key phrases extracted?")
how = """
Key phrases were extracted using the [`multi_rake`](https://github.com/vgrabovets/multi_rake) package. It implements a method known as **Rapid Automatic Keyword Extraction (RAKE)**, which uses stopwords and phrase delimiters to identify the most relevant words or phrases in a text. 
"""
st.sidebar.info(how)
st.sidebar.header('How to interpret the "phrase clouds"?')
p_clouds = """
Top 15 key phrases from each speech are shown by way of a "phrase cloud", using the [`word_cloud`](https://github.com/amueller/word_cloud) package. Phrases with higher RAKE scores have larger fonts. The variations in font colours are random. 
"""
st.sidebar.info(p_clouds)
st.sidebar.header("Connect with me")
about_me = """
Hi! My name is Zeya. This was nothing more than a side project, to explore NLP and text visualisation methods. 

**Disclaimer**: I am, in no way, affliated to the Prime Minister's Office Singapore nor the SG United initiative.

If you liked what you saw, feel free to reach out and connect with me!
"""
connect_with_me = """
[![image](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zeyalt/) 

[![image](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/zeyalt_) 

[![image](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://zeyalt.medium.com/)
"""
st.sidebar.info(about_me + connect_with_me)

# Load data in JSON format
with open('data.json', "r") as f:
    data = f.read()

# Render timeline
timeline(data, height=650)