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
            # "caption": " <a target=\"_blank\" href=''>credits</a>",
            "credit": "Source: Prime Minister's Office"
        },
        "text": {
            "headline": "Singapore's<br>COVID-19 Journey",
            "text": "Since COVID-19 struck Singapore in January 2020,<br>PM Lee has addressed the nation several times. Each<br>speech reflected the state of the pandemic as well as<br>measures taken by the Singapore Government. This<br>timeline summarises the journey using key phrases from<br>PM Lee's speeches."
        }
    },

    # Subsequent slides
    "events": [
        {
        # Slide 1
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-02-08.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-on-the-Novel-Coronavirus-nCoV-Situation-in-Singapore-on-8-February-2020'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month": "2",
            "day": "8",
            # "display_date": "HH-MM-YYYY"
        },
        "text": {
            "headline": "The Beginning", 
            "text": " "
        }
        },
        {
        # Slide 2
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-03-12.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-remarks-COVID-19-Outbreak-12-Mar-2020'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month": "3",
            "day":"12"
        },
        "text": {
            # "headline": "Streamlit Components<br>version 0.63.0",
            # "text": "Streamlit lets you turn data scripts into sharable web apps in minutes, not weeks. It's all Python, open-source, and free! And once you've created an app you can use our free sharing platform to deploy, manage, and share your app with the world."
        }
        },
        {
        # Slide 3
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-04-03.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-on-the-COVID19-situation-in-Singapore-on-3-April-2020'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"4",
            "day": "3"
        },
        "text": {
            # "headline": "Streamlit TimelineJS component",
            # "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 4
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-04-10.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-on-the-COVID-19-situation-in-Singapore-on-10-April-2020'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"4",
            "day": "10"
        },
        "text": {
            # "headline": "Streamlit TimelineJS component",
            # "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 5
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-04-21.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-address-COVID-19-21-Apr'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"4",
            "day": "21"
        },
        "text": {
            # "headline": "Streamlit TimelineJS component",
            # "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 6
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-06-07.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/National-Broadcast-PM-Lee-Hsien-Loong-COVID-19'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"6",
            "day": "7"
        },
        # "media": {
        #     "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/after_circuit_breaker.jpg?raw=true",
        #     "caption": "from ST, after CB"
        # },
        "text": {
            # "headline": "Streamlit TimelineJS component",
            # "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 7
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-12-14.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-on-the-COVID-19-situation-in-Singapore-on-14-December-2020'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"12",
            "day": "14"
        },
        "text": {
            # "headline": "Streamlit TimelineJS component",
            # "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 8
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2021-05-31.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-COVID-19-New-Normal-31-May-2021'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2021",
            "month":"5",
            "day": "31"
        },
        "text": {
            "headline": "The New Normal",
            # "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
        {
        # Slide 9
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2021-10-09.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/Update-on-the-COVID-19-Situation-In-Singapore-by-Prime-Minister-Lee-Hsien-Loong-on-9-October'>Link to speech</a>)"
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
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-on-COVID-19-A-New-Phase-on-24-Mar-2022'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2022",
            "month":"3",
            "day": "24"
        },
        "text": {
            # "headline": "Streamlit TimelineJS component",
            # "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it."
        }
        },
    ]
    }

# print(data)

# render timeline
timeline(data, height=800)