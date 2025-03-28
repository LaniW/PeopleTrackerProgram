import cv2
import mediapipe as mp

class PoseTracker:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(static_image_mode=False, model_complexity=1)

    def detect_poses(self, frame, boxes):
        poses = []
        for (x, y, w, h) in boxes:
            # Crop the person from the frame
            person_img = frame[y:y+h, x:x+w]
            rgb_person = cv2.cvtColor(person_img, cv2.COLOR_BGR2RGB)
            result = self.pose.process(rgb_person)

            # Extract pose landmarks for each detected person
            if result.pose_landmarks:
                landmarks = result.pose_landmarks.landmark
                left_shoulder = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER]
                right_shoulder = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER]
                left_hip = landmarks[self.mp_pose.PoseLandmark.LEFT_HIP]
                right_hip = landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP]

                # Calculate torso center (average of shoulders and hips)
                x_center = int((left_shoulder.x + right_shoulder.x + left_hip.x + right_hip.x) / 4 * frame.shape[1])
                y_center = int((left_shoulder.y + right_shoulder.y + left_hip.y + right_hip.y) / 4 * frame.shape[0])
                poses.append((x_center, y_center))

        return poses
