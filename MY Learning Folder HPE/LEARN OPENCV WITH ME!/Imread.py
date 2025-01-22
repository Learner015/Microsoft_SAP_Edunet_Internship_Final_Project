import cv2

# print(cv2.__version__)

# to read the image
img = cv2.imread(r'DAD.png',1)
img1 = cv2.imread(r'TestImage.png',0)
# print(img)


# To convert colors like bgr to gray,lab,hsv etc
color0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
color1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
color2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
cv2.imshow('og image', img)
cv2.imshow('color image to gray scale',color0)
cv2.imshow('color image to hsv',color1)
cv2.imshow('color image to ycr_cb',color2)
# how long it wait
# if null default 0 is selected
cv2.waitKey(0)

cv2.destroyAllWindows()

