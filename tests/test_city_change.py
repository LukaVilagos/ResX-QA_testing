from appium.webdriver.common.appiumby import AppiumBy
import time
import elements

import logging

logger = logging.getLogger(__name__)


def test_city_change(driver):
    logger.info("Verifying 'Home View' is present.")
    assert len(driver.find_elements(AppiumBy.XPATH, elements.HOME_VIEW)) > 0
    
    new_york_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.NEW_YORK_BUTTON)
    reservation_new_york = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.RESERVATION)
    
    logger.info("Verifying 'New York Reservations View' is present.")
    assert new_york_button, reservation_new_york
    
    new_york_button.click()
    time.sleep(1)
    
    new_york_current_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.NEW_YORK_CURRENT_BUTTON)
    miami_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.MIAMI_BUTTON)
    
    logger.info("Verifying 'City View' is present.")
    assert new_york_current_button, miami_button
    
    miami_button.click()
    time.sleep(1)
    
    logger.info("Verifying 'Reservation New York' is not present.")
    assert len(driver.find_elements(AppiumBy.ACCESSIBILITY_ID, elements.RESERVATION)) < 1
    
    miami_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.MIAMI_BUTTON)
    miami_button.click()
    time.sleep(1)
    
    miami_current_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.MIAMI_CURRENT_BUTTON)
    new_york_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.NEW_YORK_BUTTON)
        
    logger.info("Verifying 'City View' is present.")
    assert miami_current_button, new_york_button
    
    new_york_button.click()
    time.sleep(1)
    
    logger.info("Verifying 'Home View' is present.")
    assert len(driver.find_elements(AppiumBy.XPATH, elements.HOME_VIEW)) > 0
    
    logger.info("Verifying 'New York Reservations View' is present.")
    assert new_york_button, reservation_new_york
    