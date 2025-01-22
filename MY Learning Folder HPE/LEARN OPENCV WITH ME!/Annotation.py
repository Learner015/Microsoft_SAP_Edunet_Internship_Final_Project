import cv2

img  = cv2.imread('DAD.png',1)
# Draw a rectangle
top_left =(100,100)
bottom_right = (400,400)
color = (0,100,255)
thickness = 3

im =cv2.rectangle(img, top_left,bottom_right,color=color,thickness=thickness)
cv2.imshow('Anotated image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
