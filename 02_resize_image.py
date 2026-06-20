import cv2

img = cv2.imread("images/sample.jpg")

if img is None:
    print("Image not found")
    quit()

# resize image
resized = cv2.resize(img, (500, 400))

cv2.imshow("Original", img)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()