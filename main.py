from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai


# get the transcript
video_url = "https://www.youtube.com/watch?v=JeVDjExBf7Y"
video_id = video_url.split("=")[1]

transcript  = YouTubeTranscriptApi.get_transcript(video_id)

text = ""
for i in transcript:
    text += i['text'] 
    text += " "

# generating the summary
API_KEY = "AIzaSyDeY5mj-bmzj3ONfXw7qf1QejjNJW6QwW4"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro-latest')

response = model.generate_content(f"Summarize the following transcript in an organized manner: {text}")
print(response.text)