import arm_controller
import bean_finder
import time

def scan(control):
    print("scanning for beans")
    points = bean_finder.find_points()
    direction = arm.shoulder_right
    while len(points) == 0:
        borders = bean_finder.find_pencil()
        if len(borders) > 0:
            if borders[0][0] > camera_mid:
                direction = arm.shoulder_left
            else:
                direction = arm.shoulder_right
        control.run_pin(direction, 0.5)
        points = bean_finder.find_points()
    
    distance = abs(points[0][0] - camera_mid)
    while distance > 10:
        turn_time = distance * 0.005
        
        if points[0][0] < camera_mid:
            arm.run_pin(arm.shoulder_left, turn_time)
        else:
            arm.run_pin(arm.shoulder_right, turn_time)
        points = bean_finder.find_points()
        distance = abs(points[0][0] - camera_mid)

def target_claw(control):
    print("targeting claw")
    control.enable_pin(control.led)
    led_location = bean_finder.find_led()
    while led_location == None:
        control.run_pin(control.shoulder_down, 0.1)
        led_location = bean_finder.find_led()

    spotlight_location = bean_finder.find_spotlight()
    bean_locations = bean_finder.find_points()
    if spotlight_location == None or len(bean_locations) == 0:
        control.disable_pin(control.led)
        return
    distance = spotlight_location[1] - bean_locations[0][1]
    while abs(distance) > 10:
        if distance > 0:
            control.run_pin(control.wrist_up, 0.1)
        else:
            control.run_pin(control.wrist_down, 0.1)
            
        bean_finder.test_show(bean_finder.find_points)
        spotlight_location = bean_finder.find_spotlight()
        bean_locations = bean_finder.find_points()
        if spotlight_location == None or len(bean_locations) == 0:
            break
        distance = spotlight_location[1] - bean_locations[0][1]
    
    control.disable_pin(control.led)

arm = arm_controller.Controller()

camera_mid = 243

def approach_claw(control):
    print("approaching with claw")
    bean_locations = bean_finder.find_points()
    control.enable_pin(control.led)
    led_location = bean_finder.find_led()
    while led_location == None or led_location[1] < bean_locations[0][1] - 100:
        control.run_pin(control.shoulder_down, 0.1)
        led_location = bean_finder.find_led()
        bean_finder.test_show(bean_finder.find_led)
    control.disable_pin(control.led)

try:
##    arm.run_pin(arm.shoulder_up, 2)
##    arm.enable_pin(arm.led)
##    bean_finder.test_show()

##    scan(arm)
##    target_claw(arm)
##    approach_claw(arm)
##    target_claw(arm)
##    arm.run_pin(arm.claw_open, 1)
finally:
    arm.cleanup()
