# Standard imports
import cv2
import numpy as np;
import math

def find_points():
    frame = get_frame()
    
    params = cv2.SimpleBlobDetector_Params()
    params.minArea = 500
    params.filterByConvexity = True
    params.minConvexity = 0
    params.maxConvexity = 1
    params.filterByCircularity = True
    params.minCircularity = 0.3
    params.maxCircularity = 1
    detector = cv2.SimpleBlobDetector(params)

    points = [x.pt for x in detector.detect(frame)]
    print("beans: " + str(points))
    return points

def find_pencil():
    frame = get_frame()
    
    params = cv2.SimpleBlobDetector_Params()
    params.filterByCircularity = False
    params.filterByInertia = False
    params.filterByConvexity = False
    params.filterByColor = True
    params.blobColor = 0xffff00
    params.filterByArea = True
    params.minArea = 1000
    params.maxArea = 5000
    detector = cv2.SimpleBlobDetector(params)

    points = [x.pt for x in detector.detect(frame) if x.pt[1] > 200]
    print("pencils: " + str(points))
    return points

def find_led():
    frame = get_frame()
    
    params = cv2.SimpleBlobDetector_Params()
    params.filterByCircularity = True
    params.minCircularity = 0.3
    params.maxCircularity = 1
    params.filterByInertia = False
    params.filterByConvexity = False
    params.filterByColor = True
    params.blobColor = 255
    params.filterByArea = True
    params.minArea = 300
    params.maxArea = 500
    detector = cv2.SimpleBlobDetector(params)

    keypoints = detector.detect(frame)
##    print(frame.shape)
##    print([frame[x.pt[1], x.pt[0],:] for x in keypoints])
##    print([x.pt for x in keypoints])
    if len(keypoints) > 0:
        points = max(keypoints, key=lambda p: sum(frame[p.pt[1], p.pt[0],:]))
        if sum(frame[points.pt[1], points.pt[0],:]) > 300:
            points =  points.pt
        else:
            points = None
    else:
        points = None
    print("claw: " + str(points))
    return points

def find_spotlight():
    frame = get_frame()
    
    params = cv2.SimpleBlobDetector_Params()
    params.filterByCircularity = True
    params.minCircularity = 0.25
    params.maxCircularity = 1
    params.filterByInertia = False
    params.filterByConvexity = False
    params.filterByColor = True
    params.blobColor = 255
    params.filterByArea = True
    params.minArea = 500
    params.maxArea = 5000
    detector = cv2.SimpleBlobDetector(params)

    keypoints = detector.detect(frame)
    if len(keypoints) > 0:
        points = max(keypoints, key=lambda p: sum(frame[p.pt[1], p.pt[0],:])).pt
    else:
        points = None
    print("spotlight: " + str(points))
    return points

def get_frame():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    return frame

def display_view():
    cv2.imshow("Current View", get_frame())
    cv2.waitKey(0)


def test_show(point_func):
    frame = get_frame()
    x = point_func()
    if x:
        if type(x) == type([]):
            for y in x:
                cv2.circle(frame, (int(y[0]), int(y[1])), 50, (0, 0, 255))
        else:
            cv2.circle(frame, (int(x[0]), int(x[1])), 50, (0, 0, 255))

    cv2.imshow("Keypoints", frame)
    cv2.waitKey(0)
