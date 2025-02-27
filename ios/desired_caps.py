# ios/desired_caps.py
def get_ios_caps():
    return {
        "platformName": "iOS",
        "deviceName": "iPhone Simulator",
        "app": "/path/to/ios-app.app",
        "automationName": "XCUITest"
    }

