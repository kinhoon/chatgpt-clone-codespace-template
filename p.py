from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages = [
        # system role is the AI, user role is what you want to ask
        {"role": "system", "content": "You are an advertising expert in Ogilvy"},
        {"role": "user", "content": "Please write an 30 seconds TV advertisement script for selling satay."},
        {"role": "system", "content": "You are an insurance agent"},
        {"role": "user", "content": "Please explain to me the different types of insurance."},
    ],
    stream = True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")