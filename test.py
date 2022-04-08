# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline

# use full page width
st.set_page_config(page_title="Timeline Example", layout="wide")

# load data
# with open('example.json', "r") as f:
#     data = f.read()

data = {

    # Starting slide
    "title": {
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/pm_lee.jpg?raw=true",
            "caption": " <a target=\"_blank\" href=''>credits</a>",
            "credit": "Prime Minister's Office"
        },
        "text": {
            "headline": "Singapore's<br>COVID-19 Journey",
            "text": "<p>Through key phrases from PM Lee Hsien Loong's speeches.</p>"
        }
    },

    # Subsequent slides
    "events": [
        {
        # Slide 1
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-02-08.png?raw=true",
            "caption": "How to Use TimelineJS (<a target=\"_blank\" href='https://timeline.knightlab.com/'>credits</a>)"
        },
        "start_date": {
            "year": "2020",
            "month": "2",
            "day": "8"
        },
        "text": {
            "headline": "ABCD"
        }
        },
        {
        # Slide 2
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-03-12.png?raw=true",
            "caption": "Streamlit Components (<a target=\"_blank\" href='https://streamlit.io/'>credits</a>)"
        },
        "start_date": {
            "year": "2020",
            "month": "3",
            "day":"12"
        },
        "text": {
            "headline": "Streamlit Components<br>version 0.63.0",
            "text": "Streamlit lets you turn data scripts into sharable web apps in minutes, not weeks. It's all Python, open-source, and free! And once you've created an app you can use our free sharing platform to deploy, manage, and share your app with the world."
        }
        },
        {
        # Slide 3
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-04-03.png?raw=true",
            "caption": "github/innerdoc (<a target=\"_blank\" href='https://www.github.com/innerdoc/'>credits</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"4",
            "day": "3"
        },
        "text": {
            "headline": "Streamlit TimelineJS component",
            "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 4
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-04-10.png?raw=true",
            "caption": "github/innerdoc (<a target=\"_blank\" href='https://www.github.com/innerdoc/'>credits</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"4",
            "day": "10"
        },
        "text": {
            "headline": "Streamlit TimelineJS component",
            "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 5
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-04-21.png?raw=true",
            "caption": "github/innerdoc (<a target=\"_blank\" href='https://www.github.com/innerdoc/'>credits</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"4",
            "day": "21"
        },
        "text": {
            "headline": "Streamlit TimelineJS component",
            "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 6
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-06-07.png?raw=true",
            "caption": "github/innerdoc (<a target=\"_blank\" href='https://www.github.com/innerdoc/'>credits</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"6",
            "day": "7"
        },
        "text": {
            "headline": "Streamlit TimelineJS component",
            "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 7
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-12-14.png?raw=true",
            "caption": "github/innerdoc (<a target=\"_blank\" href='https://www.github.com/innerdoc/'>credits</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"12",
            "day": "14"
        },
        "text": {
            "headline": "Streamlit TimelineJS component",
            "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 8
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2021-05-31.png?raw=true",
            "caption": "github/innerdoc (<a target=\"_blank\" href='https://www.github.com/innerdoc/'>credits</a>)"
        },
        "start_date": {
            "year": "2021",
            "month":"5",
            "day": "31"
        },
        "text": {
            "headline": "Streamlit TimelineJS component",
            "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 9
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2021-10-09.png?raw=true",
            "caption": "github/innerdoc (<a target=\"_blank\" href='https://www.github.com/innerdoc/'>credits</a>)"
        },
        "start_date": {
            "year": "2021",
            "month":"10",
            "day": "9"
        },
        "text": {
            "headline": "Streamlit TimelineJS component",
            "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 10
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2022-03-24.png?raw=true",
            "caption": "github/innerdoc (<a target=\"_blank\" href='https://www.github.com/innerdoc/'>credits</a>)"
        },
        "start_date": {
            "year": "2022",
            "month":"3",
            "day": "24"
        },
        "text": {
            "headline": "Streamlit TimelineJS component",
            "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
    ]
    }

# print(data)

# render timeline
timeline(data, height=800)