from appium.webdriver.common.appiumby import AppiumBy
import time
import elements

import logging

logger = logging.getLogger(__name__)


def test_info_submenu(driver):
    logger.info("Verifying 'Home View' is present.")
    assert len(driver.find_elements(AppiumBy.XPATH, elements.HOME_VIEW)) > 0
    assert len(driver.find_elements(AppiumBy.XPATH, elements.INFO_VIEW)) < 1
    
    info_open_button = driver.find_element(AppiumBy.CLASS_NAME, elements.OPEN_INFO_BUTTON)
    info_open_button.click()
    time.sleep(1)
    
    logger.info("Verifying 'Information View' is present.")
    assert driver.find_element(AppiumBy.XPATH, elements.INFO_VIEW)
    info_close_button = driver.find_element(AppiumBy.CLASS_NAME, elements.CLOSE_INFO_BUTTON)
    info_close_button.click()
    time.sleep(1)
    
    logger.info("Verifying 'Home View' is present.")
    assert len(driver.find_elements(AppiumBy.XPATH, elements.INFO_VIEW)) < 1
    assert len(driver.find_elements(AppiumBy.XPATH, elements.HOME_VIEW)) > 0