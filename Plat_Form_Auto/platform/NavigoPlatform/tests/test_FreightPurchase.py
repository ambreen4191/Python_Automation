import re
import time

from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By
from NavigoPlatform.Configurations.Config import TestConfig
from NavigoPlatform.Pages.Router.FreightPurchasePage import FreightPurchasePage
from NavigoPlatform.Pages.Router.LoginPage import LoginPage
import os 
logs = TestConfig.get_logs()


def freightpurchase():
        
        headless_mode = os.environ.get("HEADLESS", "false").lower() == "true"
        driver=TestConfig.chrome_with_param_browser(headless_mode)
        driver.get(TestConfig.URL)
        logs.info("Launch the Chrome browser")

        logs.info("Opening login page")
        loginPage = LoginPage(driver)

        logs.info("Navigo Platfrom is successfully opened")
        loginPage.validate_title()
    
        logs.info("Enter the Login credentials")
        loginPage.enter_login_credentials()

        logs.info("Click the login button")
        loginPage.enter_login()
    

        freight_purchase = FreightPurchasePage(driver)
        logs.info("Click on the Freight Purchase Tab")
        freight_purchase.click_on_freight_purchase_tab()
        

        logs.info("Create the records if its not created")

        record = freight_purchase.check_records()
        if not record:
            freight_purchase.purchase_new_freight_btn()
            freight_purchase.create_new_freight_purchase()

        

        logs.info("Verify the Flights are available")
        freight_purchase.purchase_new_freight_btn()
        freight_purchase.check_flights()


        logs.info('Select the shipment date')
        freight_purchase.purchase_new_freight_btn()
        freight_purchase.shipment_date()


        logs.info('get the old shipment load')
        old_weight = freight_purchase.get_shipment_load_weight()
        old_status = freight_purchase.get_shipment_load()
        logs.info(f"{old_status} {old_weight}")


        logs.info('Change the weight unit')
        convert_to_imperial_unit = False
        convert_to_metric_unit = False
        logs.info(f'{old_weight}')
        if "kg" in old_weight:
            convert_to_imperial_unit = True
        if "lbs" in old_weight:
             convert_to_metric_unit = True
        if convert_to_imperial_unit:
            logs.info("imperial")
            freight_purchase.change_to_imperial_unit()
        if convert_to_metric_unit:
            logs.info("metric")
            freight_purchase.change_to_metric_unit()


        logs.info('get the new shipment load')
        new_status = freight_purchase.get_shipment_load()


        logs.info('is shipment load changed or not')
        logs.info(f"{old_status} and {new_status}")
        assert old_status != new_status


        logs.info('purchase new freight btn')
        freight_purchase.purchase_new_freight_btn()


        logs.info('verify the purchase new freight popup')
        assert freight_purchase.verify_purchase_freight_popup()


        logs.info('verify the measurement')
        freight_purchase.verify_measurement()

        logs.info('add the package')
        freight_purchase.add_package()
        logs.info("Added the package")


        logs.info('verify cargo details')
        freight_purchase.verify_cargo_details_valid()


        logs.info('click on next flight btn')
        freight_purchase.next_btn()


        logs.info('enter the cargo details')
        freight_purchase.add_cargo_details()
        logs.info("Entered the cargo details")


        logs.info('delete the package')
        freight_purchase.delete_package()
        logs.info("Deleted the package")


        logs.info('verify package deleted or not')
        is_package_available = freight_purchase.verify_package_deleted()
        if not is_package_available:
            logs.info("Package deleted successfully")
            assert True

        logs.info('verify the item added or not')
        is_package_available = freight_purchase.verify_package_deleted()
        if is_package_available:
            logs.info("Package Added successfully")
            assert True


        logs.info('Check the cargo details')
        is_measurement_valid = freight_purchase.verify_measurement_details()
        if is_measurement_valid:
            is_shipment_type_valid = freight_purchase.verify_shipment_type_details()
            if is_shipment_type_valid:
                if freight_purchase.add_item_visible():
                    assert freight_purchase.back_btn_visible()
                else:
                    freight_purchase.screenshot()
                    assert False, "Add item button is not available"
            else:
                freight_purchase.screenshot()
                assert False, "Shipment Type is not valid"
        else:
            freight_purchase.screenshot()
            assert False, "Measurement is not valid"


        logs.info('Check the cargo item details')
        if freight_purchase.is_measurement_visible():
            if freight_purchase.is_weight_visible():
                if freight_purchase.is_item_size_visible():
                    assert True
                else:
                    freight_purchase.screenshot()
                    assert False, "Item size is not visible"
            else:
                freight_purchase.screenshot()
                assert False, "Weight box is not visible"
        else:
            freight_purchase.screenshot()
            assert False, "Measurement is not visible"


        logs.info('Add item')
        freight_purchase.add_package()


        logs.info('Enter the next item details')
        freight_purchase.add_next_item_details()
        freight_purchase.next_btn()


        logs.info('calculate weight and items')
        number_of_items, calculated_weight = freight_purchase.calculate_weight_item()


        logs.info('check weight and items')
        total_items, total_weight = freight_purchase.get_total_weight_items()
        if number_of_items == total_items and total_weight == calculated_weight:
            logs.info("Weight and items Matched successfully")
            assert True
        else:
            freight_purchase.screenshot()
            assert False, "Weight and items did not matched"

        logs.info('add more then 20 items')
        try:
            for iterate in range(0, 23):
                freight_purchase.add_package()
            logs.info("Added the items successfully")
        except:
            freight_purchase.screenshot()
            logs.info("Failed to add items")


        logs.info('input multiple items data')
        try:
            freight_purchase.input_multiple_records()
            freight_purchase.next_btn()
            logs.info("Enter multiple items details successfully")
            assert True
        except:
            freight_purchase.screenshot()
            logs.info("Failed to enter multiple items details")
            assert False


        logs.info('Select Use Metric Units Weight')
        assert freight_purchase.select_metric_unit()


        logs.info('get the tab names')
        tabs_name = freight_purchase.get_tab_names()
        logs.info(f"{tabs_name}")
        if "Shipment Date" in tabs_name and "Cargo Details" in tabs_name and \
                "Invoice Summary" in tabs_name and "Purchaser" in tabs_name \
                and "Terms & Conditions" in tabs_name and "Confirmation" in tabs_name:
            assert True
        else:
            freight_purchase.screenshot()
            logs.info("Tabs names are different")
            assert False


        logs.info('view the freights purchase table')
        check = freight_purchase.check_records()
        if check:
            logs.info("Freight Purchase Records are visible")
            assert True
        else:
            freight_purchase.screenshot()
            logs.info("Freight Purchase Records are not visible")
            assert False


        logs.info('Verify Metric unit')
        assert freight_purchase.verify_metric_unit()


        logs.info('Freight Purchase complete table with records')
        air_route_column = freight_purchase.verify_airroute_column()
        if len(air_route_column.split('-')) == 2:
            flight_schedule_column = freight_purchase.verify_flight_schedule_column()
            if len(flight_schedule_column.split(',')) == 3:
                date_column = freight_purchase.verify_date_column()
                if len(date_column.split("-")) == 3:
                    if freight_purchase.verify_flight_status_column():
                        if freight_purchase.verify_aircraft_column():
                            if freight_purchase.verify_weight_column():
                                if freight_purchase.verify_shipment_type_column():
                                    if freight_purchase.verify_freight_status_column():
                                        if freight_purchase.verify_invoice_column():
                                            assert True
                                        else:
                                            freight_purchase.screenshot()
                                            logs.info("Freight Purchase Invoice are invalid")
                                            assert False
                                    else:
                                        freight_purchase.screenshot()
                                        logs.info("Freight Purchase Freight status are invalid")
                                        assert False
                                else:
                                    freight_purchase.screenshot()
                                    logs.info("Freight Purchase Shipment items are invalid")
                                    assert False
                            else:
                                freight_purchase.screenshot()
                                logs.info("Freight Purchase Weight are invalid")
                                assert False
                        else:
                            freight_purchase.screenshot()
                            logs.info("Freight Purchase Air Crafts are invalid")
                            assert False
                    else:
                        freight_purchase.screenshot()
                        logs.info("Freight Purchase Flights status are invalid")
                        assert False
                else:
                    freight_purchase.screenshot()
                    logs.info("Freight Purchase Dates are invalid")
                    assert False
            else:
                freight_purchase.screenshot()
                logs.info("Freight Purchase Flight Schedule are invalid")
                assert False
        else:
            freight_purchase.screenshot()
            logs.info("Freight Purchase Air Router are invalid")
            assert False


  