import time

from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By
from NavigoPlatform.Configurations.Config import TestConfig



class FlightScheduleListPage(BasePage):
    LOC_Flight_Schedules_Tab = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[1]/div[2]")
    LOC_Create_New_Flight_Schedule_Btn = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/button")
    LOC_DropDown_Menu = (By.XPATH, "//*[@id='root']/div[2]/div/div[@id='navigo.modal']/div/div[2]/div/div[2]/div/div/select")
    # LOC_DropDown_Menu = (By.CSS_SELECTOR, ".text-sm.w-full.outline-none.bg-surface.text-font")
    LOC_Input_Title = (By.XPATH, "//*[@id='title']")
    Input_Text = "Test_flight_schedule"
    LOC_Swipe_Right_Btn = (By.XPATH, "//*[@id='root']/div[2]/div/div[@id='navigo.modal']/div/div[2]/div/div[2]/div[3]/div/div/div/div/button[3]")
    LOC_Select_Date = (By.XPATH, "//*[@id='root']/div[2]/div/div[@id='navigo.modal']/div/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div/button[32]")
    LOC_Next_Btn = (By.XPATH, "//*[@id='root']/div[2]/div/div[@id='navigo.modal']/div/div[2]/div/div[3]/button[2]")
    LOC_Purchaser_Name = (By.XPATH, "//*[@id='name']")
    LOC_Additional_Name_Line = (By.XPATH, "//*[@id='name2']")
    LOC_Address = (By.XPATH, "//*[@id='address']")
    LOC_Apartment = (By.XPATH, "//*[@id='apartment_number']")
    LOC_Post_Office_Box = (By.XPATH, "//*[@id='post_office_box']")
    LOC_City = (By.XPATH, "//*[@id='city']")
    LOC_State = (By.XPATH, "//*[@id='state']")
    LOC_Postal_Code = (By.XPATH, "//*[@id='postal_code']")
    LOC_Country = (By.XPATH, "//*[@id='country']")
    LOC_Select_Country = (By.XPATH, "//*[@value='US']")
    LOC_Email = (By.XPATH, "//*[@id='email']")
    LOC_Phone_Number = (By.XPATH, "//*[@id='phone_number']")
    LOC_Verify_Flight_Schedule = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]/span')
    LOC_Close_Btn = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[3]/button')

    logs = TestConfig.get_logs()

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_flight_schedules_tab(self):
        self.click_element(self.LOC_Flight_Schedules_Tab)

    def click_on_create_new_flight_schedule_btn(self):
        self.click_element(self.LOC_Create_New_Flight_Schedule_Btn)

    def click_on_drop_menu_btn(self):
        time.sleep(2)
        self.select_from_drop_down(self.LOC_DropDown_Menu)

    def input_title(self):
        self.input_element(self.LOC_Input_Title, self.Input_Text)

    def click_on_swipe_right_btn(self):
        self.click_element(self.LOC_Swipe_Right_Btn)

    def click_on_date(self):
        self.click_element(self.LOC_Select_Date)

    def click_on_next_btn(self):
        self.click_element(self.LOC_Next_Btn)

    def input_purchaser(self):
        self.input_element(self.LOC_Purchaser_Name, "Test")
        self.input_element(self.LOC_Additional_Name_Line, "Test2")
        self.input_element(self.LOC_Address, "Test Address")
        self.input_element(self.LOC_Apartment, "123456")
        self.input_element(self.LOC_Post_Office_Box, "234")
        self.input_element(self.LOC_City, "TempCity")
        self.input_element(self.LOC_State, "tempState")
        self.input_element(self.LOC_Postal_Code, "123123")
        self.select_from_drop_down(self.LOC_Country)
        # self.click(self.LOC_Select_Country)
        self.input_element(self.LOC_Email, "TempEmail@gmail.com")
        self.input_element(self.LOC_Phone_Number, "+1 (123) 456 7890")
        self.click_element(self.LOC_Next_Btn)

    def verify_flight_created(self):
        self.click_on_element(self.LOC_Close_Btn)
        if self.is_text_present(self.LOC_Verify_Flight_Schedule, "Test_flight_schedule"):
            Expected_Flight_Name = self.get_element_by_text(self.LOC_Verify_Flight_Schedule)
            assert Expected_Flight_Name == "Test_flight_schedule"
        pass




