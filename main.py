import cv2
from pose_tracker import PoseTracker
from path_visualizer import PathVisualizer
from utils.webcam import Webcam

def main():
    # Attempt to initialize Webcam (Does not work, I believe it is only accessing the built-in camera)
    webcam = Webcam(camera_id=0) 
    pose_tracker = PoseTracker()
    path_visualizer = PathVisualizer()

    while True:
        frame = webcam.get_frame()
        if frame is None:
            break
        poses = pose_tracker.detect_poses(frame)
        frame = path_visualizer.visualize(frame, poses)

        # Display the frame
        cv2.imshow("Pose Tracker", frame)
        # Exits the program on the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
