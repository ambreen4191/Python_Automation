import time

from behave import *
from NavigoPlatform.Pages.Router.FreightManagementPage import FreightManagementPage
from NavigoPlatform.Configurations.Config import TestConfig
from NavigoPlatform.Pages.Router.LoginPage import LoginPage
import os 

logs = TestConfig.get_logs()
def freightmanagement():
        
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

    logs.info('Click on Tab Freight Management')
    freight_management = FreightManagementPage(driver)
    freight_management.click_on_freight_management_tab()
    logs.info("Clicked on Freight Management Tab")


    logs.info('Verify the Freight Management Tab')
    verify_tab = freight_management.freight_management_tab()
    assert verify_tab


    logs.info('Click on edit btn')
    freight_management.click_on_edit_btn()
    logs.info("Clicked on Edit button")


    logs.info('Click on Contact Info btn')
    freight_management.click_on_contact_btn()
    logs.info("Clicked on Contact Info button")


    logs.info('Is Contact info visible')
    freight_management.verify_contact_btn()


    logs.info('Freight Management records available')
    verify_tab = freight_management.verify_freight_management_tab()
    assert verify_tab


    logs.info('Verify the Select dropdown')
    element = freight_management.verify_select_drop_down()
    assert element


    logs.info('logout the old account')
    freight_management = FreightManagementPage(driver)
    freight_management.logout()
    logs.info("Logged out the acocunt")


    logs.info('Click on status')
    freight_management.click_on_flight_status()
    logs.info("Clicked on Status button")


    logs.info('Verify the Status Popup')
    freight_management.verify_status_popup()


    logs.info('Click on cancel btn')
    freight_management.click_on_cancel_btn()
    logs.info("Clicked on Cancel button")


    logs.info('Click on save btn')
    freight_management.click_on_save_btn()
    logs.info("Clicked on Save Button")


    logs.info('Get the old status')
    old_status = freight_management.get_the_status()
    time.sleep(2)


    logs.info('Check the Status Changed or not "{Status}"')
    new_status = freight_management.get_the_status()
    time.sleep(2)
    Status=""
    if Status == "Cancel":
        assert old_status == new_status
        logs.info(f"{new_status} are matched to {old_status}")
    if Status == "Save":
        assert old_status != new_status
        logs.info(f"{new_status} are not matched to {old_status}")


    logs.info('Check the Freight Management Tab')
    assert freight_management.verify_freight_management_tab()


    logs.info('Click on Tab Freight Purchases')
    freight_management = FreightManagementPage(driver)
    freight_management.click_on_freight_purchase_tab()
    logs.info("Clicked on Tab Freight Purchase")


    logs.info('Click on the Purchase new Freight')
    freight_management.click_on_purchase_btn()
    logs.info("Clicked on Purchase new Freight button")


    logs.info('Select Available Flight')
    freight_management.click_on_select_flight()
    freight_management.verify_select_available_flight()


    logs.info('Verify the Freight Table columns')
    freight_management.verify_table_view()


    logs.info('verify it is in table format')
    freight_management.verify_table_view()


    logs.info('click on delete btn')
    freight_management.delete_btn()


    logs.info('verify pop up appears')
    assert freight_management.delete_popup_text()


