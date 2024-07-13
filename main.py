from youtube_transcript_api import YouTubeTranscriptApi

video_url = "https://www.youtube.com/watch?v=JeVDjExBf7Y"
video_id = video_url.split("=")[1]

transcript  = YouTubeTranscriptApi.get_transcript(video_id)


print(transcript)