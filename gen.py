# import cv2
# import numpy as np
 
# def nothing(x):
#     pass
 
# img1 = cv2.imread('111.jpg')
# img2 = cv2.imread('222.jpg')
# # 创建一个黑色背景的窗口
# img = np.zeros((500,500,3), np.uint8)
# cv2.namedWindow('image')
 
# cv2.createTrackbar('a','image',0,100,nothing)
 
 
# while(1):
#     cv2.imshow('image',img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
 
#     r = cv2.getTrackbarPos('a','image')
#     r=float(r)/100.0
 
#     img=cv2.addWeighted(img1,r,img2,1.0-r,0)
 
# cv2.destroyAllWindows()

import cv2
import numpy as np
import imageio
import time
# def create_gif(image_list, gif_name, duration=0.35):
#     frames = []
#     for image_name in image_list:
#         frames.append(imageio.imread(image_name))
    
#     return
import os

step_list = [0.02 * x for x in range(0, 51)]
ori_path = 'C:/Users/63463/Desktop/GAN-Web-Selection-master/left/'
gen_path = 'C:/Users/63463/Desktop/GAN-Web-Selection-master/right/'
for file in os.listdir('C:/Users/63463/Desktop/GAN-Web-Selection-master/left/'):
    img1 = cv2.imread(ori_path + file)
    img2 = cv2.imread(gen_path + file)
    cv2.imshow("show", img1)
    frames = []
    for i in step_list:
        res = cv2.addWeighted(img1, i, img2, (1-i), 0)
        img = cv2.cvtColor(np.array(res), cv2.COLOR_BGR2RGB)
        frames.append(img)
    print(file.split('.')[0])
    imageio.mimsave('C:/Users/63463/Desktop/GAN-Web-Selection-master/ori/' + file.split('.')[0] + '.gif', frames, 'GIF', duration=0.35)







# def main():
#     image_list = ['cat/1.png', 'cat/2.png', 'cat/3.png', 'cat/4.png', 'cat/5.png', 'cat/6.png']
#     gif_name = 'cat/cat.gif'
#     duration = 0.35
#     create_gif(image_list, gif_name, duration)


# if __name__ == '__main__':
#     main()