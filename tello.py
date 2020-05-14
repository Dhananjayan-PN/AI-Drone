from djitellopy import Tello
import cv2
import math
import time

tello = Tello()  # Initializing tello SDK
tello.connect()

tello.streamoff()
time.sleep(1)
tello.streamon()

tello_frames = tello.get_frame_read()

do = True
while do:
    try:
        print(tello.get_battery()+'%')
        cv2.imshow('drone', tello_frames.frame)
    except KeyboardInterrupt:
        do = False

'''tello.takeoff()
time.sleep(5)

tello.move_up(20)
time.sleep(5)

tello.move_forward(300)
time.sleep(5)

tello.move_right(50)
time.sleep(5)

tello.rotate_clockwise(200)
time.sleep(5)

tello.land()
time.sleep(1)'''

tello.end()
