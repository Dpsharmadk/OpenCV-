import cv2

img = cv2.imread("images/sample.jpg")

if img is None:
    print("Image not found")
    quit()

# draw line
cv2.line(img, (50, 50), (300, 50), (0, 255, 0), 3)

# draw rectangle
cv2.rectangle(img, (100, 100), (300, 250), (255, 0, 0), 2)

# draw circle
cv2.circle(img, (400, 200), 50, (0, 0, 255), 3)

# add text
cv2.putText(
    img,
    "OpenCV Assignment",
    (50, 350),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

cv2.imshow("Shapes and Text", img)

cv2.waitKey(0)
cv2.destroyAllWindows()