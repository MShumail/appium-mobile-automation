from appium import webdriver

def test_ios_app():
	#Import capabililties from desired_caps.py
	from ios.desired_caps import get_ios_caps

	# Setup WebDriver
	driver= webdriver.Remote('http://localhost:4723/wd/hub', get_ios_caps())
   	 print("iOS test started!")
    
   	 # Example: Test steps here
   	 driver.quit()
