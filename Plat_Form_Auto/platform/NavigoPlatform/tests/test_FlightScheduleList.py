import time

from behave import *
from NavigoPlatform.Pages.Router.FlightScheduleListPage import FlightScheduleListPage
from NavigoPlatform.Pages.Router.LoginPage import LoginPage
from NavigoPlatform.Configurations.Config import TestConfig
import os 
logs = TestConfig.get_logs()

def flightschedule():
        headless_mode = os.environ.get("HEADLESS", "false").lower() == "true"
        driver=TestConfig.chrome_with_param_browser(headless_mode)
    
        logs.info("Launch the Chrome browser")
        driver.get(TestConfig.URL)

        logs.info("Opening login page")
        loginPage = LoginPage(driver)

        logs.info("Navigo Platfrom is successfully opened")
        loginPage.validate_title()
    
        logs.info("Enter the Login credentials")
        loginPage.enter_login_credentials()

        logs.info("Click the login button")
        loginPage.enter_login()
        

        logs.info('Click on Tabs Flight Schedule List')
        FlightSchedulePage = FlightScheduleListPage(driver)
        FlightSchedulePage.click_on_flight_schedules_tab()
        logs.info("Clicked on Flight Schedule List Tab")


        logs.info('Create the New Flight Schedule')
        FlightSchedulePage.click_on_create_new_flight_schedule_btn()
        logs.info("Clicked on New Flight Schedule button")
        FlightSchedulePage.click_on_drop_menu_btn()
        logs.info("Clicked on drop down")
        FlightSchedulePage.input_title()
        logs.info("Input Title")
        FlightSchedulePage.click_on_swipe_right_btn()
        logs.info("Swipe Right")
        FlightSchedulePage.click_on_date()
        logs.info("Select the date")
        FlightSchedulePage.click_on_next_btn()
        logs.info("Next Button")
        FlightSchedulePage.input_purchaser()
        logs.info("Input Purchase")


        logs.info('Verify Flight Created or not')
        FlightSchedulePage.verify_flight_created()


