import cv2 #pip install opencv-python
import numpy as np 

image = cv2.imread('zjedzony_dlugopis.jpg')
#npim = np.array(image)
#print(npim) 
boudary1 = np.array([0, 0, 0], dtype = "uint8") 
boundary2= np.array([100, 100, 100], dtype = "uint8")
mask = cv2.inRange(image, boudary1, boundary2)
output = cv2.bitwise_and(image, image, mask =  mask)
colorarray = np.array(output)
img2 = cv2.resize(output, (1024,750)) 
cv2.imshow("color detection", img2) 
cv2.waitKey(0) #nie ma tego = obrazek od razu sie wyłącza
