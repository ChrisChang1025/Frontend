from selenium.webdriver.common.by import By
import time
from ..Common import Common

class Home(Common):
    Index = (By.CSS_SELECTOR,'div[class^="tabNavigation_icons"] div.flex-1:nth-child(1)')
    LoginBtn = (By.CSS_SELECTOR,'button[class^="UnLogin_loginBtn"]')
    RegisterBtn = (By.CSS_SELECTOR,'button[class^="UnLogin_registerBtn"]')
    Cancel_ezpwd = (By.CSS_SELECTOR,'div[data-cid="CoreModal__Footer"] button:nth-child(2)')
    Pop_up1 = (By.CSS_SELECTOR,'#pop_close_dark')
    Pop_up2 = (By.CSS_SELECTOR,'path[fill="ivory"]')    
    User_balance = (By.CSS_SELECTOR,'div[class^="UserDetail_money"]')
    Loginpage_loginBtn1 = (By.CSS_SELECTOR,'div[style="opacity: 1;"] button[type="button"]')
    Account_textbox = (By.XPATH,'//input[@name="username"]')
    Password_textbox = (By.XPATH,'//input[@type="password"]')
    Loginpage_loginBtn2 = (By.CSS_SELECTOR,'button[type="submit"]')


    def navigate_to_home_page(self):
        self.wait_for(self.Index).click()

    def login(self, _username, _password):
        self.wait_for(self.LoginBtn).click()  #登入按鈕        
        self.wait_for(self.Loginpage_loginBtn1).click()  #登入
        self.wait_for(self.Account_textbox).send_keys(_username)  #輸入帳號
        self.wait_for(self.Password_textbox).send_keys(_password)  #輸入密碼        
        self.wait_for(self.Loginpage_loginBtn2).click()
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