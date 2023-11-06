from selenium.webdriver.common.by import By
import time
from ..Common import Common

class Profile(Common):
    Avatar = (By.CSS_SELECTOR,'div[class^="lg:cursor-pointer"]')
    LogoutBtn = (By.CSS_SELECTOR,'div[class="flex justify-center"]')

    def navigate_to_profile_page(self):
        self.wait_for(self.Avatar).click()

    def logout(self):
        self.wait_for(self.LogoutBtn).click()
        time.sleep(1)