import cv2

image1=cv2.imread('input1.png')
resized=cv2.resize(image1,(250,500))

# 0.5 and 0.4 are weights to be multiplied for each pixel,
#0 is gamma_value (measurement of light)


cv2.imshow("Original Image", image1)
cv2.imshow("New Image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()