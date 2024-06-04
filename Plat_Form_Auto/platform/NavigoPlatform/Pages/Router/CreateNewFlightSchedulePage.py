import time
from datetime import date
from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By
from NavigoPlatform.Configurations.Config import TestConfig


class CreateNewFlightSchedulePage(BasePage):
    LOC_Flight_Schedule_Tab = (By.XPATH, "//div[text()='Flight Schedules']")
    LOC_Create_New_Flight_Schedule = (By.XPATH, "//span[text()='Create New Flight Schedule']")
    LOC_Air_Route_Drop_Down = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/select")
    LOC_Title = (By.ID, "title")
    LOC_Calender_Next_arrow = (By.XPATH, "//img[contains(@class,'rotate-180 h-7')]")
    LOC_Calender_Date_Btn = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div[1]/div/"
                                       "div[1]/div[2]/div/button[18]")
    LOC_Total_Value = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div/span")
    LOC_Next_Btn = (By.XPATH, "//span[text()='Next']")
    LOC_Air_Route_Name = (By.XPATH, "(//div[@class='my-4']//span)[2]")

    LOC_Purchaser_Name = (By.ID, "name")
    LOC_Addition_Name_Line = (By.ID, "name2")
    LOC_Address = (By.ID, "address")
    LOC_Apartment_number = (By.ID, "apartment_number")
    LOC_Post_Office_Box = (By.ID, "post_office_box")
    LOC_City = (By.ID, "city")
    LOC_State = (By.ID, "state")
    LOC_Postal_code = (By.ID, "postal_code")
    LOC_Cn_Drop_Down = (By.ID, "country")
    LOC_Email = (By.ID, "email")
    LOC_Phone_number = (By.ID, "phone_number")
    LOC_Complete_Purchase_btn = (By.XPATH, "//span[text()='Complete Purchase']")

    LOC_Purchase_Completed = (By.XPATH, "//span[text()='Purchase Completed']")
    LOC_Close_Btn = (By.XPATH, "//span[text()='Close']")
    Air_route_drop_down_text = "Brazil+auto123 (Brazil) - Suriname+auto789 (Suriname) [14:30 UTC to 19:30 UTC]"

    # Flight Schedule Status
    LOC_Flight_Schedule_Action_Btn = (By.XPATH, "(//img[contains(@class,'min-w-min w-4')])[1]")
    LOC_Flight_Status_Drop_Down = (By.ID, "status")
    LOC_Flight_Payment_Status_Drop_Down = (By.ID, "paymentStatus")
    LOC_Flight_Schedule_Status_Save = (By.XPATH, "(//span[@class='visible'])[3]")
    LOC_Flight_Edit_Schedule_Title = (By.ID, "title")
    LOC_Flight_Schedule_List_Title = (By.XPATH,
                                      "//table[contains(@class,'w-full undefined')]/tbody[1]/tr[1]/td[1]/span[1]")
    LOC_Flight_Schedule_Status_Paid = (By.XPATH, "(//div[contains(@class,'flex flex-row')]//span)[2]")
    LOC_Flight_Schedule_Status_Paid_on_List = (By.XPATH,
                                               "//table[contains(@class,'w-full undefined')]/tbody[1]/tr[1]/td[10]/"
                                               "div[1]/span[1]")

    Purchase_Name = "Navigo Auto mode"
    Additional_Name_Line = "Navigo Auto test products"
    Address = "5773, old street , lavington raod"
    Apartment_Number = "555"
    Post_Office_box = "912314"
    City = "California Test"
    State = "Navigo Test State"
    Postal_code = "84739"
    Email = "test.testing@gmail.com"
    Phone_number = "+1(123)4567890"
    Str_Purchase_Completed = "Purchase Completed"
    Flight_Status = "on_time"
    Payment_Status = "paid"
    logs = TestConfig.get_logs()

    def click_on_flight_schedule_tab(self):
        self.click_on_element(self.LOC_Flight_Schedule_Tab)
        time.sleep(2)

    def click_on_create_new_flight_schedule_btn(self):
        self.click_on_element(self.LOC_Create_New_Flight_Schedule)
        time.sleep(8)

    def click_on_air_route_drop_down(self):
        air_route = self.select_from_drop_down(self.LOC_Air_Route_Drop_Down)
        CreateNewFlightSchedulePage.logs.info(air_route)

    def add_title_for_the_air_route(self):
        cur_time = date.today()
        self.input_element(self.LOC_Title, f'Test Auto mode flight schedule {cur_time}')

    def click_on_calendar_nxt_arrow(self):
        self.click_on_element(self.LOC_Calender_Next_arrow)
        time.sleep(2)
        self.click_on_element(self.LOC_Calender_Next_arrow)
        time.sleep(1)

    def click_on_calendar_date(self):
        self.click_on_element(self.LOC_Calender_Date_Btn)
        time.sleep(2)

    def check_for_total_value(self):
        if self.is_element_displayed(self.LOC_Total_Value):
            total_value = self.get_element_by_text(self.LOC_Total_Value)
            CreateNewFlightSchedulePage.logs.info(total_value)
        else:
            self.take_screenshot()

    def click_on_next(self):
        self.click_on_element(self.LOC_Next_Btn)
        time.sleep(2)
        if self.is_element_displayed(self.LOC_Air_Route_Name):
            assert True
        else:
            self.take_screenshot()
            assert False

    def enter_purchaser_details(self):
        self.input_element(self.LOC_Purchaser_Name, CreateNewFlightSchedulePage.Purchase_Name)
        self.input_element(self.LOC_Addition_Name_Line, CreateNewFlightSchedulePage.Additional_Name_Line)
        self.input_element(self.LOC_Address, CreateNewFlightSchedulePage.Address)
        self.input_element(self.LOC_Apartment_number, CreateNewFlightSchedulePage.Apartment_Number)
        self.input_element(self.LOC_Post_Office_Box, CreateNewFlightSchedulePage.Post_Office_box)
        self.input_element(self.LOC_City, CreateNewFlightSchedulePage.City)
        self.input_element(self.LOC_State, CreateNewFlightSchedulePage.State)
        self.input_element(self.LOC_Postal_code, CreateNewFlightSchedulePage.Postal_code)
        time.sleep(2)
        cn_selected = self.select_from_drop_down(self.LOC_Cn_Drop_Down)
        CreateNewFlightSchedulePage.logs.info(cn_selected)
        self.input_element(self.LOC_Email, CreateNewFlightSchedulePage.Email)
        self.input_element(self.LOC_Phone_number, CreateNewFlightSchedulePage.Phone_number)

    def click_on_complete_purchase(self):
        self.click_on_element(self.LOC_Complete_Purchase_btn)

    def check_for_confirmation(self):
        if self.is_text_present(self.LOC_Purchase_Completed, CreateNewFlightSchedulePage.Str_Purchase_Completed):
            assert True
        else:
            self.take_screenshot()
            assert False, f'{CreateNewFlightSchedulePage.Str_Purchase_Completed} is not present'

    def close_conformation_dialog(self):
        self.click_on_element(self.LOC_Close_Btn)

    def get_flight_schedule_title_in_list(self):
        first_flight_schedule_title = self.get_element_by_text(self.LOC_Flight_Schedule_List_Title)
        return first_flight_schedule_title

    def click_on_action_icon(self):
        self.click_on_element(self.LOC_Flight_Schedule_Action_Btn)
        time.sleep(2)

    def select_flight_status_drop_down(self):
        print("LOC_Flight_Edit_Schedule_Title: ",
              self.get_element_by_attribute(self.LOC_Flight_Edit_Schedule_Title, 'value'))
        print("first_flight_schedule_title: ", CreateNewFlightSchedulePage.get_flight_schedule_title_in_list(self))
        if (self.get_element_by_attribute(self.LOC_Flight_Edit_Schedule_Title, 'value') ==
                CreateNewFlightSchedulePage.get_flight_schedule_title_in_list(self)):
            self.select_drop_down_by_value(self.LOC_Flight_Status_Drop_Down, CreateNewFlightSchedulePage.Flight_Status)
        else:
            CreateNewFlightSchedulePage.logs(CreateNewFlightSchedulePage.get_flight_schedule_title_in_list(self))
            CreateNewFlightSchedulePage.logs(
                self.get_element_by_attribute(self.LOC_Flight_Edit_Schedule_Title, 'value'))
            self.take_screenshot()
            assert False, "Flight Schedule name mismatch"

    def select_payment_status_drop_down(self):
        self.select_drop_down_by_value(self.LOC_Flight_Payment_Status_Drop_Down,
                                       CreateNewFlightSchedulePage.Payment_Status)

    def click_on_flight_schedule_save_btn(self):
        self.click_on_element(self.LOC_Flight_Schedule_Status_Save)
        time.sleep(2)
        if self.is_text_present(self.LOC_Flight_Schedule_Status_Paid, 'Paid'):
            assert True
        else:
            self.take_screenshot()
            assert False, "Selected flight schedule status 'Paid' is not present !"
