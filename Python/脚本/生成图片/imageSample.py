import os
from PIL import Image,ImageDraw,ImageFont

def imgleSam(num):
    for i in range(1,num+1):

        # 生成图片
        newimg = Image.new('RGB',(595,842),color=(0,255,0))

        # 添加文字
        font = ImageFont.truetype('C:/windows/fonts/SFMono-Regular-10.otf',32)
        drawimg = ImageDraw.Draw(newimg)
        drawimg.text((200,420),f'TestFile{i}',font=font,fill=(0,0,0))

        # 保存图片
        newimg.save(f'测试文件{i}.png')

imgleSam(9)