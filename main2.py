import cv2

image1=cv2.imread('input1.png')
image2=cv2.imread('input2.png')

# 0.5 and 0.4 are weights to be multiplied for each pixel,
#0 is gamma_value (measurement of light)
subtract=cv2.subtract(image1, image2)

cv2.imshow("Output",subtract)

cv2.waitKey(0)
cv2.destroyAllWindows()