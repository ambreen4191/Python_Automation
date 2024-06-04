import re
import time

from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By
from NavigoPlatform.Configurations.Config import TestConfig

logs = TestConfig.get_logs()



class FreightPurchasePage(BasePage):
    LOC_Freight_Purchase_Tab = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[1]/div[4]")
    LOC_Freight_Purchase_Records = (
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody')
    LOC_Purchase_New_Freight_Btn = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div/button')
    LOC_Select_Available_Flight = (By.ID, 'flight')
    LOC_Available_Flights = (By.XPATH, '//*[@id="flight"]/option[2]')
    LOC_All_Dates = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/button')
    LOC_Swipe_Right = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[2]/div/div/div/button[3]')
    LOC_Select_Date = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/button[31]')
    LOC_Next_Btn = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[3]/button[2]')
    LOC_Back_Btn = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[3]/button')
    LOC_Select_Measurement = (By.ID, 'measurement')
    LOC_Select_Shipment_Type = (By.ID, 'shipmentType')
    LOC_Description = (By.ID, 'description')
    LOC_Weight = (By.ID, 'weight_gr')
    LOC_Item_Size = (By.ID, 'box_id')
    LOC_Invoice_text = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div/div/span')
    LOC_Delete_Btn = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[3]/ul/li/div[2]/div/div[3]/button')
    LOC_Package_Item_Btn = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[2]/button')
    LOC_Shipment_load = (
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[6]/div/span[1]')
    LOC_Shipment_load_Weight = (
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[6]/div/span[2]')
    LOC_Weight_Unit = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div/div/select')
    LOC_Measurement_First_Option = (By.XPATH, '//*[@id="measurement"]/option[1]')
    LOC_Measurement_Second_Option = (By.XPATH, '//*[@id="measurement"]/option[2]')
    LOC_Shipment_Type_First_Option = (By.XPATH, '//*[@id="shipmentType"]/option[1]')
    LOC_Shipment_Type_Second_Option = (By.XPATH, '//*[@id="shipmentType"]/option[2]')
    LOC_Next_Item_description = (
        By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[3]/ul[2]/li/div[2]/div/div/div/div/input')
    LOC_Next_Item_Weight = (
        By.XPATH,
        '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[3]/ul[2]/li/div[2]/div/div[2]/div/div/div/div/input')
    LOC_Select_Next_Item_Size = (
        By.XPATH,
        '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[3]/ul[2]/li/div[2]/div/div[2]/div[2]/div/div/select')
    Dynamic_Weight_Xpath = '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div/div/div/div/div[{}]/div/div/span[4]'
    LOC_All_Item_Weight = ()
    LOC_Total_Weight = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div/div/div/div[2]/span[2]')
    LOC_Total_Items = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div/div/div/div[2]/span[1]')
    Multiple_Record_Description_Xpath = '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[3]/ul[{}]/li/div[2]/div/div[1]/div/div/input'
    LOC_Multiple_Description = ()
    Multiple_Record_Weight_Xpath = '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[3]/ul[{}]/li/div[2]/div/div[2]/div/div/div/div/input'
    LOC_Multiple_Weight = ()
    LOC_Tabs = ()
    LOC_Metric_Unit = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div/div/select//*[@value="metric"]')
    LOC_Imperial_Unit = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div/div/select//*[@value="imperial"]')
    LOC_AirRoutes_Column = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[1]/span')
    LOC_Flight_Schedule_Column = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]/span')
    LOC_Date_Column = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[3]/span')
    LOC_Flight_Status_Column = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[4]/span')
    LOC_Aircraft_Column = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[5]/span')
    LOC_Weight_Column = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[6]/div/span[1]')
    LOC_Shipment_Item_Column = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[7]/span')
    LOC_Freight_Status_Columns = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[8]/span')
    LOC_Invoice_Column = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[9]/div/div/img')
    LOC_Dynamic_Date_Select = ()
    Date_Xpath = '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/button[{}]'
    logs = TestConfig.get_logs()

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_freight_purchase_tab(self):
        self.click_element(self.LOC_Freight_Purchase_Tab)

    def check_records(self):
        return self.is_element_displayed(self.LOC_Freight_Purchase_Records)

    def purchase_new_freight_btn(self):
        self.click_element(self.LOC_Purchase_New_Freight_Btn)

    def create_new_freight_purchase(self):
        self.select_from_drop_down(self.LOC_Select_Available_Flight)
        logs.info("Selected the Flight")
        self.click_element(self.LOC_Swipe_Right)
        logs.info("Swipe Right")
        self.click_element(self.LOC_Select_Date)
        logs.info("Selected the date")
        self.click_element(self.LOC_Next_Btn)
        logs.info("Clicked the next button")
        self.select_from_drop_down(self.LOC_Select_Measurement)
        logs.info("Selected the measurement")
        self.input_element(self.LOC_Description, "Laptop Temp")
        logs.info("Entered the Temp Description")
        self.input_element(self.LOC_Weight, "5")
        logs.info("Entered the temp Weight")
        self.click_element(self.LOC_Next_Btn)

    def check_flights(self):
        return self.is_element_displayed(self.LOC_Available_Flights)

    def shipment_date(self):
        self.click_element(self.LOC_Select_Available_Flight)
        logs.info("Selected the Flights")
        time.sleep(1)
        self.click_element(self.LOC_Available_Flights)
        logs.info("Selected the Flights")
        # self.click_element(self.LOC_Swipe_Right)
        while True:
            iterate = 1
            date_found = False
            while True:
                try:
                    self.LOC_Dynamic_Date_Select = (By.XPATH, self.Date_Xpath.format(iterate))
                    element = self.get_element_by_attribute(self.LOC_Dynamic_Date_Select, "class")
                    if "!bg-surface-success border-1 border-surface-success-dark" in element:
                        self.click_element(self.LOC_Dynamic_Date_Select)
                        date_found = True
                        logs.info("Date Available")
                        break
                    else:
                        iterate += 1
                        pass
                except:
                    logs.info("there is no date in this month")
                    break
            if date_found:
                break
            self.click_element(self.LOC_Swipe_Right)
            logs.info("Next Month")

        time.sleep(1)
        self.click_element(self.LOC_Next_Btn)
        logs.info("Selected Next button")

    def verify_measurement(self):
        assert self.is_element_displayed(self.LOC_Select_Measurement)

    def add_cargo_details(self):
        self.select_from_drop_down(self.LOC_Select_Measurement)
        logs.info("Selected Measurement")
        self.select_from_drop_down(self.LOC_Select_Shipment_Type)
        logs.info("Selected the Shipment type")
        self.input_element(self.LOC_Description, "Laptop Temp")
        logs.info("Entered the temp description")
        self.input_element(self.LOC_Weight, "5")
        logs.info("Entered the temp Weight")
        self.select_from_drop_down(self.LOC_Item_Size)
        logs.info("Entered the item temp size")

    def next_btn(self):
        self.click_element(self.LOC_Next_Btn)

    def verify_cargo_details_valid(self):
        assert self.is_text_present(self.LOC_Invoice_text, "Invoice")

    def delete_package(self):
        self.click_element(self.LOC_Delete_Btn)

    def verify_package_deleted(self):
        return self.is_element_displayed(self.LOC_Delete_Btn)

    def add_package(self):
        self.click_element(self.LOC_Package_Item_Btn)

    def screenshot(self):
        self.take_screenshot()

    def get_shipment_load(self):
        return self.get_element_by_text(self.LOC_Shipment_load)

    def get_shipment_load_weight(self):
        return self.get_element_by_text(self.LOC_Shipment_load_Weight)

    def change_unit(self):
        self.select_from_drop_down(self.LOC_Weight_Unit)

    def change_to_imperial_unit(self):
        self.click_element(self.LOC_Weight_Unit)
        self.click_element(self.LOC_Imperial_Unit)

    def change_to_metric_unit(self):
        self.click_on_element(self.LOC_Weight_Unit)
        self.click_on_element(self.LOC_Metric_Unit)

    def verify_purchase_freight_popup(self):
        return self.is_element_displayed(self.LOC_Select_Available_Flight)

    def verify_measurement_details(self):
        is_first_available = self.is_element_displayed(self.LOC_Measurement_First_Option)
        if is_first_available:
            is_second_available = self.is_element_displayed(self.LOC_Measurement_Second_Option)
            return is_second_available
        else:
            return False

    def verify_shipment_type_details(self):
        is_first_available = self.is_element_displayed(self.LOC_Shipment_Type_First_Option)
        if is_first_available:
            is_second_available = self.is_element_displayed(self.LOC_Shipment_Type_First_Option)
            return is_second_available
        else:
            return False

    def add_item_visible(self):
        return self.is_element_displayed(self.LOC_Package_Item_Btn)

    def back_btn_visible(self):
        return self.is_element_displayed(self.LOC_Back_Btn)

    def is_measurement_visible(self):
        return self.is_element_displayed(self.LOC_Select_Measurement)

    def is_weight_visible(self):
        return self.is_element_displayed(self.LOC_Weight)

    def is_item_size_visible(self):
        return self.is_element_displayed(self.LOC_Item_Size)

    def add_next_item_details(self):
        self.input_element(self.LOC_Next_Item_description, "temp_2")
        self.input_element(self.LOC_Next_Item_Weight, "20")
        self.select_from_drop_down(self.LOC_Select_Next_Item_Size)

    def calculate_weight_item(self):
        iterate = 1
        all_weights = []
        while True:
            try:
                self.LOC_All_Item_Weight = (By.XPATH, self.Dynamic_Weight_Xpath.format(iterate))
                all_weights.append(
                    int(self.get_element_by_text(self.LOC_All_Item_Weight).replace("Lbs", '').replace("Kg", '')))
                iterate += 1
            except Exception as e:
                iterate -= 1
                break
        return iterate, sum(all_weights)

    def get_total_weight_items(self):
        Total_Weight_Raw = self.get_element_by_text(self.LOC_Total_Weight)
        Total_Weight = "".join(re.findall(r'\d+', Total_Weight_Raw))
        Total_Items_Raw = self.get_element_by_text(self.LOC_Total_Items)
        Total_Items = "".join(re.findall(r'\d+', Total_Items_Raw))
        return int(Total_Items), int(Total_Weight)

    def input_multiple_records(self):
        iterate = 1
        while True:
            try:
                self.LOC_Multiple_Description = (By.XPATH, self.Multiple_Record_Description_Xpath.format(iterate))
                self.input_element(self.LOC_Multiple_Description, f"item_{iterate}")
                self.LOC_Multiple_Weight = (By.XPATH, self.Multiple_Record_Weight_Xpath.format(iterate))
                self.input_element(self.LOC_Multiple_Weight, f"1{iterate}")
                iterate += 1
            except Exception as e:
                iterate -= 1
                break

    def select_metric_unit(self):
        try:
            self.click_element(self.LOC_Weight_Unit)
            time.sleep(2)
            self.click_element(self.LOC_Metric_Unit)
            logs.info("done")
            return True
        except:
            return False

    def get_tab_names(self):
        iterate = 0
        all_tabs = []
        while True:
            try:
                self.LOC_Tabs = (By.ID, f'{iterate}')
                all_tabs.append(self.get_element_by_text(self.LOC_Tabs))
                iterate += 1
            except:
                iterate -= 1
                break
        return all_tabs

    def verify_metric_unit(self):
        return self.is_element_displayed(self.LOC_Weight_Unit)

    def verify_airroute_column(self):
        return self.get_element_by_text(self.LOC_AirRoutes_Column)

    def verify_flight_schedule_column(self):
        return self.get_element_by_text(self.LOC_Flight_Schedule_Column)

    def verify_date_column(self):
        return self.get_element_by_text(self.LOC_Date_Column)

    def verify_flight_status_column(self):
        return self.is_element_displayed(self.LOC_Flight_Status_Column)

    def verify_aircraft_column(self):
        return self.is_element_displayed(self.LOC_Aircraft_Column)

    def verify_weight_column(self):
        return self.is_element_displayed(self.LOC_Weight_Column)

    def verify_shipment_type_column(self):
        return self.is_element_displayed(self.LOC_Shipment_Item_Column)

    def verify_freight_status_column(self):
        return self.is_element_displayed(self.LOC_Flight_Status_Column)

    def verify_invoice_column(self):
        return self.is_element_displayed(self.LOC_Invoice_Column)






