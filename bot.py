from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from alert import Alert
import time


class Bot:

    def __init__(self, url, email, passwrd):
        '''
        initialize Bot class. The class is used to create the scraping Bot.
        :param url: url of housing website
        :param email: login user name
        :param passwrd: login password
        :return: initialized Bot object
        '''
        self.url = url
        self.email = email
        self.passwrd = passwrd

    def check_acc_by_url(self):
        '''
        This is key function of the Bot. 1.website login and filter selection, 2.refresh page until accomodation listed (loop)
        :return: print message (system status)
        '''
        # browser settings
        options = Options()
        options.headless = False
        options.add_experimental_option("detach", True)

        # browser init and call url
        browser = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)
        browser.maximize_window()
        browser.get(self.url)

        # login
        browser.find_element(By.ID, "EmailTextBox").send_keys(self.email)
        browser.find_element(By.ID, "PasswordTextBox").send_keys(self.passwrd)
        time.sleep(2)
        browser.find_element(
            By.CSS_SELECTOR, "a.smallbutton").click()

        time.sleep(10)

        regio = Select(browser.find_element(By.ID, "RegioDropDown"))
        regio.select_by_visible_text("Utrecht")

        cont = Select(browser.find_element(By.ID, "ContingenthouderDropDown"))
        cont.select_by_visible_text("Utrecht University (UU)")

        res = Select(browser.find_element(
            By.ID, "ContingentDoelgroepDropDown"))
        res.select_by_visible_text("UU Master")
        # res.select_by_visible_text("UU PhD Candidates")

        time.sleep(1)

        perio = Select(browser.find_element(
            By.ID, "ContingentPeriodeDropDown"))
        perio.select_by_visible_text("UU Master 2022-2023")

        # loop until accomodation is available
        while True:
            try:
                perio = Select(browser.find_element(
                    By.ID, "ContingentPeriodeDropDown"))
                perio.select_by_visible_text("UU Master 2022-2023")
                time.sleep(5)

                if browser.find_element(By.CLASS_NAME, "templateLijst"):
                    print("something available")
                    # send email notification
                    Alert.email_alert("A room is available !!!",
                                      browser.current_url, self.email)
                    browser.quit()
                    break
                browser.execute_script("location.reload(true);")
            except:
                print("nothing available")
                browser.execute_script("location.reload(true);")

            time.sleep(10)
