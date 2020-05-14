from tello_module import Tello
import cv2
import math
import time

tello = Tello()
tello.connect()

tello.streamoff()
time.sleep(1)
tello.streamon()

cv2.namedWindow("drone")
frame_read = tello.get_frame_read()

try:
    while True:
        img = frame_read.frame
        cv2.imshow("drone", img)
        key = cv2.waitKey(1) & 0xff
except KeyboardInterrupt:
    tello.end()
