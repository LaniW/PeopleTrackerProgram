import cv2

class PathVisualizer:
    def __init__(self):
        self.trails = {}

    def visualize(self, frame, poses):
        # Assign trails for each detected person
        for i, pose in enumerate(poses):
            if i not in self.trails:
                self.trails[i] = []  # Create a new trail for the person

            # Add the current position to the trail
            self.trails[i].append(pose)

            # Keep the trail length manageable
            if len(self.trails[i]) > 50:  # Adjust trail length here
                self.trails[i].pop(0)

        # Draw trails
        for person_id, trail in self.trails.items():
            for j in range(1, len(trail)):
                cv2.line(frame, trail[j - 1], trail[j], (0, 255, 0), 2)
                cv2.circle(frame, trail[-1], 5, (0, 0, 255), -1)

        return frame
