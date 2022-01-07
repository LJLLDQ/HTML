
# Author: ljl
import cv2
import dlib
import os
import json
import shutil


# step 1

path='non-makeup/' # 输入路径
image_path = os.listdir(path)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") # download address: https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat

for i, image in enumerate(image_path):
    img = cv2.imread(path+image)
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    faces = detector(gray) 

    if len(faces) == 0: # 是否检测出人脸框
        shutil.copy(ORG_path, NEW_path) # 无法识别人脸框图的图像集中到一起，考虑是否移出训练集


# step 2

path='non-makeup/' # 输入路径
image_path = os.listdir(path)


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

dic = {}
for i, image in enumerate(image_path):
    img = cv2.imread(path+image)
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    faces = detector(gray) #

    if len(faces) != 0:
        for face in faces:
            # Use detector to find landmarks
            for face in faces:
                b = []
                # x1 = face.left() # left point
                # y1 = face.top() # top point
                # x2 = face.right() # right point
                # y2 = face.bottom() # bottom point
                # Create landmark object
                landmarks = predictor(image=gray, box=face)
                # if landmarks is none:
                    # print('111111')

                # Loop through all the points
                for n in range(0, 68):
                    a = []
                    x = landmarks.part(n).x
                    y = landmarks.part(n).y
                    # Draw a circle
                    # cv2.circle(img=img, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1)
                    a.append(x)
                    a.append(y)
                    b.append(a)
    
    name = image
    image_path = path+image
    face_landmarks = b
    dic[str(i)] = dict(image_path=image_path,
                       name=image,
                       face_landmarks=face_landmarks)


# 存储称为一个以下格式的json文件
# 'test.json'： {0: {image_path:xxx, name:xxx, face_landmarks:xxx}, 1: {image_path:xxx, name:xxx, face_landmarks:xxx} }

with open('test.json', 'w') as f: # 自定义json文件名
    json.dump(dic, f)              





