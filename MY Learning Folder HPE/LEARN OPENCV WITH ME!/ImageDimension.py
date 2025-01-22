import cv2

image =cv2.imread('DAD.png',1)
w = 450
h =450
dim =(w,h)
img = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
# height,width and number of channels

dimension = img.shape
width = img.shape[1]
height = img.shape[0]
channels = img.shape[2]

size1 = image.size

print('Image dimensions are : \n')
print(f'1) Height:{height} \n 2) width : {width} \n channels: {channels}  \n size (number of pixels): {size1}')

b,g,r = cv2.split(img)
merged_img = cv2.merge((b,g,r))
merged_rbg = cv2.merge((r,g,b))
cv2.imshow('color_b_image',b)
cv2.imshow('color_b_image',g)
cv2.imshow('color_b_image',r)
cv2.imshow('merged bgr ',merged_img)
cv2.imshow('merged_rgb',merged_rbg)
cv2.waitKey(0)
cv2.destroyAllWindows()