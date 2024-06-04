from behave import *
from NavigoPlatform.Configurations.Config import TestConfig
from NavigoPlatform.Pages.Router.LoginPage import LoginPage
from NavigoPlatform.Pages.Router.AirRoutesPage import AirRoutesPage
import os 
logs = TestConfig.get_logs()

def airroutes():
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
    


        logs.info('click on Create New Route button')
        try:
            loginPage = LoginPage(driver)
            airRoutePage = AirRoutesPage(driver)
            airRoutePage.click_on_create_new_route_btn()
            logs.info("clicked on Create New btn")
        except:
            assert False, "Not able to click on Create New button"


        logs.info('Enter all the details of Origin Airport')
        airRoutePage.fill_all_origin_details()
        logs.info("filling origin Details")


        logs.info('Enter all the details of Destination Airport')
        airRoutePage.fill_all_destination_details()
        logs.info("filling Destination Details")


        logs.info('Enter the pricing details')
        airRoutePage.enter_price_details()
        logs.info("Entered Pricing Details")


        logs.info('Click on Save Btn to create new AirRoute')
        airRoutePage.click_on_create_air_route_btn()
        logs.info("Created New Air Route")


        logs.info('Delete the AirRoute')
        deleted_route_name = airRoutePage.click_on_delete_icon()
        logs.info("Deleted the AirRoute. AirRoute name is mentioned below: ")
        logs.info(deleted_route_name)



