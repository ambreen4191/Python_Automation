import time
from selenium.webdriver.common.by import By
from NavigoPlatform.CommonBase.BasePage import BasePage


class AirRoutesPage(BasePage):
    LOCCreateNewRouteBtn = (By.XPATH, "//span[text()='Create New Route']")
    LOCOriginCNDropDown = (By.XPATH, "(//select[contains(@class,'text-sm w-full')])[1]")
    LOCOriginAirportName = (By.ID, "origin_airport_name")
    LOCOriginAirportCode = (By.ID, "origin_airport_code")
    LOCOriginAirportMapPoint = (By.XPATH, "//*[@id='DestinationFormMap']/div[2]/canvas[1]")
    LOCOriginAirportCoordinates = (By.ID, "origin_airport_coorinates")
    LOCOriginAirportStartTime = (By.ID, "origin_time")
    LOCStartTimeZone = (By.XPATH, "//div[contains(@class,'px-2 py-[6px]')]//select)[2]")
    LOCStartNextBtn = (By.XPATH, "//span[text()='Next']")

    LOCDestCnDropDown = (
        By.XPATH, "//*[@id='navigo.modal']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/select[1]")
    LOCDestAirportName = (By.ID, "destination_airport_name")
    LOCDestAirportCode = (By.ID, "destination_airport_code")
    LOCDestAirportCoordinates = (By.ID, "destination_airport_coorinates")
    LOCDestAirportEndTime = (By.ID, "destination_time")
    LOCDestEndTimeZone = (
        By.XPATH, "//*[@id='navigo.modal']/div[1]/div[2]/div[1]/div[2]/div[1]/div[6]/div[1]/select[1]")
    LOCDestNextBtn = (By.XPATH, "//span[text()='Next']")

    LOCPriceText = (By.ID, "cost")
    LOCCreateAirRouteBtn = (By.XPATH, "//*[@id='navigo.modal']/div/div[2]/div/div[3]/button[2]/span")

    LOC_Route_Name = (By.XPATH, "(//td[contains(@class,'px-3 py-3')]//span)[3]")
    LOC_Delete_AirRoute_Icon = (By.XPATH, "(//div[@class='cursor-pointer ml-4']//img)[1]")
    LOC_Delete_AirRoute_Btn = (By.XPATH, "(//span[@class='visible'])[3]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_create_new_route_btn(self):
        time.sleep(5)
        self.click_on_element(self.LOCCreateNewRouteBtn)

    def fill_all_origin_details(self):
        origin_cn_name = self.select_country_from_drop_down(self.LOCOriginCNDropDown)
        time.sleep(5)
        self.input_element(self.LOCOriginAirportName, f'{origin_cn_name}+automation')
        time.sleep(5)
        self.input_element(self.LOCOriginAirportCode, f'{origin_cn_name}+auto123')
        time.sleep(5)
        self.click_on_random_location(self.LOCOriginAirportMapPoint)
        time.sleep(5)
        self.input_element(self.LOCOriginAirportStartTime, "14:30 PM")
        self.click_on_element(self.LOCStartNextBtn)

    def fill_all_destination_details(self):
        dest_cn_name = self.select_country_from_drop_down(self.LOCDestCnDropDown)
        self.input_element(self.LOCDestAirportName, f'{dest_cn_name}+automation')
        self.input_element(self.LOCDestAirportCode, f'{dest_cn_name}+auto789')
        time.sleep(5)
        self.click_on_random_location(self.LOCOriginAirportMapPoint)
        self.input_element(self.LOCDestAirportEndTime, "19:30 PM")
        self.click_on_element(self.LOCDestNextBtn)

    def enter_price_details(self):
        time.sleep(5)
        self.input_element(self.LOCPriceText, "2222")

    def click_on_create_air_route_btn(self):
        self.click_element(self.LOCCreateAirRouteBtn)

    def click_on_delete_icon(self):
        time.sleep(4)
        if self.is_element_displayed(self.LOC_Delete_AirRoute_Icon):
            if self.is_element_displayed(self.LOC_Route_Name):
                delete_route_name = self.get_element_by_text(self.LOC_Route_Name)
                self.click_on_element(self.LOC_Delete_AirRoute_Icon)
                time.sleep(1)
                self.click_on_element(self.LOC_Delete_AirRoute_Btn)
                time.sleep(3)
                currently_available_route_name = self.get_element_by_text(self.LOC_Route_Name)
                if delete_route_name != currently_available_route_name:
                    return delete_route_name
                else:
                    assert False, "AirRoute is not deleted. There is a mismatch on the AirRoute!"
            else:
                self.take_screenshot()
                assert False, "The route which you are trying to delete is not present !"
        else:
            self.take_screenshot()
            assert False, "The route icon is not present for which you are trying to delete !"
