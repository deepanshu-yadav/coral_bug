
import cv2
from threading import Thread

"""
Helper classs for starting a separate thread for reading frame from the Camera 
Device

"""


class VideoStream:
    """ Camera object that controls
        video streaming from the Camera
    """

    def __init__(self, resolution=(640, 480), framerate=30, source=0):
        # Initialize the PiCamera and the camera image stream
        self.stream = cv2.VideoCapture(source)

        # Read first frame from the stream
        (self.grabbed, self.frame) = self.stream.read()

        # Variable to control when the camera is stopped
        self.stopped = False

    def start(self):

        # Start the thread that reads frames from the video stream
        Thread(target=self.update, args=(), name="Reader Thread").start()

        return self

    def update(self):
        # Keep looping indefinitely until the thread is stopped
        while True:
            # If the camera is stopped, stop the thread
            if self.stopped:
                # Release camera resources

                self.stream.release()

                return

            # Otherwise, grab the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()


    def read(self):
        # Return the most recent frame
        return self.frame

    def stop(self):
        # Indicate that the camera and thread should be stopped
        self.stopped = True

