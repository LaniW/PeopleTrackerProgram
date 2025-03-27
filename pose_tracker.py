import cv2
import mediapipe as mp

class PoseTracker:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()

    def detect_poses(self, frame):
        # Convert to RGB (Change the color to something more appealing)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.pose.process(rgb_frame)

        poses = []
        if result.pose_landmarks:
            for landmark in result.pose_landmarks.landmark:
                poses.append((int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])))

        return poses
