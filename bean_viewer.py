# Standard imports
import cv2
import numpy as np;
import math

class BeanEye(object):
    def __init__(self):
        self.bean_detector = build_bean_detector()
        self.pencil_detector = build_pencil_detector()
        self.led_detector = build_led_detector()
        self.spotlight_detector = build_spotlight_detector()

        self.latest_image = None

    def find_beans():
        if self.latest_image == None:
            return []

        points = [x.pt for x in self.bean_detector.detect(self.latest_image)]
        print("beans: " + str(points))
        return points

    def find_pencil():
        if self.latest_image == None:
            return []

        points = [x.pt for x in self.pencil_detector.detect(self.latest_image) if x.pt[1] > 200]
        print("pencils: " + str(points))
        return points

    def find_led():
        if self.latest_image == None:
            return None

        keypoints = self.led_detector.detect(self.latest_image)
        if len(keypoints) > 0:
            points = max(keypoints, key=lambda p: sum(self.latest_image[p.pt[1], p.pt[0],:]))
            if sum(self.latest_image[points.pt[1], points.pt[0],:]) > 300:
                points =  points.pt
            else:
                points = None
        else:
            points = None
        print("claw: " + str(points))
        return points

    def find_spotlight():
        if self.latest_image == None:
            return None

        keypoints = self.spotlight_detector.detect(self.latest_image)
        if len(keypoints) > 0:
            points = max(keypoints, key=lambda p: sum(self.latest_image[p.pt[1], p.pt[0],:])).pt
        else:
            points = None
        print("spotlight: " + str(points))
        return points

    def update_image():
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        self.latest_image = frame

    def display_view():
        if self.latest_image == None:
            return

        cv2.imshow("Current View", self.latest_image)
        cv2.waitKey(0)

    def test_show(point_func):
        x = point_func()
        if x:
            if type(x) == type([]):
                for y in x:
                    cv2.circle(self.latest_image, (int(y[0]), int(y[1])), 50, (0, 0, 255))
            else:
                cv2.circle(self.latest_image, (int(x[0]), int(x[1])), 50, (0, 0, 255))

        cv2.imshow("Keypoints", self.latest_image)
        cv2.waitKey(0)

## Feature Detector Builders ##
def build_bean_detector():
    bean_params = cv2.SimpleBlobDetector_Params()
    bean_params.minArea = 500
    bean_params.filterByConvexity = True
    bean_params.minConvexity = 0
    bean_params.maxConvexity = 1
    bean_params.filterByCircularity = True
    bean_params.minCircularity = 0.3
    bean_params.maxCircularity = 1
    return cv2.SimpleBlobDetector(bean_params)

def build_pencil_detector():
    pencil_params = cv2.SimpleBlobDetector_Params()
    pencil_params.filterByCircularity = False
    pencil_params.filterByInertia = False
    pencil_params.filterByConvexity = False
    pencil_params.filterByColor = True
    pencil_params.blobColor = 0xffff00
    pencil_params.filterByArea = True
    pencil_params.minArea = 1000
    pencil_params.maxArea = 5000
    return cv2.SimpleBlobDetector(pencil_params)

def build_led_detector():
    led_params = cv2.SimpleBlobDetector_Params()
    led_params.filterByCircularity = True
    led_params.minCircularity = 0.3
    led_params.maxCircularity = 1
    led_params.filterByInertia = False
    led_params.filterByConvexity = False
    led_params.filterByColor = True
    led_params.blobColor = 255
    led_params.filterByArea = True
    led_params.minArea = 300
    led_params.maxArea = 500
    return cv2.SimpleBlobDetector(led_params)

def build_spotlight_detector():
    spotlight_params = cv2.SimpleBlobDetector_Params()
    spotlight_params.filterByCircularity = True
    spotlight_params.minCircularity = 0.25
    spotlight_params.maxCircularity = 1
    spotlight_params.filterByInertia = False
    spotlight_params.filterByConvexity = False
    spotlight_params.filterByColor = True
    spotlight_params.blobColor = 255
    spotlight_params.filterByArea = True
    spotlight_params.minArea = 500
    spotlight_params.maxArea = 5000
    return cv2.SimpleBlobDetector(spotlight_params)