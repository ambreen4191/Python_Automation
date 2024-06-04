from behave import *
from NavigoPlatform.Configurations.Config import TestConfig
from NavigoPlatform.Pages.Router.CreateNewFlightSchedulePage import CreateNewFlightSchedulePage
from NavigoPlatform.Pages.Router.LoginPage import LoginPage
import os 
logs = TestConfig.get_logs()


def createnewflightschedule():
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
        
        logs.info('Click on Flight Schedule Tab')
        NewFlightSchedule = CreateNewFlightSchedulePage(driver)
        NewFlightSchedule.click_on_flight_schedule_tab()
        logs.info("Clicked on Flight Schedule Tab")


        logs.info('Click on Create New Flight Schedule Btn')
        NewFlightSchedule.click_on_create_new_flight_schedule_btn()
        logs.info("Clicked on Create New Flight Schedule Btn")


        logs.info('Select the suitable Air Route from the dropdown')
        NewFlightSchedule.click_on_air_route_drop_down()
        logs.info("Select the suitable Air Route from the dropdown")


        logs.info('Enter the Suitable Title')
        NewFlightSchedule.add_title_for_the_air_route()
        logs.info("Entered the Suitable Title")


        logs.info('Select the Available Dates')
        NewFlightSchedule.click_on_calendar_nxt_arrow()
        NewFlightSchedule.click_on_calendar_date()
        logs.info("Entered the available dates")


        logs.info('Check if Prices matches or not')
        NewFlightSchedule.check_for_total_value()
        logs.info("Total value checked")


        logs.info('Click on Next btn')
        NewFlightSchedule.click_on_next()
        logs.info("Clicked on Next btn")


        logs.info('Add Purchaser Details')
        NewFlightSchedule.enter_purchaser_details()
        logs.info("Added Purchaser Details")


        logs.info('Click on Complete Purchase')
        NewFlightSchedule.click_on_complete_purchase()
        logs.info("Clicked on Complete Purchase")


        logs.info('Check for the Confirmation')
        NewFlightSchedule.check_for_confirmation()
        logs.info("Checked for the Confirmation")


        logs.info('Close the Confirmation Overlay')
        NewFlightSchedule.close_conformation_dialog()
        logs.info("Checked for the Confirmation")


        logs.info('Click on Action icon')
        NewFlightSchedule.click_on_action_icon()
        logs.info("Clicked on Action icon")


        logs.info('Select Flight Status dropdown as "On Time"')
        NewFlightSchedule.select_flight_status_drop_down()
        logs.info("Select Flight Status dropdown as 'On Time'")


        logs.info('Select Payment Status as "Paid"')
        NewFlightSchedule.select_payment_status_drop_down()
        logs.info("Selected Payment Status as 'Paid'")


        logs.info('Save the Status')
        NewFlightSchedule.click_on_flight_schedule_save_btn()
        logs.info("Saved the Status")

