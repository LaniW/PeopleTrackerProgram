import cv2
from pose_tracker import PoseTracker
from path_visualizer import PathVisualizer
from utils.webcam import Webcam

# Option 1: Use HOG for people detection (replace this with YOLO if you prefer YOLO)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detect_people(frame):
    # Convert frame to grayscale for HOG detector
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect people in the image using HOG
    boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8), padding=(16, 16), scale=1.05)

    return boxes

def main():
    webcam = Webcam(camera_id=0)  # ID of the external webcam, usually index 0
    pose_tracker = PoseTracker()
    path_visualizer = PathVisualizer()

    while True:
        frame = webcam.get_frame()
        if frame is None:
            break

        # Detect people (bounding boxes) using HOG or YOLO
        boxes = detect_people(frame)

        # Detect poses for each person detected in the frame
        poses = pose_tracker.detect_poses(frame, boxes)

        # Visualize the trails
        frame = path_visualizer.visualize(frame, poses)

        # Display the frame with pose tracking
        cv2.imshow("Pose Tracker", frame)

        # Exits the program on the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
