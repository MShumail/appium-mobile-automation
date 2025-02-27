from appium import webdriver
from time import sleep

def android_linkedin_login():
    # Desired capabilities for Android
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "15",  # e.g., "12.0"
        "deviceName": "Pixel 6 Pro",          # e.g., "Pixel_4"
        "appPackage": "com.linkedin.android",
        "appActivity": "com.linkedin.android.authenticator.LaunchActivity",
        "automationName": "UiAutomator2"
    }

    # Connect to Appium server
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    sleep(5)

    try:
        # Locate and interact with the Email field
        email_field = driver.find_element_by_id("com.linkedin.android:id/growth_prereg_fragment_login_email_address")
        email_field.send_keys("shumailabc.com")

        # Locate and interact with the Password field
        password_field = driver.find_element_by_id("com.linkedin.android:id/growth_prereg_fragment_login_password")
        password_field.send_keys("Temp/12345678")

        # Locate and click on the Sign In button
        sign_in_button = driver.find_element_by_id("com.linkedin.android:id/growth_prereg_fragment_login_login")
        sign_in_button.click()

        sleep(5)  # Wait for login process

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    android_linkedin_login()
