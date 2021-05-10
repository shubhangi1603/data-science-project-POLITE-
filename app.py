import nltk
#nltk.download('popular')
from textblob import TextBlob
import streamlit as st
import pandas as pd
from streamlit.elements.image import _format_from_image_type



st.title("Sentiment Analysis For Tweets ")
st.image('NLP.jpg')
st.header("")

sidebar=st.sidebar
sidebar.header("Choose Your Option")
choices=["Select OPtion","Enter a sentence to analyze ","Enter username to analyse tweet sentiments"]
selOpt = sidebar.selectbox("Choose what to do", choices)


def userInput():
    with st.spinner("Loading View... "):
        user_input = st.text_input("Enter the sentence you want to analyze")
    
        if user_input != '':
            test1 = TextBlob(user_input)
            st.write(format(test1.sentiment))

if selOpt == choices[1]:
    userInput()