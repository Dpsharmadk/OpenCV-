import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Webcam not detected")
    quit()

while True:

    success, frame = camera.read()

    if not success:
        break

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()