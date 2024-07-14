from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import streamlit as st
import os
API_KEY = st.secrets["APIKEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')


def fetch_transcript(link):
    # get the transcript
    video_id = link.split("=")[1]
    transcript  = YouTubeTranscriptApi.get_transcript(video_id)

    text = ""
    for i in transcript:
        text += i['text'] 
        text += " "

    return text

def summary(text):
    # generating the summary
    response = model.generate_content(f"Summarize the following transcript in an bullets short and crisp, do not mention advertisements: {text}")
    return response.text



st.title('Youtube Video Summariser 2024')

title = st.text_input("Enter video link")
    

if st.button("summary"):
    st.video(title)
    text = fetch_transcript(title)
    oui = summary(text)
    st.write("Summary of the video: ", oui)
 

