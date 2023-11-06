from selenium.webdriver.common.by import By
import time
from ..Common import Common

class Profile(Common):
    My = (By.CSS_SELECTOR,'div[class^="tabNavigation_icons"] div.flex-1:nth-child(5)')
    LogoutBtn = (By.CSS_SELECTOR,'div[class^="flex justify-center"]')

    def navigate_to_profile_page(self):
        self.wait_for(self.My).click()

    def logout(self):
        self.wait_for(self.LogoutBtn).click()
        time.sleep(1)