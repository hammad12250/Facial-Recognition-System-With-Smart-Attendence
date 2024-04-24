import cv2
import numpy as np
from finalyearproject.models import RtspCamera, Attendance, Admin
import face_recognition
import os
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class LiveWebCam(object):
    def __init__(self, save_path='intruder_images'):
        self.save_path = save_path
        # Create directory if it does not exist
        os.makedirs(self.save_path, exist_ok=True)
        print("Initializing video capture...")

        # Fetching the latest RTSP link from the database
        latest_rtsp_link = RtspCamera.objects.latest('id').camera_link
        self.url = cv2.VideoCapture(latest_rtsp_link)

        if not self.url.isOpened():
            print("Failed to initialize video capture")
            raise Exception("Failed to initialize video capture")
         
        # Load images and their corresponding encodings for face recognition
        self.images, self.classNames = self.load_images('img/img')
        self.encodeListKnown = self.finding_encoding(self.images)

    def __del__(self):
        self.url.release()
        cv2.destroyAllWindows()

    def mark_attendance(self, person_id):
        # Check if the person with the given ID is already marked present today
        today = datetime.today().date()
        attendance_entry = Attendance.objects.filter(person_id=person_id, date=today).first()

        if attendance_entry is None:
            # If not marked present today, add a new entry to the Attendance table
            attendance_entry = Attendance(person_id=person_id, date=today, time=datetime.now().time())
            attendance_entry.save()

    def detect_intruder(self, encodesCurFrame):
        intruder_detected = False
        for encodeFace in encodesCurFrame:
            matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
            if not any(matches):
                intruder_detected = True
                break
        return intruder_detected

    def save_image(self, img):
        file_name = datetime.now().strftime("%Y%m%d%H%M%S") + '.jpg'
        file_path = os.path.join(self.save_path, file_name)
        cv2.imwrite(file_path, img)

    def send_email(self, img):
        try:
            sender_email = "ar256381@gmail.com"
            admin_email = Admin.objects.first().email  # Assuming Admin model has only one entry
            email_subject = "Intruder Detected!"
            email_body = "An unknown person has been detected by the security system."
            # Encode the image as a JPEG byte array
            img_bytes = cv2.imencode('.jpg', img)[1].tobytes()
            
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = admin_email
            msg['Subject'] = email_subject

            # Attach email body
            msg.attach(MIMEText(email_body, 'plain'))

            # Attach image
            img_attachment = MIMEImage(img_bytes, _subtype="jpeg")
            img_attachment.add_header('Content-Disposition', 'attachment', filename='intruder.jpg')
            msg.attach(img_attachment)

            # Connect to SMTP server and send email
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.starttls()
            smtp_server.login(sender_email, 'znbg mssa pifl gknm')  # Replace 'your_password' with actual password
            smtp_server.sendmail(sender_email, admin_email, msg.as_string())
            smtp_server.quit()

            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

    def get_frame(self):
        success, imgNp = self.url.read()
        if not success or imgNp is None or imgNp.size == 0:
            raise Exception("Failed to retrieve frame from video stream")

        imgS = cv2.resize(imgNp, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matchIndex >= 0 and matchIndex < len(self.classNames) and matches[matchIndex]:
                person_id = int(self.classNames[matchIndex])  # Assuming person ID is an integer
                self.mark_attendance(person_id)

                name = self.classNames[matchIndex].upper()
                color = (0, 255, 0)  # green color for known person
            else:
                name = "Unknown"
                color = (0, 0, 255)  # red color for unknown person

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(imgNp, (x1, y1), (x2, y2), color, 2)
            cv2.rectangle(imgNp, (x1, y2 - 35), (x2, y2), color, cv2.FILLED)
            cv2.putText(imgNp, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        intruder_detected = self.detect_intruder(encodesCurFrame)
        if intruder_detected:
            self.save_image(imgNp)
            self.send_email(imgNp)

        resize = cv2.resize(imgNp, (640, 480), interpolation=cv2.INTER_LINEAR)
        ret, jpeg = cv2.imencode('.jpg', resize)
        return jpeg.tobytes()

    @staticmethod
    def load_images(path):
        images = []
        classNames = []
        mylist = os.listdir(path)

        for cls in mylist:
            cur_img = cv2.imread(f'{path}/{cls}')
            images.append(cur_img)
            classNames.append(os.path.splitext(cls)[0])

        return images, classNames

    @staticmethod
    def finding_encoding(images):
        encodeList = []
        for img in images:
            try:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            except Exception as e:
                print(f"Error processing image: {e}")
        return encodeList
