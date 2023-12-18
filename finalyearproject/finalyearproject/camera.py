import cv2
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

        # Adjust the frame rate (if needed)
        self.url.set(cv2.CAP_PROP_FPS, 30)

        # Load Haar Cascade Classifier for face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def __del__(self):
        self.url.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        success, imgNp = self.url.read()
        if not success or imgNp is None or imgNp.size == 0:
            raise Exception("Failed to retrieve frame from video stream")

        # Convert to grayscale for face detection
        gray = cv2.cvtColor(imgNp, cv2.COLOR_BGR2GRAY)

        # Detect faces using Haar Cascade Classifier
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(imgNp, (x, y), (x + w, y + h), (255, 0, 0), 2)

        resize = cv2.resize(imgNp, (480, 480), interpolation=cv2.INTER_LINEAR)
        ret, jpeg = cv2.imencode('.jpg', resize)
        return jpeg.tobytes()

# Example usage:
# webcam = LiveWebCam()
# while True:
#     frame = webcam.get_frame()
#     # Display or process the frame as needed
