import pytest
import allure,time
from Fixture.environment import *
from Page.WAP.wap_home import Home
from Page.PC.pc_profile import Profile
from Page.PC.pc_sport import Sport
from Page.PC.pc_thirdparty import Thirdparty
from Page.PC.pc_order import Order_Record
from Page.PC.pc_promotion import Promotion
from Page.CommonFunction import CommonFunction

@allure.feature("Platform Mine Page Test")
@pytest.mark.DB_used
@pytest.mark.usefixtures('get_screenshot_path')
@pytest.mark.usefixtures('get_wap_driver')

class TestBackendFunction:

    def test_setup(self, env_url, get_admin_user, get_user):
        print("TestPlatformMinePage: test_setup")
        func = CommonFunction(env_url)        
        ad_user, ad_pw, secret_key = get_admin_user
        account , password = get_user
        print(ad_user)
        admin_token = func.login_admin(ad_user, ad_pw, secret_key)
        func.set_bank_card_deposit()
        func.get_all_sms_settings()
        func.set_tiger_sms_status('off')
        func.get_sport_settings()
        print(func.sport_settings)
        func.set_sport_cashout_status(status='on')
        print(func.sport_settings)
        sms_code = func.get_sms_code(account)
        print(f'sms_code={sms_code}')
        func.get_merchant_setting()
        print(func.merchant_settings)
        func.get_transaction_status(func.Transaction_Type.DEPOSIT, '202311140a84c5a5148c')
        func.c2c_enable(False)
        print(func.get_transaction_status(func.Transaction_Type.DEPOSIT, '202311140a84c5a5148c'))
        print(func.get_transaction_status(func.Transaction_Type.WITHDRAW, '20231114141517883bdcf4fd0da94'))
        func.deposit_audit('202311140a84c5a5148c',func.Deposit_Status.CONFIRMED)
        func.withdraw_accepted('20231114141517883bdcf4fd0da94')
        func.c2c_enable(True)
    
    def test_logout(self):
        pass
    
