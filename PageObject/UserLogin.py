from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class LoginWithCredentials(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    textboxEmail = "//input[@id='username']"
    textboxPassword = "//input[@id='password']"
    buttonLogin = "//input[@id='signInBtn']"
    errorText = "//div[@class='alert alert-danger col-md-12']"
    blinkingText = "//a[text()='Free Access to InterviewQues/ResumeAssistance/Material']"

    def clickBlinkText(self):
        self.verifyelementpresent(LoginWithCredentials.blinkingText)
        self.driver.find_element(By.XPATH, LoginWithCredentials.blinkingText).click()

    def enterData_UserName(self, username):
        return self.driver.find_element(By.XPATH, LoginWithCredentials.textboxEmail).send_keys(username)

    def enterData_Password(self, password):
        return self.driver.find_element(By.XPATH, LoginWithCredentials.textboxPassword).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, LoginWithCredentials.buttonLogin).click()

    def errorText(self):
        errorText = self.driver.find_element(By.XPATH, LoginWithCredentials.errorText).text
        print(errorText)

    def login(self, username, password):
        self.driver.find_element(By.XPATH, LoginWithCredentials.textboxEmail).send_keys(username)
        self.driver.find_element(By.XPATH, LoginWithCredentials.textboxPassword).send_keys(password)
        self.driver.find_element(By.XPATH, LoginWithCredentials.buttonLogin).click()
