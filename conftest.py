import os
import pytest
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import elements

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

EXECUTOR = 'http://127.0.0.1:4723'
ANDROID_APP_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'android_app')

apk_files = [f for f in os.listdir(ANDROID_APP_DIR) if f.endswith('.apk')]
assert len(apk_files) == 1, 'App directory can only contain one app file.'
ANDROID_APP_PATH = os.path.join(ANDROID_APP_DIR, apk_files.pop(0))

options = UiAutomator2Options()
options.app = ANDROID_APP_PATH
options.app_package = 'com.resx.test'
options.app_activity = 'com.resx.test.MainActivity'
options.platform_name = 'Android'
options.device_name = 'emulator-5554'
options.automation_name = 'UiAutomator2'
options.no_reset = True

@pytest.fixture(scope="module")
def driver():
    driver_instance = webdriver.Remote(EXECUTOR, options=options)
    yield driver_instance
    driver_instance.quit()

def pytest_runtest_makereport(item, call):
    if call.when == 'call' and call.excinfo is not None:
        driver = item.funcargs['driver']
        click_button_on_failure(driver)
        
def click_button_on_failure(driver):
    try:
        button = driver.find_element(AppiumBy.CLASS_NAME, elements.GO_HOME_BUTTON)
        button.click()
        logger.info("Clicked the button on test failure.")
    except Exception as e:
        logger.error(f"Failed to click the button: {e}")