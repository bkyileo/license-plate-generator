#!/usr/bin/python
# -*- coding: UTF-8 -*-
from io import BytesIO
from image import *
import PIL
import random
from PIL import Image
image = ImageCaptcha(fonts=['msyh.ttc'])

'''
# data = image.generate(u'京·AB3411')
image.write(u'l234567890', 'dig.png')
img = Image.open('dig.png')
img = img.resize((500,60))
#img = img.rotate(random.uniform(-5, 5), Image.BILINEAR, expand=1)
img.save('dig.png')

image.write(u'ABCDEFGHJKLMN', 'ch1.png')
img = Image.open('ch1.png')
img = img.resize((500,60))
#img = img.rotate(random.uniform(-5, 5), Image.BILINEAR, expand=1)
img.save('ch1.png')

image.write(u'PQRSTUVWXYZ', 'ch2.png')
img = Image.open('ch2.png')
img = img.resize((500,60))
#img = img.rotate(random.uniform(-5, 5), Image.BILINEAR, expand=1)
img.save('ch2.png')
'''
import random
from PIL import Image
from PIL import ImageFilter
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype
ch = "ABCDEFGHJKLMNPQRSTUVWXYZ"
di = "l234567890"
num = 1

def rndColor():
    return (random.randint(0, 255), random.randint(0,255), random.randint(0, 255))

for i in xrange(num):
    label = ''
    label = label + str(ch[random.randint(0,23)])
    label =label+u'·'
    for j in xrange(5):
        if(random.randint(1,4))<=3:
            label = label + str(di[random.randint(0,9)])
        else:
            label = label + str(ch[random.randint(0,23)])
    label = u'京'+label
    image.write(label, label+'.jpg')
    '''
    img = Image.open('./dataset/'+name+'.jpg')
    img = img.rotate(random.uniform(-4, 4), Image.BILINEAR, expand=1)
    width, height = img.size
    draw = Draw(img)
    for x in range(width):
        for y in range(height):
            if img.getpixel((x,y))==(0,0,0):
                draw.point((x, y), fill=rndColor())
    img = img.resize((224,224))
    print name
    img.save('./dataset/'+name+'.jpg')
    '''

