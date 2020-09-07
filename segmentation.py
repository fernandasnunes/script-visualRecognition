#using open-Cv lib in python to segmentation
import cv2
import os
#recover local image
image =  cv2.imread("imageTest.jpg")
image = cv2.resize(image,(1000,500))
#shape of numpy array contains image height at first index and width at second index
imgheight=image.shape[0]
imgwidth=image.shape[1]
y1 = 0
segmentation = 20
#M is the number of rows or height of the image while N is the number of columns or width of the image
M = imgheight//segmentation
N = imgwidth//segmentation
for y in range(0,imgheight,M):
    for x in range(0, imgwidth, N):
        y1 = y + M
        x1 = x + N
        tiles = image[y:y+M,x:x+N]
        cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0))
        # save tiles/segmentations in folder save
        cv2.imwrite("save/" + str(x) + '_' + str(y)+".png",tiles)
        #save image segmented
        cv2.imwrite("final.png",image)

