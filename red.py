# # https://blog.csdn.net/weixin_45903952/article/details/104865694


# from PIL import Image
# from PIL import ImageChops 
# #from PIL import ImageEnhance

# def compare_images(path_one, path_two, diff_save_location):

#     image_one = Image.open(path_one)
#     image_two = Image.open(path_two)

#     diff = ImageChops.difference(image_one, image_two)
#     #diff.show()            #不同的点图
#     r,g,b=diff.split()      #RGB分离
#     invertr=ImageChops.invert(r)    #红色反向
#     img1=invertr.convert('1')       #转成黑白图，黑点即红点
    
#     img = img1.convert("RGBA")    # 转换格式，确保像素包含alpha通道
#     width, height = img.size     # 长度和宽度
#     for i in range(0,width):     # 遍历所有长度的点
#         for j in range(0,height):       # 遍历所有宽度的点
#             data = img.getpixel((i,j))  # 获取一个像素
#             if (data.count(255) == 4):  # RGBA都是255，改成透明色
#                 img.putpixel((i,j),(255,255,255,0))
#             else:
#                 #if img.getpixel((i,j))[0]>200:
#                 img.putpixel((i,j),(255,0,0,255))
#                 img.paste((255,0,0,255),(i-4,j-4,i,j))  #放大红点范围
#     img=img.convert("RGB")
#     image_one_l=image_one.convert("L")      #转化为灰度
#     image_one=image_one_l.convert("RGB")    #再把灰度图像转为RGB
#     #r,g,b=image_one.split()#     # if diff.getbbox() is None:
# #     # # 图片间没有任何不同则直接退出
# #     #     print("【+】We are the same!")
# #     # else:
# #     #     diff.save(diff_save_location)

#     r,g,b=img.split()
#     image=Image.composite(image_one,img,g)
#     # image.show()
#     image.save("最终_"+diff_save_location)

 

#     # if diff.getbbox() is None:
#     # # 图片间没有任何不同则直接退出
#     #     print("【+】We are the same!")
#     # else:
#     #     diff.save(diff_save_location)


 
# if __name__ == '__main__':
#     compare_images('/home/jl/gif/blur/8.jpg',
#                    '/home/jl/gif/resized/8.jpg',
#                    '我们不一样.png')


###############################################################################################

import cv2
import numpy as np
import imageio
import time
from PIL import Image
from PIL import ImageChops 
import os

#from PIL import ImageEnhance


ori_path = '/home/jl/gif/resized/'
gen_path = '/home/jl/gif/blur/'

for file in os.listdir('/home/jl/gif/blur/'):
    image_one = Image.open(ori_path + file)
    image_two =  Image.open(gen_path + file)

    diff = ImageChops.difference(image_one, image_two)
    r,g,b=diff.split()      #RGB分离
    invertr=ImageChops.invert(r)    #红色反向
    img1=invertr.convert('1')       #转成黑白图，黑点即红点
    img = img1.convert("RGBA") 
    width, height = img.size
    for i in range(0,width):     # 遍历所有长度的点
        for j in range(0,height):       # 遍历所有宽度的点
            data = img.getpixel((i,j))  # 获取一个像素
            if (data.count(255) == 4):  # RGBA都是255，改成透明色
                img.putpixel((i,j),(255,255,255,0))
            else:
                #if img.getpixel((i,j))[0]>200:
                img.putpixel((i,j),(255,0,0,255))
                img.paste((255,0,0,255),(i-7,j-7,i,j))  #放大红点范围
    img=img.convert("RGB")
    image_one_l=image_one.convert("L")      #转化为灰度
    image_one=image_one_l.convert("RGB")    #再把灰度图像转为RGB
    #r,g,b=image_one.split()
    r,g,b=img.split()
    image=Image.composite(image_one,img,g)

    # image.show()
    # image.save('/home/jl/gif/results/' + file.split('.')[0] + '.jpg')
    image.save('/home/jl/gif/red/' + file)
        
    if diff.getbbox() is None:
    # 图片间没有任何不同则直接退出
        print("[+]We are the same!")
    else:
        diff.save('/home/jl/gif/black/' + file)



