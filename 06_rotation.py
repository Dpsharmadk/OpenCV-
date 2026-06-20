import cv2

img = cv2.imread("images/sample.jpg")

if img is None:
    print("Image not found")
    quit()

rows, cols = img.shape[:2]

center = (cols // 2, rows // 2)

rotation_matrix = cv2.getRotationMatrix2D(
    center,
    45,
    1
)

rotated = cv2.warpAffine(
    img,
    rotation_matrix,
    (cols, rows)
)

cv2.imshow("Original", img)
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()