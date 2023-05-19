#넘파이파일 프레임 카운트 하는 방법

import numpy as np        
import os

npyPath = r"D:\Justin\Audio2Face\Postman\TTS_Voice_001.txt"
with open(npyPath, 'r') as f:
    content = f.readlines()

content = np.array(content)


print(content.shape)
#(frame_count, 259)
# fCount = npy.shape[0]
# chanCount = npy.shape[1]

# print(fCount, chanCount)

# SetTimeLineEnd(fCount)