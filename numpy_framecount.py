#넘파이파일 프레임 카운트 하는 방법

import numpy as np        
import os

npyPath = os.path.join("C:\\Users\\vivestudios\\Downloads\\" , "bs_value_1114_2_01.npy")
npy = np.load(npyPath)
print(npy.shape)
#(frame_count, 259)
fCount = npy.shape[0]
chanCount = npy.shape[1]

print(fCount, chanCount)

# SetTimeLineEnd(fCount)