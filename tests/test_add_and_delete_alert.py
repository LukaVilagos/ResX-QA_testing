from appium.webdriver.common.appiumby import AppiumBy
import time
import elements

import logging

logger = logging.getLogger(__name__)


def test_add_and_delete_alert(driver):
    logger.info("Verifying 'Home View' is present.")
    assert len(driver.find_elements(AppiumBy.XPATH, elements.HOME_VIEW)) > 0
    
    alerts_open_button = driver.find_element(AppiumBy.XPATH, elements.OPEN_ALERTS_BUTTON)
    alerts_open_button.click()
    time.sleep(1)
    
    add_new_alert_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.ADD_NEW_ALERT_BUTTON)
    logger.info("Verifying 'Alert View' is present.")
    assert add_new_alert_button
    
    add_new_alert_button.click()
    time.sleep(1)
    
    alert = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.ALERT)
    logger.info("Verifying 'Alert' is present.")
    assert alert
    
    alert.click()
    time.sleep(1)
    add_new_alert_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.ADD_NEW_ALERT_BUTTON)
    add_new_alert_button.click()
    time.sleep(1)
    
    ok_button = driver.find_element(AppiumBy.XPATH, elements.OK_BUTTON)
    ok_button.click()
    time.sleep(1)
    
    alert_card = driver.find_element(AppiumBy.XPATH, elements.ALERT_CARD)
    logger.info("Verifying 'Alert Card' is present.")
    assert alert_card
    
    logger.info("Verifying 'Add New Alert Button' is not enabled.")
    assert not driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.ADD_NEW_ALERT_BUTTON).is_enabled()
    
    delete_button = driver.find_element(AppiumBy.XPATH, elements.DELETE_ALERT_BUTTON)
    delete_button.click()
    time.sleep(1)
    
    yes_delete_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.YES_DELETE_BUTTON)
    yes_delete_button.click()
    time.sleep(1)
    
    ok_button = driver.find_element(AppiumBy.XPATH, elements.OK_BUTTON)
    ok_button.click()
    time.sleep(1)
    
    logger.info("Verifying 'Add New Alert Button' is enabled.")
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.ADD_NEW_ALERT_BUTTON).is_enabled()
    
    alerts_close_button = driver.find_element(AppiumBy.CLASS_NAME, elements.GO_HOME_BUTTON)
    alerts_close_button.click()
    time.sleep(1)
    
    logger.info("Verifying 'Home View' is present")
    assert len(driver.find_elements(AppiumBy.XPATH, elements.HOME_VIEW)) > 0
    assert len(driver.find_elements(AppiumBy.XPATH, elements.ALERTS_VIEW)) < 1