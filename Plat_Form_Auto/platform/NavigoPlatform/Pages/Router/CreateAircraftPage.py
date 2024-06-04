import os
import time

from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By
from NavigoPlatform.Configurations.Config import TestConfig

logs = TestConfig.get_logs()


class CreateAirCraftPage(BasePage):
    global c_before
    global c_after
    # AirCraft Details section
    LOCAircraftTab = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[1]/div[3]")
    LOCAvailableAircraftTab = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]")
    LOCCreateNewAircraftBtn = (
        By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/button")
    LOCAircraftMake = (By.ID, "make")
    LOCAircraftModel = (By.ID, "model")
    LOCAircraftTitle = (By.ID, "title")
    LOCAircraftTail = (By.ID, "tail_number")
    LOCAircraftWeight = (By.ID, "weight")
    LOCAircraftLength = (By.ID, "length")
    LOCAircraftSeatsTotal = (By.ID, "seats_total")
    LOCAircraftNumberOfEngines = (By.ID, "number_of_engines")
    LOCAircraftEngineType = (By.ID, "engine_type")
    LOCAircraftMaxSpeed = (By.ID, "max_speed")
    LOCAircraftMaxPayload = (By.ID, "maximum_payload")
    LOCAirSchematicsBrowseFiles = (By.ID, "file-input")

    # Seat Availability Section
    LOCSeatAvailabiltyTab = (By.XPATH, "//*[@id='navigo.modal']/div/div[2]/div/div[1]/div[2]")
    LOCBrowseSeatSelection = (By.ID, "file-input")
    LOCSaveAircraftBtn = (By.XPATH, "//*[@id='navigo.modal']/div/div[3]/div[2]/button/span")
    LOCVerifyAircraftName = (By.XPATH,
                             "//*[@id='root']/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[1]/span")
    # LOCVerifyAircraftName = (By.XPATH, "(//td[contains(@class,'px-3 py-3')]//span)[1]")
    # LOCVerifyAircraftName = (By.XPATH, "(//span[contains(@class,'text-font font-roboto')])[2]")

    # Freight Section
    LOC_Freight_Tab = (By.XPATH, "//div[text()='Freight']")
    LOC_Freight_Space_Availability = (By.ID, "hasFreight")
    LOC_Total_MaxAircraft_Space = (By.ID, "weight_capacity_gr")
    LOC_MainDeck_Toggle = (By.XPATH, "(//input[@id='main'])[1]")
    LOC_Overhead_BinTotal = (By.ID, "bin_total")
    LOC_MainDeck_Maximum_Payload = (By.ID, "bin_max_payload")
    # Lower Deck Forward
    LOC_Lower_Deck_Forward_Toggle = (By.XPATH, "(//input[@id='fordward'])[1]")
    LOC_LowerDeck_Forward_Height = (By.ID, "lower_deck_fordward_height")
    LOC_LowerDeck_Forward_Width = (By.ID, "lower_deck_fordward_width")
    LOC_LowerDeck_Forward_Depth = (By.ID, "lower_deck_fordward_depth")
    LOC_LowerDeck_Forward_Door_Height = (By.ID, "lower_deck_fordward_door_height")
    LOC_LowerDeck_Forward_Door_Width = (By.ID, "lower_deck_fordward_door_width")
    LOC_LowerDeck_Forward_Max_Payload = (By.ID, "lower_deck_fordward_max_payload")
    # Lower Deck Aft
    LOC_LowerDeck_Aft_Toggle = (By.XPATH, "(//input[@id='aft'])[1]")
    LOC_LowerDeck_Aft_Height = (By.ID, "lower_deck_aft_height")
    LOC_LowerDeck_Aft_Width = (By.ID, "lower_deck_aft_width")
    LOC_LowerDeck_Aft_Depth = (By.ID, "lower_deck_aft_depth")
    LOC_LowerDeck_Aft_Door_Height = (By.ID, "lower_deck_aft_door_height")
    LOC_LowerDeck_Aft_Door_Width = (By.ID, "lower_deck_aft_door_width")
    LOC_LowerDeck_Aft_Max_Payload = (By.ID, "lower_deck_aft_max_payload")

    LOC_Save_Aircraft_Btn_With_Freight = (By.XPATH, "//span[text()='Save Aircraft']")

    Aircraft_title_name = " "

    # Aircraft Assignment
    LOC_Aircraft_Assignment_Tab = (By.XPATH, "(//div[contains(@class,'border-b-2 border-solid')])[2]")
    LOC_Assign_Action_Btn = (By.XPATH, "(//img[contains(@class,'min-w-min w-4')])")
    LOC_Selected_Air_Route_Name = (By.XPATH, "//*[@id='navigo.modal']/div/div[2]/div/span")
    LOC_Select_Flight_DropDown = (By.ID, "flight")
    LOC_Assign_Save_Btn = (By.XPATH, "//span[text()='Assign']")
    LOC_Assigned_list = (By.XPATH, "(//span[text()='Assigned'])")

    LOC_Metric_Unit_Change_Path = (By.XPATH, "(//span[contains(@class,'text-font-muted font-roboto')])[3]")
    LOC_Metric_Select = (By.TAG_NAME, "select")

    def __init__(self, driver):
        super().__init__(driver)

    def click_On_Aircraft_Tab(self):
        self.click_on_element(self.LOCAircraftTab)

    def click_On_Available_Aircraft_Tab(self):
        self.click_on_element(self.LOCAvailableAircraftTab)

    def click_On_Create_New_Aircraft_Btn(self):
        self.click_on_element(self.LOCCreateNewAircraftBtn)

    def fill_aircraft_details(self):
        selected_aircraft_make = self.select_from_drop_down(self.LOCAircraftMake)
        selected_aircraft_model = self.select_from_drop_down(self.LOCAircraftModel)
        CreateAirCraftPage.Aircraft_title_name = f'{selected_aircraft_make}+{selected_aircraft_model}+automode'
        self.input_element(self.LOCAircraftTitle, f'{CreateAirCraftPage.Aircraft_title_name}')
        tail_number = self.generate_random_four_digit_number()
        self.input_element(self.LOCAircraftTail, tail_number)
        self.input_element(self.LOCAircraftWeight, "88888")
        self.input_element(self.LOCAircraftLength, "66666")
        self.input_element(self.LOCAircraftSeatsTotal, "450")
        self.input_element(self.LOCAircraftNumberOfEngines, "4")
        self.input_element(self.LOCAircraftEngineType, "automode dual type")
        self.input_element(self.LOCAircraftMaxSpeed, "555")
        # self.input_element(self.LOCAircraftMaxPayload, "999999")

    def upload_seat_schematics(self):
        path_to_schematics_file = os.path.join(os.path.abspath('NavigoPlatform/TestData/Seat_schematics.png'))
        self.upload_file(self.LOCAirSchematicsBrowseFiles, path_to_schematics_file)

    def upload_seats(self):
        path_to_seats_file = os.path.join(os.path.abspath('NavigoPlatform/TestData/75_seats.txt'))
        self.click_on_element(self.LOCSeatAvailabiltyTab)
        self.upload_file(self.LOCBrowseSeatSelection, path_to_seats_file)

    def click_On_Save_Aircraft(self):
        self.click_on_element(self.LOCSaveAircraftBtn)

    def verify_created_aircraft(self):
        if self.is_text_present(self.LOCVerifyAircraftName, CreateAirCraftPage.Aircraft_title_name):
            expected_aircraft_name = self.get_element_by_text(self.LOCVerifyAircraftName)
            assert expected_aircraft_name == CreateAirCraftPage.Aircraft_title_name
        else:
            assert False, f'Created {CreateAirCraftPage.Aircraft_title_name} is not present'

    def click_on_freight_tab(self):
        self.click_on_element(self.LOC_Freight_Tab)

    def select_freight_space_available(self):
        self.select_drop_down_by_value(self.LOC_Freight_Space_Availability, "yes")

    def add_max_payload_cap(self):
        self.input_element(self.LOC_Total_MaxAircraft_Space, "999999")

    def enable_main_deck_toggle(self):
        self.click_on_element(self.LOC_MainDeck_Toggle)
        time.sleep(1)

    def add_overhead_bin_box_dimensions(self):
        self.input_element(self.LOC_Overhead_BinTotal, "888888")
        self.input_element(self.LOC_MainDeck_Maximum_Payload, '999999')

    def enable_lower_deck_forward_toggle(self):
        self.click_on_element(self.LOC_Lower_Deck_Forward_Toggle)
        time.sleep(1)

    def add_lower_deck_forward_details(self):
        self.input_element(self.LOC_LowerDeck_Forward_Height, "500")
        self.input_element(self.LOC_LowerDeck_Forward_Width, "500")
        self.input_element(self.LOC_LowerDeck_Forward_Depth, "500")
        self.input_element(self.LOC_LowerDeck_Forward_Door_Height, "800")
        self.input_element(self.LOC_LowerDeck_Forward_Door_Width, "600")
        self.input_element(self.LOC_LowerDeck_Forward_Max_Payload, "9999")

    def enable_lower_deck_aft_toggle(self):
        self.click_on_element(self.LOC_LowerDeck_Aft_Toggle)
        time.sleep(1)

    def add_lower_deck_aft_details(self):
        self.input_element(self.LOC_LowerDeck_Aft_Height, "400")
        self.input_element(self.LOC_LowerDeck_Aft_Width, "400")
        self.input_element(self.LOC_LowerDeck_Aft_Depth, "400")
        self.input_element(self.LOC_LowerDeck_Aft_Door_Height, "700")
        self.input_element(self.LOC_LowerDeck_Aft_Door_Width, "500")
        self.input_element(self.LOC_LowerDeck_Aft_Max_Payload, "9999")

    def save_aircraft_freight(self):
        self.click_element(self.LOC_Save_Aircraft_Btn_With_Freight)

    def click_on_aircraft_assignment_tab(self):
        self.click_on_element(self.LOC_Aircraft_Assignment_Tab)

    def before_aircraft_assignment(self):
        list_of_assign_aircrafts_before_count = self.get_elements(self.LOC_Assigned_list)
        count_before = len(list_of_assign_aircrafts_before_count)
        logs.info("list of assigned aircrafts len before assignment is:")
        logs.info(count_before)
        return count_before

    def click_on_assign_action_btn(self):
        time.sleep(4)
        CreateAirCraftPage.c_before = CreateAirCraftPage.before_aircraft_assignment(self)
        time.sleep(4)
        self.click_on_single_element_from_list_of_elements(self.LOC_Assign_Action_Btn)

    def select_available_air_craft_from_dropdown(self):
        time.sleep(10)
        logs.info("selected airroute and aircraft names are mentioned below:")
        route_name = self.get_element_by_text(self.LOC_Selected_Air_Route_Name)
        logs.info(route_name)
        selected_air_craft = self.select_from_drop_down(self.LOC_Select_Flight_DropDown)
        logs.info(selected_air_craft)
        time.sleep(1)

    def after_aircraft_assignment(self):
        list_of_assign_aircrafts_after_count = self.get_elements(self.LOC_Assigned_list)
        count_after = len(list_of_assign_aircrafts_after_count)
        logs.info("list of assigned aircrafts len after new assignment is:")
        logs.info(count_after)
        return count_after

    def click_on_assign_save_btn(self):
        self.click_element(self.LOC_Assign_Save_Btn)
        time.sleep(5)
        CreateAirCraftPage.c_after = CreateAirCraftPage.after_aircraft_assignment(self)
        if CreateAirCraftPage.c_after > CreateAirCraftPage.c_before:
            assert True
        else:
            assert False, "AirCraft Assignment didnt happened properly"

    def change_the_aircraft_metric_unit(self):
        # assuming default will always be Metric Unit
        time.sleep(4)
        self.select_drop_down_by_value(self.LOC_Metric_Select, "imperial")
        time.sleep(2)

    def verify_metric_unit_change(self):
        if self.is_text_present(self.LOC_Metric_Unit_Change_Path, 'lbs'):
            assert True
        else:
            self.take_screenshot()
            assert False
