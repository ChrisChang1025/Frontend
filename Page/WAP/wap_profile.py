import random
import string
from selenium.webdriver.common.by import By
import time
from ..Common import Common


class Profile(Common):
    # profile
    My = (By.CSS_SELECTOR, 'div[class^="tabNavigation_icons"] div.flex-1:nth-child(5)')
    LogoutBtn = (By.CSS_SELECTOR, 'div[class^="flex justify-center"]')
    HeaderLeftMsg = (By.CSS_SELECTOR, 'div[class^="pageHeader_left"] div.relative')
    MsgContent = (By.CSS_SELECTOR, 'div[class^="content_msgCard"]')
    MsgHeadRight = (By.CSS_SELECTOR, 'div[class^="pageHeader_right"]')
    MsgTabNotify = (By.CSS_SELECTOR, 'div[class^="tabListing_tabListing"] div:nth-child(1)')
    MsgTabAnnounce = (By.CSS_SELECTOR, 'div[class^="tabListing_tabListing"] div:nth-child(2)')
    MsgTabInbox = (By.CSS_SELECTOR, 'div[class^="tabListing_tabListing"] div:nth-child(3)')
    HeaderRightBtn = (By.CSS_SELECTOR, 'div[class^="pageHeader_right"] svg')
    CustServicePage = (By.CSS_SELECTOR, 'div[class^="VdPersonInfo_personalContent"]')
    PointExchange = (By.CSS_SELECTOR, 'div[class^="personInfo_exchange"]')
    PointPage = (By.CSS_SELECTOR, 'div[data-cid="MyBonus"]')

    # nav buttons
    Wallet = (By.CSS_SELECTOR, 'div[class^="personInfo_icon"] div.flex:nth-child(1)')
    Deposit = (By.CSS_SELECTOR, 'div[class^="personInfo_icon"] div.flex:nth-child(2)')
    VIPBtn = (By.CSS_SELECTOR, 'div[class^="personInfo_icon"] div.flex:nth-child(4)')
    VIPPage = (By.CSS_SELECTOR, 'div[data-cid="VipCenter"]')
    CardMng = (By.ID, 'M7')
    PersonalInfo = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(1) div.flex-wrap:nth-child(1) div:nth-child(1)')
    TransDetail = (By.ID, 'M16')
    MyFavoriate = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(1) div.flex-wrap:nth-child(3) div:nth-child(1)')
    FavoriteClose = (By.CSS_SELECTOR, 'div[class^="FavoriteHeader_close"]')
    CouponCenter = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(1) div.flex-wrap:nth-child(6) div:nth-child(1)')
    CouponPage = (By.CSS_SELECTOR, 'div[data-cid="CouponCenter"]')
    EventGift = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(1) div.flex-wrap:nth-child(7) div:nth-child(1)')
    EventGiftBanner = (By.CSS_SELECTOR, 'div[class="flex h-[50px]"] div.h-full')
    ShareEarnMoney = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(1) div.flex-wrap:nth-child(8) div:nth-child(1)')
    EarnMoneyPage = (By.CSS_SELECTOR, 'div[data-cid="EarnMoney"]')
    EarnClose = (By.CSS_SELECTOR, 'div[class^="dialogSheet_closeIcon"]')
    BizCopor = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(1) div.flex-wrap:nth-child(9) div:nth-child(1)')
    BizCoporPage = (By.CSS_SELECTOR, 'div[data-cid="FranchiseCooperation"]')
    AppDownload = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(1) div.flex-wrap:nth-child(10) div:nth-child(1)')
    AppDownloadBtn = (By.CSS_SELECTOR, 'div[data-cid="DownloadApp_Footer"] button')
    Username = (By.CSS_SELECTOR, 'div[class^="personInfo_info"] div div div:nth-child(2) div.text-base')
    GameSetting = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(2) div.flex-wrap:nth-child(1) div div.flex:nth-child(1)')
    GameSetPage = (By.CSS_SELECTOR, 'div[data-cid="GameSetting"]')
    GameSearch = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(2) div.flex-wrap:nth-child(3) div div.flex:nth-child(1)')
    CountryElm = (By.CSS_SELECTOR, 'div[class^="HeaderContent_box"]')
    GameSearchBack = (By.CSS_SELECTOR, 'div[class^="TopHeader_top"] div:nth-child(1) svg')
    GameTutorial = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(2) div.flex-wrap:nth-child(4) div div.flex:nth-child(1)')
    BetEmulate = (By.CSS_SELECTOR, 'div[data-cid="GameTutorial"] div.bg-white div.flex div:nth-child(1)')
    Tutorial = (By.CSS_SELECTOR, 'div[data-cid="GameTutorial"] div.bg-white div.flex div:nth-child(2)')
    TutorialBack = (By.CSS_SELECTOR, 'div[data-cid="GameTutorial"] div.bg-white div svg')
    PlayRule = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(2) div.flex-wrap:nth-child(5) div div.flex:nth-child(1)')
    RulePage = (By.CSS_SELECTOR, 'div[data-cid="GamePlan"]')
    WebAnchors = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(3) div.flex-wrap:nth-child(1) div div.flex:nth-child(1)')
    AnchorBackIndex = (By.CSS_SELECTOR, 'div[data-cid="BottomNavigation"] button:nth-child(1)')
    LangChange = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(4) div[class^="ripple_main"]:nth-child(1)')
    LangPage = (By.CSS_SELECTOR, 'div[data-cid="Language"]')
    Timezone = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(4) div[class^="ripple_main"]:nth-child(2)')
    TimePage = (By.CSS_SELECTOR, 'div[data-cid="TimezoneBlocks"]')
    CustService = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(5) div[class^="ripple_main"]:nth-child(1)')
    AboutUs = (By.CSS_SELECTOR, 'div[data-cid="Services"] div.bg-white:nth-child(5) div[class^="ripple_main"]:nth-child(2)')
    AboutUsPage = (By.CSS_SELECTOR, 'div[data-cid="AboutUs"]')

    # footer
    FooterDivElm = (By.CSS_SELECTOR, 'div[data-cid="Services"] div[class^="p-[16px]"]')
    PromPage = (By.CSS_SELECTOR, 'div[data-cid="PromotionDetail_Context"]')
    FooterGameSear = (By.CSS_SELECTOR, 'div[data-cid="Services"] div[class^="p-[16px]"]:nth-child(2) div.grid div:nth-child(2)')
    # footer - partnership
    LogoBackIndex = (By.CSS_SELECTOR, 'div[data-cid="Logo"]')
    PartnershipPage = (By.CSS_SELECTOR, 'div[data-cid="Partnership"]')
    # footer - TopAdSponsor
    TopAdSponPage = (By.CSS_SELECTOR, 'div[data-cid="TopAdSponsorship"]')
    # personalInfo
    BannerAcc = (By.CSS_SELECTOR, 'div[data-cid="banner"] div span')
    NoCompItem = (By.CSS_SELECTOR, 'div.list_notCompleted__SlyTP')
    SetPersonal = (By.CSS_SELECTOR, 'div[data-cid="accountMsg"] div:nth-child(1) div.relative:nth-child(2)')
    # personalInfo - edit personal data
    EditPersonalPage = (By.CSS_SELECTOR, 'div[data-cid="MineInfoEdit"]')
    EditPerNoItem = (By.CSS_SELECTOR, 'div.listItem_incomplete__x-fKB')
    SetName = (By.CSS_SELECTOR, 'div[class^="m-[10px]"]  div div:nth-child(5)')
    Name_Textbox = (By.XPATH, '//input[@name="name"]')
    NameSubmit = (By.CSS_SELECTOR, 'div.bg-white button.bg-primary')
    SetBirthday = (By.CSS_SELECTOR, 'div[class^="m-[10px]"]  div div:nth-child(9)')
    ConfirmBirth = (By.CSS_SELECTOR, 'div[data-rsbs-content="true"] div[class^="birthdaySelector"]:nth-child(3)')
    # personalInfo - set withdraw password
    SetWalPwdPage = (By.CSS_SELECTOR, 'div[data-cid="EditWithdrawalPassword"]')
    SetWalPwd = (By.CSS_SELECTOR, 'div[data-cid="accountMsg"] div:nth-child(1) div.relative:nth-child(6)')
    WalPwdInput = (By.CSS_SELECTOR, 'input:nth-child(1)')
    WalPwdSubmit = (By.CSS_SELECTOR, 'div.bg-white button.bg-primary')
    Canvas_frame = (By.CSS_SELECTOR, "canvas[class^='JigsawPuzzleValidation_canvas']")
    Drag_slider = (By.CSS_SELECTOR, "div[class^='JigsawPuzzleValidation_slider_']")
    # personalInfo - set phone number
    SetPhoneNo = (By.CSS_SELECTOR, 'div[data-cid="security"] div.bg-white div:nth-child(2) div.text-xs')
    PhoneNumber_Textbox = (By.XPATH, '//input[@name="phoneNumber"]')
    SendSMSBtn = (By.CSS_SELECTOR, 'form button.bg-primary')
    SMSCode_Textbox = (By.XPATH, '//input[@name="otpCode"]')
    SMSCodeSubmit = (By.CSS_SELECTOR, 'button.bg-primary:nth-child(4)')
    PrompErrorText = (By.CSS_SELECTOR, 'div[data-cid="CoreModal__Header"] div.text-xs')
    # transaction records
    RecordNum = (By.CSS_SELECTOR, 'div[class^="header"] span:nth-child(2)')
    AllRecord = (By.CSS_SELECTOR, 'div[class^="box-border"] div:nth-child(1)')
    DepositRec = (By.CSS_SELECTOR, 'div[class^="box-border"] div:nth-child(2)')
    WithdrawRec = (By.CSS_SELECTOR, 'div[class^="box-border"] div:nth-child(3)')
    NodataItem = (By.CSS_SELECTOR, 'div[class^="noItem_noData"]')
    HasDataItem = (By.CSS_SELECTOR, 'div[class^="list_list"]')
    DepOrderNo = (By.CSS_SELECTOR, 'div[class^="deposit_content"] div[class^="rowInfo_row"]:nth-child(1) div')
    WalOrderNo = (By.CSS_SELECTOR, 'div[class^="withdraw_content"] div[class^="rowInfo_row"]:nth-child(1) div')
    DepOrderProgs = (By.CSS_SELECTOR, 'div[data-cid="CircularProgressbar"] div svg text')
    CancelBtn = (By.CSS_SELECTOR, 'div[class^="flex items-center justify-between h-10"] button')
    CurFilterBtn = (By.CSS_SELECTOR, 'div[data-cid="CurrencyPicker"] svg')
    DatePickLeft = (By.CSS_SELECTOR, 'div[class^="header_info"] span:nth-child(1)')
    DatePickRight = (By.CSS_SELECTOR, 'div[class^="pageHeader_right"] button:nth-child(1)')
    DatePicker = (By.CSS_SELECTOR, 'div[data-cid="DatePickerPanel"]')
    CurPanel = (By.CSS_SELECTOR, 'div[data-rsbs-content="true"]')
    CancelCurPanel = (By.CSS_SELECTOR, 'div[data-rsbs-content="true"] div.bg-white:nth-child(1) div:nth-child(1)')
    FilterBtn = (By.CSS_SELECTOR, 'div[class^="pageHeader_right"] button:nth-child(2)')
    FilterStatus = (By.CSS_SELECTOR, 'div[class^="statusBar_status"]')
    StatusSuccess = (By.CSS_SELECTOR, 'div[class^="w-full h-[32px] flex flex-nowrap"] div:nth-child(3)')
    StatusSubmit = (By.CSS_SELECTOR, 'div[data-rsbs-content="true"] button.bg-primary span')
    # into add bankcard info page
    AddCardBtn = (By.CSS_SELECTOR, 'div[data-cid="AddBankCardItem"]')
    AddCardPop = (By.CSS_SELECTOR, 'div[data-cid="CoreModal__Footer"] button.inline-flex:nth-child(1)')
    CurrencyBtn = (By.CSS_SELECTOR, 'div[class="cursor-pointer relative"]')
    CurrencyIcon = (By.CSS_SELECTOR, 'div[data-cid="currencyIconItem"]')
    BankBtn = (By.CSS_SELECTOR, 'div[class="relative"]')
    BankList = (By.CSS_SELECTOR, 'div[class="max-h-[80vh] overflow-y-scroll"] div.flex:nth-child(1)')
    CardNo_Textbox = (By.XPATH, '//input[@name="cardNo"]')
    CityChoose = (By.CSS_SELECTOR, 'div[data-cid="MultiPickerPopup"] div.flex:nth-child(1)')
    CitySelected = (By.CSS_SELECTOR, 'div[class="rmc-picker-popup-header"] div.rmc-picker-popup-item:nth-child(3)')
    AddCardSubmitBtn = (By.CSS_SELECTOR, 'div[data-cid="MyBankCard__AddBankCardForm"] button:nth-child(1)')
    SuccessOk = (By.CSS_SELECTOR, 'div[data-cid="CoreModal__Footer"] button.inline-flex:nth-child(1)')
    CardItem = (By.CSS_SELECTOR, 'div[data-cid="BankcardItem"]')
    # card mng page
    CardMngEdit = (By.CSS_SELECTOR, 'div[class^="pageHeader_right"]')
    CardDelBtn = (By.CSS_SELECTOR, 'div[data-cid="BankcardItem"] div:nth-child(3)')
    CardMngBack = (By.CSS_SELECTOR, 'div[class^="pageHeader_left"]')
    # wallet mng page
    WalletDepBtn = (By.CSS_SELECTOR, 'div[class^="flex justify-between"] div:nth-child(1)')
    WalletWalBtn = (By.CSS_SELECTOR, 'div[class^="flex justify-between"] div:nth-child(2)')
    WalletInfo = (By.CSS_SELECTOR, 'div[data-cid="WalletInfo"]')
    AddCurrency = (By.CSS_SELECTOR, 'div[data-cid="WalletList"] div.mt-5:nth-child(3)')
    Add_firstCurrency = (By.CSS_SELECTOR, 'div[class="flex flex-col space-y-10"] div:nth-child(1) svg:nth-child(1)')
    CurrencyName = (By.CSS_SELECTOR, 'span[class="text-[#333333] text-xs font-semibold"]')
    CurrencyEdit = (By.CSS_SELECTOR, 'div[data-cid="WalletList"] svg')
    DeleteCur = (By.CSS_SELECTOR, 'div[data-rbd-droppable-id="currenciesDroppable"] div:nth-child(5) div:nth-child(1) div:nth-child(1) svg')
    DoneBtn = (By.CSS_SELECTOR, 'div[class^="pageHeader_right"]')
    MyCurrency = (By.CSS_SELECTOR, 'div[class="ml-7"] div:nth-child(1) div.flex:nth-child(1) span')
    SwitchCur = (By.CSS_SELECTOR, 'div[class="flex flex-col"] div:nth-child(3) div:nth-child(1) div span:nth-child(1)')
    SwitchCurBtn = (By.CSS_SELECTOR, 'div[class="flex flex-col"] div:nth-child(3) div:nth-child(2) button')
    WalletBalance = (By.CSS_SELECTOR, 'div[class="ml-7"] div:nth-child(1) div:nth-child(2) span')
    # crypto wallet
    CryptoCurWallet = (By.CSS_SELECTOR, 'div[class="xl:flex xl:justify-around"] div:nth-child(2) div:nth-child(3)')
    CryptoHeader = (By.CSS_SELECTOR, 'div[data-cid="MyCryptoAddress"]')
    AddCryptoCurBtn = (By.CSS_SELECTOR, 'div[data-cid="AddCryptoAddressItem"] div svg:nth-child(1)')
    ChooseCryptoCur = (By.CSS_SELECTOR, 'div[class="relative"] div[class^="cursor"]')
    CurItem = (By.CSS_SELECTOR, 'div[data-cid="CryptoAddressItem"]')
    CryptoCurItem = (By.CSS_SELECTOR, 'div[data-cid="currencyIconItem"]')
    Alias_Textbox = (By.XPATH, '//input[@name="alias"]')
    CryptoAddr_Textbox = (By.XPATH, '//input[@name="address"]')
    AddCryptoSubmitBtn = (By.CSS_SELECTOR, 'div[data-cid="AddCryptoAddressForm"] button:nth-child(1)')
    Del_cryptoCur = (By.CSS_SELECTOR, 'div[data-cid="CryptoAddressItem"] div:nth-child(2)')
    CryptoCur = ['BTC', 'ETH', 'USDT', 'DOGE', 'BCH', 'LTC', 'DASH', 'ETC', 'AAVE', 'DAI', 'UNI']
    # apply deposit
    FirstDepWay = (By.CSS_SELECTOR, 'div[data-cid="Deposit"] div:nth-child(2) div div div div span')
    DepositAmount = (By.XPATH, '//input[@name="amount"]')
    DepositSubmit = (By.CSS_SELECTOR, 'div[class^="wapFloatingButton_container"] button')
    DepositName = (By.XPATH, '//input[@name="depositorName"]')
    DepositToRecord = (By.CSS_SELECTOR, 'div[data-cid="CoreModal__Footer"] button.inline-flex:nth-child(2)')
    # apply withdraw
    WithdrawCurPage = (By.CSS_SELECTOR, 'div[data-cid="Withdrawal_Entrance"]')
    WalFirstCur = (By.CSS_SELECTOR, 'div[data-cid="Withdrawal_Entrance_Currency"] div:nth-child(2) span')
    WalAmount = (By.XPATH, '//input[@name="amount"]')
    WalSubmitBtn = (By.CSS_SELECTOR, 'button[class^="items-center justify-center"]')
    WalPwdPanel = (By.ID, 'CipherInput')
    WalConfirmBtn = (By.CSS_SELECTOR, 'div[class="flex flex-col"] button:nth-child(1)')
    WalToRecord = (By.CSS_SELECTOR, 'div[data-cid="CoreModal__Footer"] button.inline-flex:nth-child(1)')

    def navigate_to_profile_page(self):
        self.wait_for(self.My).click()

    def logout(self):
        self.wait_for(self.LogoutBtn).click()
        time.sleep(1)

    def navigate_to_wallet_page(self):
        self.wait_for(self.Wallet).click()
        time.sleep(1)

    def navigate_to_cardmng_page(self):
        self.wait_for(self.CardMng).click()
        time.sleep(1)

    def add_bankCard(self):
        self.wait_for(self.AddCardBtn).click()
        self.wait_for(self.AddCardPop).click()
        # bankCard info
        # currency
        self.wait_for(self.CurrencyBtn).click()
        self.wait_for(self.CurrencyIcon).click()
        # bank
        self.wait_for(self.BankBtn).click()
        self.wait_for(self.BankList).click()
        # cardNo
        self.wait_for(self.CardNo_Textbox).send_keys(f"1{str(random.randint(0, 9999999999)).zfill(10)}")
        # city
        self.clickElementifExist(self.CityChoose)
        self.clickElementifExist(self.CitySelected)
        # submit
        self.wait_for(self.AddCardSubmitBtn).click()
        # success
        self.wait_for(self.SuccessOk).click()
        time.sleep(1)

    def delete_bankCard(self):
        self.wait_for(self.CardMngEdit).click()
        self.wait_for(self.CardDelBtn).click()
        self.wait_for(self.SuccessOk).click()
        self.wait_for(self.SuccessOk).click()
        time.sleep(1)

    def add_wallet_currency(self):
        self.wait_for(self.AddCurrency).click()
        self.wait_for(self.Add_firstCurrency).click()
        self.wait_for(self.CardMngBack).click()
        time.sleep(1)

    def delete_wallet_currency(self):
        self.wait_for(self.CurrencyEdit).click()
        self.wait_for(self.DeleteCur).click()
        self.wait_for(self.DoneBtn).click()
        time.sleep(1)

    def switch_wallet_currency(self):
        self.wait_for(self.SwitchCurBtn).click()
        self.wait_for(self.SuccessOk).click()
        time.sleep(1)

    def navigate_to_cryptoWallet_page(self):
        myCur = self.getElementText(self.MyCurrency)
        if myCur not in self.CryptoCur:
            for i in range(2, 11):
                elm = (By.CSS_SELECTOR, f'div[class="flex flex-col"] div:nth-child({i}) div:nth-child(1) div span:nth-child(1)')
                elmBtn = (By.CSS_SELECTOR, f'div[class="flex flex-col"] div:nth-child({i}) div:nth-child(2) button')
                targetCur = self.getElementText(elm)
                if targetCur in self.CryptoCur:
                    self.wait_for(elmBtn).click()
                    self.wait_for(self.SuccessOk).click()
                    break
                else:
                    pass
        time.sleep(1)
        self.wait_for(self.CryptoCurWallet).click()
        time.sleep(1)

    def add_cryptocurrency_wallet(self):
        self.wait_for(self.AddCryptoCurBtn).click()
        self.wait_for(self.ChooseCryptoCur).click()
        self.wait_for(self.CryptoCurItem).click()
        self.wait_for(self.Alias_Textbox).send_keys(''.join(random.choices(string.ascii_lowercase, k=4)))
        self.wait_for(self.CryptoAddr_Textbox).send_keys(''.join(random.choices(string.ascii_lowercase + string.digits, k=6)))
        self.wait_for(self.AddCryptoSubmitBtn).click()
        self.wait_for(self.SuccessOk).click()
        time.sleep(1)

    def delete_cryptocurrency_wallet(self):
        self.wait_for(self.CardMngEdit).click()
        self.wait_for(self.Del_cryptoCur).click()
        self.wait_for(self.SuccessOk).click()
        self.wait_for(self.SuccessOk).click()
        time.sleep(1)

    def navigate_to_trans_page(self):
        self.wait_for(self.TransDetail).click()
        time.sleep(1)

    def navigate_to_trans_allRecord_page(self):
        self.wait_for(self.AllRecord).click()
        time.sleep(1)

    def navigate_to_trans_depositRec_page(self):
        self.wait_for(self.DepositRec).click()
        time.sleep(1)

    def navigate_to_trans_withdrawRec_page(self):
        self.wait_for(self.WithdrawRec).click()
        time.sleep(1)

    def apply_deposit(self, depAmount):
        # swith main currency to CNY
        self.wait_for(self.Wallet).click()
        time.sleep(1)
        myCur = self.getElementText(self.MyCurrency)
        curCount = self.getElementCount(self.CurrencyName)
        if myCur != 'CNY':
            for i in range(2, int(curCount - 1)):
                elm = (By.CSS_SELECTOR, f'div[class="flex flex-col"] div:nth-child({i}) div:nth-child(1) div span:nth-child(1)')
                elmBtn = (By.CSS_SELECTOR, f'div[class="flex flex-col"] div:nth-child({i}) div:nth-child(2) button')
                targetCur = self.getElementText(elm)
                if targetCur == 'CNY':
                    self.wait_for(elmBtn).click()
                    self.wait_for(self.SuccessOk).click()
                    time.sleep(1)
                    break
                else:
                    pass
        assert self.getElementText(self.MyCurrency) == 'CNY'
        assert self.checkElementExists(self.WalletInfo) == True
        balance = self.getElementText(self.WalletBalance)
        self.wait_for(self.WalletDepBtn).click()
        time.sleep(1)
        # apply bankcard deposit
        self.wait_for(self.FirstDepWay).click()
        self.wait_for(self.DepositAmount).send_keys(depAmount)
        self.wait_for(self.DepositSubmit).click()
        self.wait_for(self.DepositName).send_keys(''.join(random.choices(string.ascii_lowercase, k=4)))
        self.wait_for(self.DepositSubmit).click()
        self.wait_for(self.DepositToRecord).click()
        time.sleep(1)
        return balance

    def click_deposit_withdraw_cancel(self):
        self.wait_for(self.CancelBtn).click()
        self.wait_for(self.SuccessOk).click()
        time.sleep(1)

    def apply_withdraw(self, walAmount):
        # swith main currency to CNY
        self.wait_for(self.Wallet).click()
        time.sleep(1)
        myCur = self.getElementText(self.MyCurrency)
        curCount = self.getElementCount(self.CurrencyName)
        if myCur != 'CNY':
            for i in range(2, int(curCount - 1)):
                elm = (By.CSS_SELECTOR, f'div[class="flex flex-col"] div:nth-child({i}) div:nth-child(1) div span:nth-child(1)')
                elmBtn = (By.CSS_SELECTOR, f'div[class="flex flex-col"] div:nth-child({i}) div:nth-child(2) button')
                targetCur = self.getElementText(elm)
                if targetCur == 'CNY':
                    self.wait_for(elmBtn).click()
                    self.wait_for(self.SuccessOk).click()
                    time.sleep(1)
                    break
                else:
                    pass
        assert self.getElementText(self.MyCurrency) == 'CNY'
        assert self.checkElementExists(self.WalletInfo) == True
        balance = self.getElementText(self.WalletBalance)
        self.wait_for(self.WalletWalBtn).click()
        time.sleep(1)
        assert self.getElementText(self.WalFirstCur) == 'CNY'
        self.wait_for(self.WalFirstCur).click()
        self.wait_for(self.WalAmount).send_keys(walAmount)
        self.wait_for(self.WalSubmitBtn).click()
        self.wait_for(self.WalPwdPanel).send_keys('123456')  # payment password
        self.wait_for(self.WalConfirmBtn).click()
        time.sleep(2)
        self.wait_for(self.WalToRecord).click()
        time.sleep(1)
        return balance

    def trans_page_filter_success(self):
        self.wait_for(self.FilterBtn).click()
        self.wait_for(self.StatusSuccess).click()
        self.wait_for(self.StatusSubmit).click()
        time.sleep(1)

    def click_trans_func_buttons(self):
        self.wait_for(self.CurFilterBtn).click()
        time.sleep(1)
        assert self.checkElementExists(self.CurPanel) == True
        self.wait_for(self.CancelCurPanel).click()
        self.wait_for(self.DatePickLeft).click()
        assert self.checkElementExists(self.DatePicker) == True
        self.wait_for(self.SuccessOk).click()
        self.wait_for(self.DatePickRight).click()
        assert self.checkElementExists(self.DatePicker) == True
        self.wait_for(self.SuccessOk).click()
        self.wait_for(self.FilterBtn).click()
        count = self.getElementCount(self.FilterStatus)
        assert count == 5
        self.wait_for(self.StatusSubmit).click()
        time.sleep(1)

    def navigate_to_personalInfo_page(self):
        self.wait_for(self.PersonalInfo).click()
        time.sleep(1)

    def complete_personal_data(self):
        self.wait_for(self.SetPersonal).click()
        self.wait_for(self.EditPersonalPage)
        assert self.checkElementExists(self.EditPersonalPage) == True
        self.wait_for(self.SetName).click()
        self.wait_for(self.Name_Textbox).send_keys(''.join(random.choices(string.ascii_lowercase, k=4)))
        self.wait_for(self.NameSubmit).click()
        self.wait_for(self.SuccessOk).click()
        self.wait_for(self.SetBirthday).click()
        self.wait_for(self.ConfirmBirth).click()
        self.wait_for(self.SuccessOk).click()
        self.wait_for(self.CardMngBack).click()
        time.sleep(1)

    def complete_withdraw_password(self):
        self.wait_for(self.SetWalPwd).click()
        self.wait_for(self.SetWalPwdPage)
        assert self.checkElementExists(self.SetWalPwdPage) == True
        self.wait_for(self.WalPwdInput).send_keys('123456')
        self.wait_for(self.WalPwdSubmit).click()
        self.wait_for(self.WalPwdInput).send_keys('123456')
        self.wait_for(self.WalPwdSubmit).click()
        time.sleep(2)
        frame = self.find(self.Canvas_frame)
        style = frame.get_attribute("style")
        self.drag_and_drop(self.Drag_slider, int(style[style.index('left:')+5:style.index('px')]), 3)
        time.sleep(2)
        self.wait_for(self.SuccessOk).click()

    def set_phoneNumber_getSMSCode(self):
        self.wait_for(self.SetPhoneNo).click()
        self.wait_for(self.PhoneNumber_Textbox).send_keys(f"13{str(random.randint(0, 999999999)).zfill(9)}")
        self.wait_for(self.SendSMSBtn).click()
        time.sleep(2)
        frame = self.find(self.Canvas_frame)
        style = frame.get_attribute("style")
        self.drag_and_drop(self.Drag_slider, int(style[style.index('left:')+5:style.index('px')]), 3)
        time.sleep(2)

    def set_phoneNumber_inputSMS(self, otpCode):
        self.wait_for(self.SMSCode_Textbox).send_keys(otpCode)
        self.wait_for(self.SMSCodeSubmit).click()
        time.sleep(2)
        frame = self.find(self.Canvas_frame)
        style = frame.get_attribute("style")
        self.drag_and_drop(self.Drag_slider, int(style[style.index('left:')+5:style.index('px')]), 3)
        time.sleep(2)
        self.wait_for(self.SuccessOk).click()
        time.sleep(1)

    def navigate_to_eventGift_page(self):
        self.wait_for(self.EventGift).click()
        time.sleep(1)

    def click_MyPage_navLinks(self):
        self.wait_for(self.HeaderLeftMsg).click()
        for elem in [self.MsgTabNotify, self.MsgTabAnnounce, self.MsgTabInbox]:
            self.wait_for(elem).click()
        self.wait_for(self.MsgHeadRight).click()
        self.wait_for(self.MsgHeadRight).click()
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.HeaderRightBtn).click()
        self.wait_for(self.CustServicePage)
        assert self.checkElementExists(self.CustServicePage) == True
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.PointExchange).click()
        self.wait_for(self.PointPage)
        assert self.checkElementExists(self.PointPage) == True
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.VIPBtn).click()
        self.wait_for(self.VIPPage)
        assert self.checkElementExists(self.VIPPage) == True
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.MyFavoriate).click()
        self.wait_for(self.FavoriteClose).click()

        self.wait_for(self.CouponCenter).click()
        self.wait_for(self.CouponPage)
        assert self.checkElementExists(self.CouponPage) == True
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.ShareEarnMoney).click()
        time.sleep(1)
        self.wait_for(self.EarnClose).click()
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.BizCopor).click()
        self.wait_for(self.BizCoporPage)
        assert self.checkElementExists(self.BizCoporPage) == True
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.AppDownload).click()
        self.wait_for(self.AppDownloadBtn)
        assert self.checkElementExists(self.AppDownloadBtn) == True
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.GameSetting).click()
        self.wait_for(self.GameSetPage)
        assert self.checkElementExists(self.GameSetPage) == True
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.GameSearch).click()
        self.wait_for(self.CountryElm)
        assert self.checkElementExists(self.CountryElm) == True
        self.wait_for(self.GameSearchBack).click()

        self.wait_for(self.GameTutorial).click()
        self.wait_for(self.BetEmulate).click()
        self.wait_for(self.Tutorial).click()
        self.wait_for(self.TutorialBack).click()

        self.wait_for(self.PlayRule).click()
        self.wait_for(self.RulePage)
        assert self.checkElementExists(self.RulePage) == True
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.WebAnchors).click()
        self.wait_for(self.AnchorBackIndex).click()
        self.wait_for(self.My).click()

        self.wait_for(self.LangChange).click()
        self.wait_for(self.LangPage)
        assert self.checkElementExists(self.LangPage) == True
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.Timezone).click()
        self.wait_for(self.TimePage)
        assert self.checkElementExists(self.TimePage) == True
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.CustService).click()
        self.wait_for(self.CustServicePage)
        assert self.checkElementExists(self.CustServicePage) == True
        self.wait_for(self.CardMngBack).click()

        self.wait_for(self.AboutUs).click()
        self.wait_for(self.AboutUsPage)
        assert self.checkElementExists(self.AboutUsPage) == True
        time.sleep(1)
        self.screenshot(f"{self._screenshot_path}AboutUs.png")
        self.wait_for(self.CardMngBack).click()
        time.sleep(1)

    def click_profile_footer_links(self):
        time.sleep(1)
        footerDivNum = self.getElementCount(self.FooterDivElm)      # 取得 footer div 數量
        # 1 特別優惠
        FooterEventElm = 'div[data-cid="Services"] div[class^="p-[16px]"]:nth-child(1) div.grid div'
        eventCount = self.getElementCount((By.CSS_SELECTOR, FooterEventElm))
        for i in range(1, eventCount + 1):
            self.wait_for((By.CSS_SELECTOR, f"{FooterEventElm}:nth-child({i})")).click()
            time.sleep(1)
            if self.checkElementExists(self.PromPage):
                self.wait_for(self.CardMngBack).click()
                self.wait_for(self.CardMngBack).click()
            else:
                assert self.checkElementExists(self.EventGiftBanner) == True
                self.wait_for(self.CardMngBack).click()

        # 2 比分與賽果
        self.wait_for(self.FooterGameSear).click()  # 賽果查詢
        self.wait_for(self.CountryElm)
        assert self.checkElementExists(self.CountryElm) == True
        self.wait_for(self.GameSearchBack).click()

        # 4, 5 官方合作伙伴, 廣告贊助球隊
        if footerDivNum > 5:
            self.click_footer_partnership(footerDivNum)

        # 6 Helps
        FooterCustService = f'div[data-cid="Services"] div[class^="p-[16px]"]:nth-child({footerDivNum-1}) div.grid div:nth-child(1)'
        FooterPlayRule = f'div[data-cid="Services"] div[class^="p-[16px]"]:nth-child({footerDivNum-1}) div.grid div:nth-child(2)'
        FooterAboutUs = f'div[data-cid="Services"] div[class^="p-[16px]"]:nth-child({footerDivNum-1}) div.grid div:nth-child(3)'
        self.wait_for((By.CSS_SELECTOR, FooterCustService)).click()
        self.wait_for(self.CustServicePage)
        assert self.checkElementExists(self.CustServicePage) == True
        self.wait_for(self.CardMngBack).click()
        self.wait_for((By.CSS_SELECTOR, FooterPlayRule)).click()
        self.wait_for(self.RulePage)
        assert self.checkElementExists(self.RulePage) == True
        self.wait_for(self.CardMngBack).click()
        self.wait_for((By.CSS_SELECTOR, FooterAboutUs)).click()
        self.wait_for(self.AboutUsPage)
        assert self.checkElementExists(self.AboutUsPage) == True
        self.wait_for(self.CardMngBack).click()

    def click_footer_partnership(self, footerDivNum):
        FooterPartnerElm = None
        FooterAdSponElm = None
        if footerDivNum == 6:
            FooterPartnerElm = f'div[data-cid="Services"] div[class^="p-[16px]"]:nth-child({footerDivNum - 2}) div.flex div'
            FooterAdSponElm = f'div[data-cid="Services"] div[class^="p-[16px]"]:nth-child({footerDivNum - 2}) div.flex'
        elif footerDivNum == 7:
            FooterPartnerElm = f'div[data-cid="Services"] div[class^="p-[16px]"]:nth-child({footerDivNum - 3}) div.flex div'
            FooterAdSponElm = f'div[data-cid="Services"] div[class^="p-[16px]"]:nth-child({footerDivNum - 2}) div.flex'

        # partnership
        partnerCount = self.getElementCount((By.CSS_SELECTOR, FooterPartnerElm))
        if partnerCount > 0:
            for i in range(1, partnerCount + 1):
                self.wait_for((By.CSS_SELECTOR, f"{FooterPartnerElm}:nth-child({i}) img")).click()
                time.sleep(1)
                assert self.checkElementExists(self.PartnershipPage) == True
                time.sleep(1)
                self.screenshot(f"{self._screenshot_path}PartnerShip_{i}.png")
                self.wait_for(self.CardMngBack).click()
                if not self.checkElementExists(self.PersonalInfo):
                    self.wait_for(self.LogoBackIndex).click()
                    self.wait_for(self.My).click()
        # Ad sponsor
        adsponCount = self.getElementCount((By.CSS_SELECTOR, FooterAdSponElm))
        if adsponCount > 0:
            for i in range(1, adsponCount + 1):
                self.wait_for((By.CSS_SELECTOR, f"{FooterAdSponElm}:nth-child({i}) img")).click()
                time.sleep(1)
                assert self.checkElementExists(self.TopAdSponPage) == True
                time.sleep(1)
                self.screenshot(f"{self._screenshot_path}TopAdSponsor_{i}.png")
                self.wait_for(self.CardMngBack).click()
                if not self.checkElementExists(self.PersonalInfo):
                    self.wait_for(self.LogoBackIndex).click()
                    self.wait_for(self.My).click()
        time.sleep(1)
