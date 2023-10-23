# from PIL import Image pip install pillow
import sys
sys.version
scriptPath=r'C:\python377\Lib\site-packages'
sys.path.append(scriptPath)

from PIL import Image
import pymel.core as pm

#pm.createNode('transform',n='null1')
color=pm.PyNode('null1.outlinerColor').get()
# 이미지 크기 설정 (가로 1픽셀, 세로 1픽셀)
width, height = 30, 30
colorA=(int(color[0]*255),int(color[1]*255),int(color[2]*255))
image = Image.new("RGB", (width, height), colorA)
# 이미지 저장
image.save("d:/color"+str(colorA[0])+'_'+str(colorA[1])+'_'+str(colorA[2])+".png")
