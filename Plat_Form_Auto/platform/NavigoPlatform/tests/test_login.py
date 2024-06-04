import os
from NavigoPlatform.Configurations.Config import TestConfig
from NavigoPlatform.Pages.Router.LoginPage import LoginPage
logs=TestConfig.get_logs()

def test_login():
    
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


    driver.quit()