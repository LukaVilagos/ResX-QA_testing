from appium.webdriver.common.appiumby import AppiumBy
import time
import elements

import logging

logger = logging.getLogger(__name__)


def test_day_change(driver):
    logger.info("Verifying 'Home View' is present.")
    assert len(driver.find_elements(AppiumBy.XPATH, elements.HOME_VIEW)) > 0
    assert driver.find_elements(AppiumBy.ACCESSIBILITY_ID, elements.NEW_YORK_BUTTON)
    
    today_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.TODAY_BUTTON)
    tomorrow_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.TOMOROW_BUTTON)
    reservation_today = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.RESERVATION)
    
    tomorrow_button.click()
    time.sleep(1)
    
    reservation_tomorrow = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.RESERVATION_TOMORROW)
    
    logger.info("Verifying 'Reservation Today' and 'Reservation Tomorrow' are not the same.")
    logger.info(f"Reservation today: {reservation_today.id}")
    logger.info(f"Reservation tomorrow: {reservation_tomorrow.id}")
    assert reservation_today != reservation_tomorrow
    
    today_button.click()
    
    logger.info("Verifying 'Home View' is present.")
    assert len(driver.find_elements(AppiumBy.XPATH, elements.INFO_VIEW)) < 1
    assert len(driver.find_elements(AppiumBy.XPATH, elements.HOME_VIEW)) > 0