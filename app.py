import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from generate_gemini_content import generate_gemini_content
from extract_transcript_details import extract_transcript_details
from prompt import prompt

load_dotenv()
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)




