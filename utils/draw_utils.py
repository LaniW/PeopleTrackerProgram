import cv2

def draw_keypoints(frame, keypoints):
    for x, y in keypoints:
        cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
    return frame
