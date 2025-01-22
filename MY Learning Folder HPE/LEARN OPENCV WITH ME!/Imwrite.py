import cv2

img = cv2.imread(r'DAD.png',0)
status = cv2.imwrite('DADPic.png',img)
# Status is a boolean variable that checks wether image is sucessfully saved or not.
print("Image in file name is : ", status) #output : true => New file named DADPic is created. Here, a grayscale image is generated in new file

