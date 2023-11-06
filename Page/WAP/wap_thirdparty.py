from selenium.webdriver.common.by import By
import time
from ..Common import Common

class Thirdparty(Common) :

    Casino = (By.CSS_SELECTOR,'div[class^="tabNavigation_icons"] div.flex-1:nth-child(2)')
    Game_Entrys = (By.CSS_SELECTOR,'button[class^="entryBlocks"]')

    def navigate_to_casino_page(self):
        return self.wait_for(self.Casino).click()    