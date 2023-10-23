import sys
sys.version
#scriptPath=r'C:\python377\Lib\site-packages'
#sys.path.append(scriptPath)
scriptPath=r'Z:\Private_Folder\kyuseokKim\site-packages'
sys.path.append(scriptPath)
from PIL import Image, ImageDraw, ImageFont
import os
import pymel.core as pm
if pm.objExists('null1'):
    pass
else:
    pm.createNode('transform',n='null1') 
    pm.PyNode('null1.outlinerColor').set((1.0, 0.8191999793052673, 0.31369996070861816))     
    pm.PyNode('null1.useOutlinerColor').set(1)  
if pm.objExists('null2'):
    pass
else:
    pm.createNode('transform',n='null2')
    pm.PyNode('null2.outlinerColor').set((0.0,0.0,0.0))
    pm.PyNode('null2.useOutlinerColor').set(1)


#
#
#pm.createNode('transform',n='null1')
#pm.createNode('transform',n='null2')

bg_color=pm.PyNode('null1.outlinerColor').get()
tx_color=pm.PyNode('null2.outlinerColor').get()
bg_colorA=(int(bg_color[0]*255),int(bg_color[1]*255),int(bg_color[2]*255))
tx_colorA=(int(tx_color[0]*255),int(tx_color[1]*255),int(tx_color[2]*255))
#import cv2
# 이미지 크기 설정
width, height = 30, 30
background_color = bg_colorA
# 새 이미지 생성
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# 글자 추가
#font_path = os.path.join(cv2.__path__[0],'qt','fonts','DejaVuSans.ttf')
#font = ImageFont.truetype(font_path, size=128)
font_size = 15
font = ImageFont.truetype("arial.ttf", font_size)
text = "ETC"
#font = ImageFont.load_default(6)

# 글자의 크기와 위치 설정
text_bbox = draw.textbbox((0, 0), text, font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
x = (width - text_width) // 2
y = (height - text_height) // 2
text_color = tx_colorA
# 글자 쓰기
draw.text((x, y), text, fill=text_color, font=font)

# 이미지 저장
image.save("D:/study_python.png")
