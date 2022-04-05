import cv2
import numpy as np

mood = input("Enter your mood (happy or sad): ")

if mood == "happy":
    file_name = "happy.mp4"
else:
    file_name = "https://youtu.be/eX2qFMC8cFo"

#file_name = "happy1.mp4"
window_name = "window"
interframe_wait_ms = 30

cap = cv2.VideoCapture(file_name)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

try:
    while (True):
        ret, frame = cap.read()
        if not ret:
            print("Reached end of video, exiting.")
            break

        cv2.imshow(window_name, frame)
        if cv2.waitKey(interframe_wait_ms) & 0x7F == ord('q'):
            print("Exit requested.")
            break
except KeyboardInterrupt:
    pass

cap.release()
cv2.destroyAllWindows()