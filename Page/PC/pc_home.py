from selenium.webdriver.common.by import By
import time
from ..Common import Common

class Home(Common):
    Logo = (By.CSS_SELECTOR,'img[alt="primary_logo"]')
    LoginBtn = (By.CSS_SELECTOR,'div[class^="flex space"] button:first-child')
    RegisterBtn = (By.CSS_SELECTOR,'div[class^="flex space"] button:nth-child(2)')
    Cancel_ezpwd = (By.CSS_SELECTOR,'div[data-cid="CoreModal__Footer"] button:nth-child(2)')
    Pop_up1 = (By.CSS_SELECTOR,'#pop_close_dark')
    Pop_up2 = (By.CSS_SELECTOR,'path[fill="ivory"]')    
    User_balance = (By.CSS_SELECTOR,'div[class^="userBalance"]')
    Loginpage_loginBtn = (By.XPATH,"//button[1]")
    Account_textbox = (By.XPATH,'//input[@name="username"]')
    Password_textbox = (By.XPATH,'//input[@type="password"]')

    def navigate_to_home_page(self):
        self.wait_for(self.Logo).click()

    def login(self, _username, _password):
        self.wait_for(self.LoginBtn).click()  #登入按鈕        
        self.wait_for(self.Loginpage_loginBtn).click()  #登入
        self.wait_for(self.Account_textbox).send_keys(_username)  #輸入帳號
        self.wait_for(self.Password_textbox).send_keys(_password)  #輸入密碼        
        self.wait_for(self.Loginpage_loginBtn).click()
        time.sleep(3)
    
    def close_popup(self):
        self.clickElementifExist(self.Cancel_ezpwd)
        time.sleep(2)
        while self.checkElementExists(self.Pop_up1) or self.checkElementExists(self.Pop_up2):
                if self.checkElementExists(self.Pop_up1):
                    self.find(self.Pop_up1).click()
                else :
                    self.find(self.Pop_up2).click()            
                time.sleep(2)