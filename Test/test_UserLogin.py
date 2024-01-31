import time

import pytest
from selenium.webdriver.common.by import By

from PageObject.UserLogin import LoginWithCredentials
from Utilities.BaseClass import BaseClass


class TestUserLogin(BaseClass):

    @pytest.mark.regression
    def test_UserLogin(self):
        LoginWithCredentials.clickBlinkText(self)
        self.managebrowsertab(1)
        mailText = self.driver.find_element(By.XPATH, "//a[@href='mailto:mentor@rahulshettyacademy.com']").text
        print(mailText)
        self.managebrowsertab(0)
        LoginWithCredentials.login(self, "test@test.com", "12345")
        errorText = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']/strong").text
        print(errorText)

        # LoginWithCredentials.login(self, "contentadmin", "Ctadmin@1234")
        # self.getLogger().info("User is logged in sucessfully")

    @pytest.mark.smoke
    def test_UserLoginUsing_Constructor(self):
        login_Process = LoginWithCredentials(self.driver)
        login_Process.login("contentadmin", "Ctadmin@12345")
        self.verifyelementpresent("//h2[text()='Content in review']")
        # //h2[text()='Content in review']
        actualurl = self.driver.current_url
        assert "https://cms-dev.monotype.com/user/8661/moderation/dashboard?check_logged_in=1" == actualurl
