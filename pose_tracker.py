import cv2
import mediapipe as mp

class PoseTracker:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(static_image_mode=False, model_complexity=1)

    def detect_poses(self, frame):
        # Convert to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.pose.process(rgb_frame)

        poses = []
        if result.pose_landmarks:
            landmarks = result.pose_landmarks.landmark

            # Extract landmarks
            left_shoulder = landmarks[11]
            right_shoulder = landmarks[12]
            left_hip = landmarks[23]
            right_hip = landmarks[24]

            # Calculate torso center (average of shoulders and hips midpoints)
            visible_parts = [
                left_shoulder.visibility,
                right_shoulder.visibility,
                left_hip.visibility,
                right_hip.visibility,
            ]

            # Ensure all points are sufficiently visible (visibility > 0.5)
            if all(part > 0.5 for part in visible_parts):
                x = int(
                    (left_shoulder.x + right_shoulder.x + left_hip.x + right_hip.x) / 4
                    * frame.shape[1]
                )
                y = int(
                    (left_shoulder.y + right_shoulder.y + left_hip.y + right_hip.y) / 4
                    * frame.shape[0]
                )
                poses.append((x, y))

        return poses
