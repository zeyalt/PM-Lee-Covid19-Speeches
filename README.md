# Singapore's COVID-19 Story

[Link to app](https://share.streamlit.io/zeyalt/sg-covid19-story/app.py)

## About this app

This app presents a timeline of Singapore's COVID-19 story, as told through key phrases extracted from PM Lee's speeches. This timeline is built with the awesome [`streamlit_timeline`](https://github.com/innerdoc/streamlit-timeline) package! :blue_heart:

## How were key phrases extracted?

Key phrases were extracted using the [`multi_rake`](https://github.com/vgrabovets/multi_rake) package. It implements a method known as **Rapid Automatic Keyword Extraction (RAKE)**, which uses stopwords and phrase delimiters to identify the most relevant words or phrases in a text. 

## How to interpret the "phrase clouds"?

Top 15 key phrases from each speech are shown by way of a "phrase cloud", using the [`word_cloud`](https://github.com/amueller/word_cloud) package. Phrases with higher RAKE scores have larger fonts. The variations in font colours are random. 

## Connect with me
Hi! My name is Zeya. This was nothing more than a side project, to explore NLP and text visualisation methods. 

**Disclaimer**: I am, in no way, affliated to the Prime Minister's Office Singapore nor the SG United initiative.

If you liked what you saw, feel free to reach out and connect with me!

[![image](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zeyalt/) 

[![image](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/zeyalt_) 

[![image](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://zeyalt.medium.com/)