import cv2

class VideoMotionAnalyzer:
    def __init__(self, video_path):
        self.video_path = video_path

    def analyze_video(self):
        cap = cv2.VideoCapture(self.video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150, apertureSize=3)

            cv2.imshow('frame', frame)
            cv2.imshow('edges', edges)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
