# People Tracking Program

This project takes in video feed, finds people in the feed through HOG, within each region where a person is found through mediapipe, calculates the center of that person's torso, and once calculated a red dot marks the center and a trail of green follows that person around. The video feed, red dots and green trails are all depicted on a pop up that shows up when one runs this project. It is important to note that while extremely laggy for multiple people, the third commit made holds code that tracks a single person quite smootly and well with mediapipe alone. 

## Set up
This tutorial assumes you have Python, a Python environment and pip installed already.

1. Clone this GitHub repo
2. Run the following in a terminal within this project:

``` bash
    pip install -r requirements.txt
```

this should download opencv, numpy and mediapipe.
3. Connect the additional webcam if you want to use a different camera at this point. Make sure that multiple apps can access said camera at a time. You can check which cameras are open by running:

``` bash
    python camera_checker.py
```

and then updating the camera index in main.py within the first line of the main function based on whichever index corresponds with your camera of interest. 
4. To run the program, you can enter:

``` bash
    python main.py
```

## Images of the Project