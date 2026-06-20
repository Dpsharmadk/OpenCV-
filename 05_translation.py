import cv2
import numpy as np

img = cv2.imread("images/sample.jpg")

if img is None:
    print("Image not found")
    quit()

rows, cols = img.shape[:2]

# move image 100 pixels right and 50 down
matrix = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])

translated = cv2.warpAffine(img, matrix, (cols, rows))

cv2.imshow("Original", img)
cv2.imshow("Translated", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()