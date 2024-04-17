# 텍스트르 음성으로 변환하느 라이브러리
# gtts
# TTS : Text to Speach
# STT : Speach to Text
# pip install gtts
from gtts import gTTS
import os

# 텍스트를 음성으로 변환
text = "집에 갈 시간입니다."
tts = gTTS(text=text, lang='ko')

# 음성mp3 파일 저장
tts.save('test.mp3')

# mp3 재생
os.system("test.mp3")