import cv2
import numpy as np
class WebCam():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 800) #width
        self.cap.set(4, 800) #height

    def get_frame(self):
        if self.cap.isOpened() :
            _,frame = self.cap.read()
            _,frame = cv2.imencode('.jpg', frame)
            return  frame.tobytes()


    def reload_webcam(self):
        self.cap = cv2.VideoCapture(0)
