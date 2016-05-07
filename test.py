import bean_viewer

def assert_equal(expected, actual, message):
	if expected == actual:
		return

	print(message)
	print("Expected: " + str(expected) + " Actual: " + str(actual))

def assert_close_point(expected, actual, message):
	if abs(expected[0] - actual[0]) < location_accuracy and abs(expected[1] - actual[1]) < location_accuracy:
		return

	print(message)
	print("Expected: " + str(expected) + " Actual: " + str(actual))

def spotlight_bean_1_bean_location():
	eye = bean_viewer.BeanEye()
	eye.load_view("test_data/images/spotlight_bean_1.pickle")
	beans = eye.find_beans()
	assert_equal(1, len(beans), "spotlight_bean_1_bean_location: Problem with number of beans found")
	assert_close_point((243, 301), beans[0], "spotlight_bean_1_bean_location: Problem with the bean location")

def spotlight_bean_2_bean_location():
	eye = bean_viewer.BeanEye()
	eye.load_view("test_data/images/spotlight_bean_2.pickle")
	beans = eye.find_beans()
	assert_close_point((243, 301), beans[0], "spotlight_bean_1_bean_location: Problem with the bean location")

def spotlight_bean_3_bean_location():
	eye = bean_viewer.BeanEye()
	eye.load_view("test_data/images/spotlight_bean_3.pickle")
	beans = eye.find_beans()
	assert_close_point((242, 310), beans[0], "spotlight_bean_1_bean_location: Problem with the bean location")

location_accuracy = 25

spotlight_bean_1_bean_location()
spotlight_bean_2_bean_location()
spotlight_bean_3_bean_location()