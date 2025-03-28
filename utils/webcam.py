import cv2

class Webcam:
    def __init__(self, camera_id=0):  # Default to camera index 1 (adjust if needed)
        self.camera_id = camera_id
        self.cap = cv2.VideoCapture(self.camera_id)

        # Check if the webcam is accessible
        if not self.cap.isOpened():
            raise ValueError(f"Unable to access the camera with ID {self.camera_id}")

        # Set resolution to Full HD (1920x1080)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        # Optionally set frame rate (if supported by your webcam)
        self.cap.set(cv2.CAP_PROP_FPS, 30)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Failed to grab frame from webcam.")
            return None
        return frame

    def release(self):
        if self.cap:
            self.cap.release()
            print("Webcam released.")

    def show_webcam_feed(self):
        while True:
            frame = self.get_frame()
            if frame is None:
                break

            cv2.imshow("Webcam Feed", frame)

            # Exit loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Exiting webcam feed...")
                break

        self.release()
        cv2.destroyAllWindows()
