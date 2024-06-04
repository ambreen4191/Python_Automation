import time

from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By
from NavigoPlatform.Configurations.Config import TestConfig


class FreightManagementPage(BasePage):
    LOC_Freight_Purchase_Tab = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[1]/div[4]")
    LOC_Freight_Management_Tab = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[1]/div[5]")
    LOC_Purchase_Btn = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div/button')
    LOC_Verify_Freight_Management = (
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr')
    LOC_Select_Flight = (By.XPATH, '//*[@id="flight"]')
    LOC_Verify_Available_Flight = (By.XPATH, '//*[@id="flight"]//option[2]')
    LOC_Verify_Table = (
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/table/thead/tr/th')
    LOC_Edit_Btn = (By.XPATH,
                    '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[10]/div/div[2]')
    LOC_Select_DropDown = (By.XPATH, '//*[@id="status"]/option[2]')
    LOC_Select = (By.ID, 'status')
    LOC_Cancel = (By.XPATH, '//*[@id="navigo.modal"]/div/div[3]/div/button')
    LOC_Save = (By.XPATH, '//*[@id="navigo.modal"]/div/div[3]/div[2]/button')
    LOC_Contact_Info_Btn = (By.XPATH,
                            '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[10]/div/div[1]')
    LOC_Status = (
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[6]/span')
    LOC_Logout = (By.ID, 'logout')
    LOC_Delete_Btn = (By.XPATH,
                      '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[10]/div/div[3]')
    LOC_Delete_Popup_Text = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/span')
    logs = TestConfig.get_logs()

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_freight_purchase_tab(self):
        self.click_element(self.LOC_Freight_Purchase_Tab)

    def click_on_freight_management_tab(self):
        self.click_element(self.LOC_Freight_Management_Tab)

    def freight_management_tab(self):
        return self.is_element_displayed(self.LOC_Freight_Management_Tab)

    def logout(self):
        self.click_element(self.LOC_Logout)

    def click_on_edit_btn(self):
        self.click_element(self.LOC_Edit_Btn)

    def verify_select_drop_down(self):
        return self.is_element_displayed(self.LOC_Select_DropDown)

    def verify_freight_management_tab(self):
        time.sleep(1)
        return self.is_element_displayed(self.LOC_Freight_Management_Tab)

    def click_on_purchase_btn(self):
        self.click_element(self.LOC_Purchase_Btn)

    def click_on_select_flight(self):
        self.click_element(self.LOC_Select_Flight)

    def verify_select_available_flight(self):
        element = self.is_element_displayed(self.LOC_Verify_Available_Flight)
        if element:
            assert True
        else:
            assert False

    def verify_table_view(self):
        Table_Text = self.get_element_by_text(self.LOC_Verify_Table)
        if "Air Route" in Table_Text or "Flight Schedule" in Table_Text or "Aircraft" in Table_Text:
            assert True
        else:
            assert False

    def click_on_flight_status(self):
        time.sleep(2)
        print(self.select_from_drop_down(self.LOC_Select))

    def click_on_cancel_btn(self):
        self.click_element(self.LOC_Cancel)

    def click_on_contact_btn(self):
        self.click_element(self.LOC_Contact_Info_Btn)

    def verify_contact_btn(self):
        self.is_element_displayed(self.LOC_Contact_Info_Btn)

    def get_the_status(self):
        return self.get_element_by_text(self.LOC_Status)

    def click_on_save_btn(self):
        self.click_element(self.LOC_Save)
        time.sleep(3)

    def verify_status_popup(self):
        assert self.is_element_displayed(self.LOC_Select)

    def delete_btn(self):
        self.click_element(self.LOC_Delete_Btn)

    def delete_popup_text(self):
        return self.is_text_present(self.LOC_Delete_Popup_Text,
                                    'Are you sure you want to delete this freight from the flight schedule?')
