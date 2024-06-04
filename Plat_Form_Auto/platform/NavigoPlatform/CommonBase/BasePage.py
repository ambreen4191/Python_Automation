import os
import random
import time
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException, \
    NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, \
    InvalidSelectorException as EX
from NavigoPlatform.Configurations.Config import TestConfig

"""This class is the parent of all the page classes"""
"""It contains all the common action methods and utilities for all the pageObjects"""

logs = TestConfig.get_logs()


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_time(self, wait_time):
        wait.WebDriverWait(self.driver, wait_time)

    def click_on_random_location(self, ByLocator):
        Element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ByLocator))
        Element.click()
        # js_code = """
        # var mapElement = document.getElementsByTagName('canvas');
        # var clickEvent = new MouseEvent('click', {
        #     clientX: 30,  // Replace with the desired X coordinate
        #     clientY: 130   // Replace with the desired Y coordinate
        #     });
        #     mapElement[0].dispatchEvent(clickEvent);
        #     """

        # Execute the JavaScript code
        # self.driver.execute_script(js_code)

    def click_on_element(self, ByLocator):
        try:
            Element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ByLocator))
            self.driver.execute_script("arguments[0].click();", Element)
        except EX as e:
            print("Exception! Can't click on the element")

    def click_element(self, ByLocator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ByLocator)).click()

    def input_element(self, ByLocator, Text):
        try:
            WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(ByLocator)).send_keys(Text)
        except EX as e:
            print("Exception! Can't click on the element")

    def get_element_by_text(self, ByLocator):
        Element = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(ByLocator))
        return Element.text

    def is_text_present(self, ByLocator, Text):
        Element = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(ByLocator, Text))
        return Element

    def get_title(self):
        return self.driver.title

    def get_element_by_attribute(self, ByLocator, AttributeName):
        Element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ByLocator))
        return Element.get_attribute(AttributeName)

    def is_element_displayed(self, ByLocator):
        try:
            Element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ByLocator))
            return Element.is_displayed()
        except:
            return False

    def select_country_from_drop_down(self, ByLocator):
        Element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ByLocator))
        DropdownElement = Element
        select = Select(DropdownElement)
        Options = select.options
        SelectedOption = random.choice(Options)
        SelectedCountry = SelectedOption.text
        select.select_by_visible_text(SelectedCountry)
        return SelectedCountry

    def select_from_drop_down(self, ByLocator):
        Element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ByLocator))
        DropdownElement = Element
        select = Select(DropdownElement)
        options = select.options
        SelectedOption = random.choice(options)
        SelectedChoice = SelectedOption.text
        select.select_by_visible_text(SelectedChoice)
        return SelectedChoice

    def upload_file(self, ByLocator, PathToFile):
        FileUpload = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ByLocator))
        FileUpload.send_keys(PathToFile)

    def generate_random_four_digit_number(self):
        # Generate a random 4-digit number
        RandomNumber = random.randint(1000, 9999)
        print(RandomNumber)
        return RandomNumber

    def take_screenshot(self):
        current_date_time = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
        screenshot_path = os.path.join(os.path.abspath('NavigoPlatform/Reports/Screenshots'),
                                       f"Failed_Screenshots_{current_date_time}.png")
        self.driver.save_screenshot(screenshot_path)

    def select_drop_down_by_value(self, ByLocator, option):
        Element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ByLocator))
        Select(Element).select_by_value(option)

    def select_drop_down_by_visible_text(self, ByLocator, text):
        Element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ByLocator))
        DropdownElement = Element
        select = Select(DropdownElement)
        select.select_by_visible_text(text)

    def double_click_element(self, ByLocator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ByLocator))
        actionChains = ActionChains(self.driver)
        actionChains.double_click(element)
        actionChains.perform()

    def select_checkbox(self, ByLocator):
        checkbox = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ByLocator))
        checkbox.click()

    def refresh(self):
        self.driver.refresh()

    def scroll_element(self, from_locator, to_locator):
        element_to_tap = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(from_locator))
        element_to_drag_to = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(to_locator))
        self.driver.scroll(element_to_tap, element_to_drag_to)

    def click_on_single_element_from_list_of_elements(self, ByLocator):
        elements = WebDriverWait(self.driver, 25).until(EC.presence_of_all_elements_located(ByLocator))
        logs.info(elements)
        if elements:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(elements[1])).click()
        else:
            assert False, "Empty list of Paid status for Routes"

    def get_elements(self, ByLocator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(ByLocator))
        return elements
