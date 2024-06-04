import datetime
from datetime import datetime
import logging
import os
from selenium import webdriver


class TestConfig:
    BROWSER = 'chrome'
    MOZ_BROWSER = 'Mozilla'

    URL = "https://test.navigo.global/apps/router"
    USERNAME = "-"
    PASSWORD = "1234"

    IMPLICIT_WAIT = 10
    


        #The purpose of this method is to create and configure a logger for 
        #logging messages in a Python application.
        #It sets up a logger with a specific log format and saves log messages to a file.
    @staticmethod
    def get_logs():
        #Retrieves the current timestamp in the format "%d_%m_%y_%H_%M_%S" (day_month_year_hour_minute_second).
        TimeStamp = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
        #This timestamp will be used to create a unique log file name.
        TimeOnly = str(datetime.now())
        LogFileName = "logs_" + f"test_{TimeStamp}.log"

        #Creates the full path to the log file by joining the absolute path of the meta-mask/Logs directory with the constructed log file name.
        LogPath = os.path.join(os.path.abspath('NavigoPlatform/Logs'), f"{LogFileName}")
        #Initializes a logger object using the timestamp (converted to a string) as the logger name.
        Logger = logging.getLogger(TimeOnly)
        logging.basicConfig(datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)
        #opening the file in  write mode to overwrite the content
        Filehandler = logging.FileHandler(LogPath, mode="w")
        Formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                    datefmt='%d/%m/%Y %I:%M:%S %p')
        Filehandler.setFormatter(Formatter)
        Logger.addHandler(Filehandler)
        Logger.setLevel(logging.INFO)
        return Logger


    def headless_chrome_browser():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        # options.add_argument('--disable-gpu')  # Required for headless mode
        # options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS'  # Set the path to Chrome 118
        driver = webdriver.Chrome(options=options)
        driver.get(TestConfig.URL)


    def chrome_browser(context):
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        options.add_experimental_option("detach", True)  # Required for headless mode
        context.driver = webdriver.Chrome(options=options)
        context.driver.get(TestConfig.URL)


    def chrome_with_param_browser(headless_mode):
        options = webdriver.ChromeOptions()
        if headless_mode:
            options.add_argument('--headless=new')
        else:
            options.add_argument('start-maximized')
            # Options.add_argument("--window-size=1920x1080")
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options)
        return driver
