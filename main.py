from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Create prompt template for generating ig_engagements

ig_engagement_template = "Calculate my instagram engagement rate. Given number of likes are {n1}, comments are {n2}, saves are {n3}, shares are {n4} and number of followers are {n5}. Use the method where take into consideration likes, comments, saves, shares and number of followers with equal weightage."

ig_engagement_prompt = PromptTemplate(template = ig_engagement_template, input_variables = ['n1', 'n2','n3','n4','n5'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")


# Create LLM chain using the prompt template and model
ig_engagement_chain = ig_engagement_prompt | gemini_model


import streamlit as st

st.header("Your IG Engagement Calculator")

st.subheader("Calculate your engagement rates and know your value as a UGC creator")

followers = st.number_input("Number of Followers", min_value = 1, max_value = 1000000000, value = 1, step = 1)
likes = st.number_input("Number of Likes", min_value = 1, max_value = 1000000000, value = 1, step = 1)
comments = st.number_input("Number of Comments", min_value = 1, max_value = 1000000000, value = 1, step = 1)
saves = st.number_input("Number of Saves", min_value = 1, max_value = 1000000000, value = 1, step = 1)
shares = st.number_input("Number of Shares", min_value = 1, max_value = 1000000000, value = 1, step = 1)


if st.button("Calculate"):
    ig_engagements = ig_engagement_chain.invoke({"n1" : likes, "n2" : comments, "n3" : saves, "n4" : shares, "n5" : followers})
    st.write(ig_engagements.content)
    
