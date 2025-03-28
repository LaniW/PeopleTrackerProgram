# This script checks if cameras are accessible at all indexes 0 to max_index.
# Usually ports 0 or 1 are accessible and typically represent either the 
# computer internal camera or the external USB camera. Make sure to allow
# multiple apps access the same camera as otherwise you may not be able to 
# use the external webcam. 

import cv2

def test_camera(index):
    """Check if a camera is accessible at the given index."""
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"Camera {index} is accessible.")
        cap.release()
    else:
        print(f"Camera {index} is NOT accessible.")

def list_available_cameras(max_index=10):
    """Test available camera indices from 0 to max_index."""
    for i in range(max_index):
        test_camera(i)

if __name__ == "__main__":
    print("Testing available cameras...")
    list_available_cameras(max_index=10)
