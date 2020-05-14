from tello_module import Tello
import cv2
import time

tello = Tello()  # Initializing tello SDK

tello.connect()


tello
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
