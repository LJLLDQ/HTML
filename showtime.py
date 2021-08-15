




















from PIL import Image
import shutil
import os
import cv2

import numpy as np

# im = Image.open('/home/jl/Classifier/16.png')
# width, height = im.size   # Get dimensions

# new_width = 512
# new_height = 512

# left = (width - new_width)/2
# top = (height - new_height)/2
# right = (width + new_width)/2
# bottom = (height + new_height)/2


# print(left)
# print(right)

# # Crop the center of the image
# # im = im.crop((left, top, right, bottom))
# # im.save('/home/jl/Classifier/result1.png')




# # im = Image.open('/home/jl/Classifier/result.png')
# # out = im.resize((1024, 1024),Image.ANTIALIAS)
# # out.save('/home/jl/Classifier/result2.png')






# image = cv2.imread('/home/jl/Classifier/16.png')

# cv2.rectangle(image, (int(left), int(left)), (int(right), int(right)), (0, 0, 255), 2)


# cv2.imwrite('/home/jl/Classifier/2.jpg', image)




img_out=cv2.imread('/home/jl/Classifier/2.jpg')
img_tmp=cv2.imread('/home/jl/Classifier/16.png')



img_out = np.concatenate((img_out, img_tmp), axis=1)
cv2.imwrite("/home/jl/Classifier/merge.jpg",img_out)

