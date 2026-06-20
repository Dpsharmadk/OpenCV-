import cv2

video = cv2.VideoCapture("videos/input.mp4")

if not video.isOpened():
    print("Unable to open video")
    quit()

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter(
    "videos/output.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    20,
    (width, height)
)

while True:

    success, frame = video.read()

    if not success:
        break

    writer.write(frame)

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
writer.release()
cv2.destroyAllWindows()