import numpy as np
import cv2 as cv
img= cv.imread('Images/bliss.jpg')
cv.imshow('bliss', img)

test_kernel=  float(1)*np.array([[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[1,1,1],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])

def convolve(kernel, image):
    temp=image.copy()
    for x_traverse in range(image.shape[1]-3):
        for y_traverse in range(image.shape[0]-3):
            km= kernel*(temp[y_traverse:y_traverse+3,x_traverse:x_traverse+3])
            image[y_traverse+1,x_traverse+1]= np.matmul([1,1,1],np.matmul([1,1,1], km))
    return image

convolved_img= convolve(test_kernel, img)
cv.imshow('convolved_image', convolved_img)
cv.imwrite('Images/convolved.jpg', convolved_img)
cv.waitKey(0)