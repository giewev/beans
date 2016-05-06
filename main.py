import arm_controller
import bean_viewer
import time

def scan(controller, viewer):
    print("scanning for beans")
    viewer.update_image()
    points = viewer.find_beans()
    direction = arm.shoulder_right
    while len(points) == 0:
        borders = viewer.find_pencil()
        if len(borders) > 0:
            direction = arm.shoulder_left if borders[0][0] > camera_mid else arm.shoulder_right
        controller.run_pin(direction, 0.5)
        viewer.update_image()
        points = viewer.find_beans()
    
    distance = abs(points[0][0] - camera_mid)
    while distance > 10:
        turn_time = distance * 0.005
        if points[0][0] < camera_mid:
            arm.run_pin(arm.shoulder_left, turn_time)
        else:
            arm.run_pin(arm.shoulder_right, turn_time)
        viewer.update_image()
        points = viewer.find_beans()
        distance = abs(points[0][0] - camera_mid)

def target_claw(controller, viewer):
    print("targeting claw")
    controller.enable_pin(controller.led)
    viewer.update_image()
    led_location = viewer.find_led()
    while led_location == None:
        controller.run_pin(controller.shoulder_down, 0.1)
        viewer.update_image()
        led_location = viewer.find_led()

    spotlight_location = viewer.find_spotlight()
    bean_locations = viewer.find_beans()
    if spotlight_location == None or len(bean_locations) == 0:
        controller.disable_pin(controller.led)
        return
    distance = spotlight_location[1] - bean_locations[0][1]
    while abs(distance) > 10:
        if distance > 0:
            controller.run_pin(controller.wrist_up, 0.1)
        else:
            controller.run_pin(controller.wrist_down, 0.1)
            
        viewer.update_image()
        viewer.test_show(viewer.find_beans)
        spotlight_location = viewer.find_spotlight()
        bean_locations = viewer.find_beans()
        if spotlight_location == None or len(bean_locations) == 0:
            break
        distance = spotlight_location[1] - bean_locations[0][1]
    
    controller.disable_pin(controller.led)

def approach_claw(controller, viewer):
    print("approaching with claw")
    viewer.update_image()
    bean_locations = viewer.find_beans()
    controller.enable_pin(controller.led)
    viewer.update_image()
    led_location = viewer.find_led()
    while led_location == None or led_location[1] < bean_locations[0][1] - 100:
        controller.run_pin(controller.shoulder_down, 0.1)
        viewer.update_image()
        led_location = viewer.find_led()
        viewer.test_show(viewer.find_led)
    controller.disable_pin(controller.led)


arm = arm_controller.Controller()
eye = bean_viewer.BeanEye()
camera_mid = 243

try:
    scan(arm, eye)
    target_claw(arm, eye)
    approach_claw(arm, eye)
    target_claw(arm, eye)
finally:
    arm.cleanup()
