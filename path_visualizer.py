import cv2

class PathVisualizer:
    def __init__(self):
        self.trails = {}

    def visualize(self, frame, poses):
        # Update trails for each detected pose (Should only have one trail, and the trail should be thicker)
        for i, pose in enumerate(poses):
            if i not in self.trails:
                self.trails[i] = []
            self.trails[i].append(pose)

            # Keep the trail length manageable
            if len(self.trails[i]) > 50:
                self.trails[i].pop(0)

        # Draw trails
        for trail in self.trails.values():
            for j in range(1, len(trail)):
                cv2.line(frame, trail[j - 1], trail[j], (0, 255, 0), 2)

        return frame
