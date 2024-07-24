import cv2

image = cv2.imread("ENTER THE NAME OF YOUR PIC",cv2.IMREAD_UNCHANGED)

scale_percent = "UPDATE THIS SCALE AS AN INTEGER"

#0 FOR HEIGHT AND 1 FOR WIDTH
new_width = int(image.shape[1]*scale_percent/100)
new_height = int(image.shape[0]*scale_percent/100)

output = cv2.resize(image,(new_height, new_width))


cv2.imwrite("newImage.jpg",output)
cv2.imshow("newImage.jpg",output)
cv2.waitKey(0)