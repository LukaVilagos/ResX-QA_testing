from appium.webdriver.common.appiumby import AppiumBy
import time
import elements
import logging

logger = logging.getLogger(__name__)

def test_checkbox_enables_button(driver):
    reservation = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "American Cut Tribeca, Greenwich St, Manhattan · Indoor, 11:00 PM EST, 2 people")
    reservation.click()
    time.sleep(1)
    
    reservation_button = driver.find_element(AppiumBy.XPATH, elements.CLAIM_RESERVATION_BUTTON)
    
    logger.info("Verifying 'Reservation Submit Button' is not enabled.")
    assert not reservation_button.is_enabled()
    
    checkbox = driver.find_element(AppiumBy.XPATH, elements.RESERVATION_CHECKBOX)
    checkbox.click()
    time.sleep(1)
    
    logger.info("Verifying 'Reservation Submit Button' is enabled.")
    assert reservation_button.is_enabled()
    time.sleep(1)
    
    close_button = driver.find_element(AppiumBy.XPATH, elements.CLOSE_RESERVATION_BUTTON)
    close_button.click()
    