from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_youtube_text(video_url):
    try:
        # Video ID-ni ajratib olish
        if "v=" in video_url:
            video_id = video_url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in video_url:
            video_id = video_url.split("youtu.be/")[1].split("?")[0]
        else:
            video_id = video_url

        print(f"ID aniqlandi: {video_id}") # Tekshirish uchun

        # Subtitrlarni olishga urinish
        try:
            # Avval videoda bor barcha subtitrlar ro'yxatini olamiz
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            
            # Eng yaxshi subtitrni (qo'lda yozilgan yoki avtomatik) topamiz
            transcript = transcript_list.find_transcript(['en', 'ru', 'uz', 'de'])
            data = transcript.fetch()
            
            full_text = " ".join([item['text'] for item in data])
            return full_text
            
        except:
            # Agar yuqoridagilar o'xshamasa, shunchaki birinchi duch kelganini olamiz
            data = YouTubeTranscriptApi.get_transcript(video_id)
            full_text = " ".join([item['text'] for item in data])
            return full_text

    except Exception as e:
        return f"Xatolik: {str(e)}"