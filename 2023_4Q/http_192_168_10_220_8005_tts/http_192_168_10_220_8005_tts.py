#http_192_168_10_220_8005_tts.py
import sys
sys.version
scriptPath=r'C:\python377\Lib\site-packages'
sys.path.append(scriptPath)
import maya.cmds as cmds
import requests
import numpy as np
import json 
import pymel.core as pm
import requests
import base64
import time
import os
ttsList=["주위의 자연을 살피며 새로운 경험을 즐겨보세요.",
"다양한 경험들이 나를 더 풍요롭게 만들어줍니다.",
"그 별도의 시선으로 세상을 바라보는 것이 중요합니다.",
"과거의 노력이 지금의 성공을 이끌어냈습니다.",
"일상 속에서도 소중한 순간들이 숨어있습니다.",
"여행을 떠나서 새로운 옷차림을 선보여보세요.",
"숫자 하나하나가 중요한 의미를 갖고 있습니다.",
"인생의 여정은 끝없는 학교입니다.",
"물품을 정리하는 것은 생활에서 중요한 습관입니다.",
"향기로 가득한 꽃들이 공원을 아름답게 장식하고 있습니다."]
def tts8005(strTTS,IntSpeaker,strSave):
    url = "http://192.168.10.220:8005/tts"
    payload = {"text": strTTS , "speaker": IntSpeaker, "speed": 1.0}
    response = requests.post(url, params=payload)
    with open("d:/"+strSave+".wav", "wb") as f:
        f.write(response.content)
for i in range(0,10):
    tts8005(ttsList[i],10,'TTS_benchmark_8005_010_0'+str(i))# 아나운서 남           
    tts8005(ttsList[i],20,'TTS_benchmark_8005_020_0'+str(i))# 아나운서 여 
    tts8005(ttsList[i],30,'TTS_benchmark_8005_030_0'+str(i))# 문재인 
    tts8005(ttsList[i],40,'TTS_benchmark_8005_040_0'+str(i))# 윤석열 
    tts8005(ttsList[i],50,'TTS_benchmark_8005_050_0'+str(i))# 예훈님                 
    tts8005(ttsList[i],60,'TTS_benchmark_8005_060_0'+str(i))# 대표님                     
