import  cv2

image = cv2.imread('img.jpg',1)
if image is None:
    print("Could not open or find the image.")
else:
    print("Image loaded successfully.")
cv2.imshow('Display window', image)        
cv2.waitKey(0)
cv2.destroyAllWindows()