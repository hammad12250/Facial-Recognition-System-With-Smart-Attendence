import cv2
import numpy as np
from finalyearproject.models import RtspCamera
class LiveWebCam(object):
    def __init__(self):
        print("Initializing video capture...")
        
        # Fetching the latest RTSP link from the database
        latest_rtsp_link = RtspCamera.objects.latest('id').camera_link
        
        self.url = cv2.VideoCapture(latest_rtsp_link)
        
        if not self.url.isOpened():
            print("Failed to initialize video capture")
            raise Exception("Failed to initialize video capture")

    def __del__(self):
        self.url.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        success, imgNp = self.url.read()
        if not success or imgNp is None or imgNp.size == 0:
            raise Exception("Failed to retrieve frame from video stream")

        resize = cv2.resize(imgNp, (640, 480), interpolation=cv2.INTER_LINEAR)
        ret, jpeg = cv2.imencode('.jpg', resize)
        return jpeg.tobytes()

