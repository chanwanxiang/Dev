from PIL import Image,ImageDraw,ImageFont

# 生成图片以及写入文字
def newImage(width, height, num, color=(100, 100, 100, 255)):
    for i in range(1,num+1):
        newimg = Image.new('RGB', (int(width), int(height)), color)
        drawImage(newimg, i)

        newimg.save(f'测试文件{i}.jpg')

# 写入文字
def drawImage(newimg, text):
    text = str(text)
    draw = ImageDraw.Draw(newimg)

    fontSize = 100
    # 返回写入文字区域高度宽度
    font = ImageFont.truetype('arial.ttf', fontSize)
    fontArea = font.getsize(text)

    imgsize = newimg.size
    x = (imgsize[0] - fontArea[0])/2
    y = (imgsize[1] - fontArea[1])/2
    draw.text((x,y), text, font=font, fill=(255, 0, 0))

if '__main__' == __name__:
    newImage(764, 494, 9)