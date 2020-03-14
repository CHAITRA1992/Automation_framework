from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import allure

class Test_Login():  #scope is only for one time pass an also class
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/Shilpa/PycharmProjects/Automation_framework/drivers/chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test completed")

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "abc"

        except AssertionError as error:
            print("assertion error occured")
            print(error)

            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise

        except:
            print("There was an exception")
            raise
        else:
            print("No exceptions occured")

        finally:
            print("I am inside finally block")


      # raise will show assertion error
      #driver.find_element_by_id("welcome").click()
      #driver.find_element_by_link_text("Logout").click()

    # terminal commands
    # python -m pytest -alluredir=reports/allure-reports
    # allure serve reports/allure-reports