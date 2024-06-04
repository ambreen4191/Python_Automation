from behave import *
from NavigoPlatform.Configurations.Config import TestConfig
from NavigoPlatform.Pages.Router.AirRoutesPage import AirRoutesPage
from NavigoPlatform.Pages.Router.LoginPage import LoginPage
from NavigoPlatform.Pages.Router.CreateAircraftPage import CreateAirCraftPage
from NavigoPlatform.Pages.Router.LoginPage import LoginPage
import os 
logs = TestConfig.get_logs()


def createaircraft():
        #retrieving the headless from environment variable
        #if it is set , the value would be true , otherwise false
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
        
        logs.info('Click on Tabs Aircraft and Available Aircraft')
        AirCraftPage = CreateAirCraftPage(driver)
        AirCraftPage.click_On_Aircraft_Tab()
        AirCraftPage.click_On_Available_Aircraft_Tab()
        logs.info("clicked on Tabs Aircraft")


        logs.info('Click on Tabs Aircraft and Available Aircraft')
        AirCraftPage = CreateAirCraftPage(driver)
        AirCraftPage.click_On_Aircraft_Tab()
        AirCraftPage.click_On_Available_Aircraft_Tab()
        logs.info("clicked on Tabs Aircraft")


        logs.info('click on Create New Aircraft Btn')
        AirCraftPage.click_On_Create_New_Aircraft_Btn()
        logs.info("clicked on Create New Aircraft Btn")


        logs.info('Enter all Aircraft Details')
        AirCraftPage.fill_aircraft_details()
        logs.info("Filled all the details of the aircraft")


        logs.info('Upload Seat Schematics file')
        AirCraftPage.upload_seat_schematics()
        logs.info("Uploaded the Seat Schematics")


        logs.info('Goto Seat Availability Tab and upload Seat which is less than total number of available Seats')
        AirCraftPage.upload_seats()
        logs.info("Uploaded the Seats txt file")


        logs.info('Save Aircraft')
        AirCraftPage.click_On_Save_Aircraft()
        logs.info("clicked on the Save Btn")


        logs.info('Verify its been Create or not')
        AirCraftPage.verify_created_aircraft()
        logs.info("Verified that the aircraft has created")


        logs.info('Click on Freight Tab')
        AirCraftPage.click_on_freight_tab()
        logs.info("Click on Freight Tab")


        logs.info('Select Freight Space Availability to Yes')
        AirCraftPage.select_freight_space_available()
        logs.info("Selected YES from space available dropdown")


        logs.info('Enter Maximum Payload')
        AirCraftPage.add_max_payload_cap()
        logs.info("Entered Max payload")


        logs.info('Fill all the deck details')
        AirCraftPage.enable_main_deck_toggle()
        logs.info("Enabled main deck toggle btn")
        AirCraftPage.add_overhead_bin_box_dimensions()
        logs.info("Added overhead bin box dimensions")
        AirCraftPage.enable_lower_deck_forward_toggle()
        logs.info("Enabled lower deck forward btn")
        AirCraftPage.add_lower_deck_forward_details()
        logs.info("Added lower deck forward details")
        AirCraftPage.enable_lower_deck_aft_toggle()
        logs.info("Enabled lower deck aft btn")
        AirCraftPage.add_lower_deck_aft_details()
        logs.info("Added lower deck aft details")


        logs.info('Save the Aircraft with Freight')
        AirCraftPage.save_aircraft_freight()
        logs.info("Clicked on Save button to Save the Aircraft with Freight Cap")


        logs.info('Click on Aircraft Tabs and then Aircraft Assignment Tabs')
        AirCraftPage = CreateAirCraftPage(driver)
        AirCraftPage.click_On_Aircraft_Tab()
        logs.info("Clicked on Tabs Aircraft")
        AirCraftPage.click_on_aircraft_assignment_tab()
        logs.info("Clicked on Aircraft Assignment Tab")


        logs.info('Click on Assign Action Button')
        AirCraftPage.click_on_assign_action_btn()
        logs.info('Clicked on Assign Action Button')


        logs.info('Select available AirCraft from Dropdown')
        AirCraftPage.select_available_air_craft_from_dropdown()
        logs.info('Selected available AirRoute from Dropdown')


        logs.info('Click on Assign Button to assign the Aircaft to the Route')
        AirCraftPage.click_on_assign_save_btn()
        logs.info('Clicked on Assign Button')


        logs.info('Select the Imperical Unit')
        AirCraftPage.change_the_aircraft_metric_unit()
        logs.info('Clicked on Unit changed dropdown')


        logs.info('Verify if it has been applied or not')
        AirCraftPage.verify_metric_unit_change()
        logs.info('Verified Unit Change')



