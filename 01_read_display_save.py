import cv2

# reading image
img = cv2.imread("images/sample.jpg")

# check if image loaded
if img is None:
    print("Image not found")
else:
    print("Image loaded successfully")

# show image
cv2.imshow("Original Image", img)

# save copy
cv2.imwrite("images/output.jpg", img)

print("Image saved")

cv2.waitKey(0)
cv2.destroyAllWindows()