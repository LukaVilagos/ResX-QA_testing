from appium.webdriver.common.appiumby import AppiumBy
import time
import elements

import logging

logger = logging.getLogger(__name__)


def test_notifications_submenu(driver):
    logger.info("Verifying 'Home View' is present")
    assert len(driver.find_elements(AppiumBy.XPATH, elements.HOME_VIEW)) > 0
    assert len(driver.find_elements(AppiumBy.XPATH, elements.ALERTS_VIEW)) < 1
    
    alerts_open_button = driver.find_element(AppiumBy.XPATH, elements.OPEN_ALERTS_BUTTON)
    alerts_open_button.click()
    time.sleep(1)
    
    logger.info("Verifying 'Alerts View' is present.")
    assert driver.find_element(AppiumBy.XPATH, elements.ALERTS_VIEW)
    
    alerts_close_button = driver.find_element(AppiumBy.CLASS_NAME, elements.GO_HOME_BUTTON)
    alerts_close_button.click()
    time.sleep(1)
    
    logger.info("Verifying 'Home View' is present")
    assert len(driver.find_elements(AppiumBy.XPATH, elements.HOME_VIEW)) > 0
    assert len(driver.find_elements(AppiumBy.XPATH, elements.ALERTS_VIEW)) < 1