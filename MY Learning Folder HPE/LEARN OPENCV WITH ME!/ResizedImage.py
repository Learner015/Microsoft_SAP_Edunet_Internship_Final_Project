import cv2
img =cv2.imread('DAD.png',1)
print('Original Dimension',img.shape)

width = 350
height = 350
dimension = (width,height)

resized = cv2.resize(img,dimension,interpolation=cv2.INTER_AREA)

print('Resized image dimension are : ',resized.shape)
cv2.imshow('Resized image', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()