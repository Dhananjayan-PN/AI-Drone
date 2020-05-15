from tello_module import Tello
import cv2
import math
import time

tello = Tello()
tello.connect()

tello.streamoff()
time.sleep(1)
tello.streamon()

cv2.namedWindow("Live Drone Footage")
frame_read = tello.get_frame_read()
_time = time.time()

try:
    while True:
        if (_time - time.time() > 5):
            print('{}%'.format(tello.get_battery()))
            _time = time.time()
        frame = frame_read.frame
        face_cascade = cv2.CascadeClassifier("frontalface.xml")
        faces = face_cascade.detectMultiScale(frame)
        try:
            x, y, w, h = faces[0]
            #print(x, y, w, h)
            print(str(x+(w/2)), str(y+(h/2)))
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
        except Exception as e:
            print(e)
        cv2.imshow("drone", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            tello.end()
            break
except KeyboardInterrupt:
    tello.end()
