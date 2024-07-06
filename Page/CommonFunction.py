from selenium.webdriver.common.by import By
import requests
from base64 import b64encode, b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import threading, time
import pyotp, pymysql
from enum import Enum
from datetime import datetime, timezone, timedelta

Pk1 = 'MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAIdBzuXIwtMAsuaBgGYrxXf3DMEKB1jvsZHmMpCZHkl1iMrv1ktWZ94AHA0Qxq/GQ0GHOf6hYJgqCSLybgANfRdBjxC6pj9DbWbWNUfopdvxUhJ2z1E1BDNdZZOh9LAVEyF92sH0GThWSxQykVP+SfUBCEVaoURrC2HYSEZk56S3AgMBAAECgYBzO1OjXKjuzxebXhUf9oajr+xDweGEmaD0pePKYUj2WJYUHsS5JoITFpDPaM19DzJZb3WvQ5lhyd5C0bt5fARnNOL65U5GHjMwZCYrgY7fnDE5d//r6Eb6QNPvpiK8RJ+R8bcD8OI2lN/BbM55bWGmwCJv1/YWYz4vkyYOZ0+lsQJBAPRWnP5/X3TG3i+Q5m8xYA0Oxn0xslXB64F5W1aATRzXirdzhTgeEFbBWhT49XpMA1xncvrXs2PwE8cjwHaNYiMCQQCNtmmqOm1rALychmV0mjHpfGjKd1YK8OA2BHtMxfrRvNjk72LrNxpuQ8Ib+1Jwdsk9qVvzULaEmJUQgKEMvepdAkActhTKnwMDgN7Y7gj15fJodmUCjxVqmFfpJe6Csp7dFcLaHbv4xSecWioQrtSBo279q7ZKHZCZ3LsmOmBCTgjLAkBhBGf0nYl5PwjhU/UzTbkr8vs+2VIzrVKiSJEtL0EWw+XtXaHoDFJw+Lx0MavvyLLfHwoPWsuJnXg30wfu1DoVAkBlDUUVnjMnHoi8smEiL6yqp+bDJJ4tHnlInNhiDPT19uBpmLa1CGSNr4joxjmccmdeprtSa0tXRBa8s7WVZxVw'
Pk2 = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCHQc7lyMLTALLmgYBmK8V39wzBCgdY77GR5jKQmR5JdYjK79ZLVmfeABwNEMavxkNBhzn+oWCYKgki8m4ADX0XQY8QuqY/Q21m1jVH6KXb8VISds9RNQQzXWWTofSwFRMhfdrB9Bk4VksUMpFT/kn1AQhFWqFEawth2EhGZOektwIDAQAB'

private_key = '-----BEGIN RSA PRIVATE KEY-----\n{}\n-----END RSA PRIVATE KEY-----'.format(Pk1)
public_key = '-----BEGIN PUBLIC KEY-----\n{}\n-----END PUBLIC KEY-----'.format(Pk2)

class CommonFunction():

    class Transaction_Type(Enum):
        DEPOSIT = 1
        WITHDRAW = 2
    
    class Deposit_Status(Enum):
        DENIED = -1
        PROCESSING = 0
        LOCKED = 1
        CONFIRMED = 2
        CANCELED = 3
    
    class Live_Sport_Limit(Enum): #0: 不限制, 1: 登入後 2: 生涯存款總額, 11: Vip-1, 12: Vip-2, 13: Vip-3, 14: Vip-4, 15: Vip-5, 16: Vip-6, 17: Vip-7, 18: Vip-8, 19: Vip-9, 20: Vip-10
        NO_LIMIT = 0
        AFTER_LOGIN = 1
        DEPOSIT_TOTAL = 2
        VIP1 = 11
        VIP2 = 12
        VIP3 = 13
        VIP4 = 14
        VIP5 = 15
        VIP6 = 16
        VIP7 = 17
        VIP8 = 18
        VIP9 = 19
        VIP10 = 20

    def __init__(self, env_conf) -> None:
        self.api_url = env_conf['api_url']
        self.admin_url = env_conf['admin_url']
        self.url = env_conf['url']
        self.tiger_db_host = env_conf['tiger_db_host']
        self.tiger_db_user = env_conf['tiger_db_user']
        self.tiger_db_pw = env_conf['tiger_db_pw']         
        self.env = env_conf['env'] 
        self.vend = env_conf['vend']
        self.vd_code = env_conf['vd_code']
        self.admin_token = None
        self.headers = {
            "Content-Type": "application/json",
            "referer": self.admin_url,
            "time-zone": "GMT-0400",
            "Currency":"CNY",
            "Accept-Language" : "zh-CN"
        }
        print(f'InitialSetup: {env_conf}')


    def encrypt(self, text):
        s = str.encode(text)
        rsa_public_key = RSA.importKey(public_key)
        rsa_public_key = PKCS1_v1_5.new(rsa_public_key)
        encrypted_text = rsa_public_key.encrypt(s)
        encrypted_text = b64encode(encrypted_text)
        return encrypted_text
    
    def login_admin(self, ad_account, ad_password, secret):
        print('login_admin')
        auth = ""
        if secret != '':
            auth = pyotp.TOTP(secret).now()
        
        payload = {
            "account" : ad_account,
            "auth": auth,
            "password" : self.encrypt(ad_password).decode("utf-8"),
        }
        
        path = f'{self.api_url}/platform/admin/token'
        r = requests.request("POST", path, headers=self.headers, json=payload)
        if r.status_code == 200:
            response = r.json()
            self.admin_token = response['data']['token']
            self.headers.update({"authorization": "Bearer " + str(self.admin_token)})
            return response['data']['token']
        else: 
            return ''

    def get_all_sms_settings(self):
        path = f'{self.api_url}/platform/admin/otp/settings'
        r = requests.request("GET", path, headers=self.headers, json={})
        if r.status_code == 200:
            response = r.json()
            self.sms_settings = response['data']
            print(self.sms_settings)
        else:
            assert False     
        

    def set_tiger_sms_status(self, status='off'): # off:1 , on:3
        
        path = f'{self.api_url}/platform/admin/otp/settings'
        payload = self.sms_settings

        settings = str(status.lower()) in ('true','on','1','yes','y','t')
        if settings:
            payload['smsLoginMobile'] = 3
            payload['smsLoginApp'] = 3

            payload['smsRegisterApp'] = 3
            payload['smsRegisterMobile'] = 3

        else:
            payload['smsLoginMobile'] = 1
            payload['smsLoginApp'] = 1

            payload['smsRegisterApp'] = 1
            payload['smsRegisterMobile'] = 1

        r = requests.request("PUT", path, headers=self.headers, json=payload)
        if r.status_code == 200:
            response = r.json()
            if response['code'] != 0:
                assert False
        else:
            assert False
        
    def get_sport_settings(self):
        
        path = f'{self.api_url}/platform/admin/sport-setting'

        r = requests.request("GET", path, headers=self.headers, json={})
        if r.status_code == 200:
            response = r.json()
            if response['code'] != 0:
                assert False
            self.sport_settings =response['data']['data']

        else:
            assert False     

    def set_sport_cashout_status(self, status='on'):
        print ('set_sport_cashout_status')
        
        path = f'{self.api_url}/platform/admin/sport-setting'
        self.sport_settings['cashOut'] = str(status.lower()) in ('true','on','1','yes','y','t')
        payload = self.sport_settings

        r = requests.request("PUT", path, headers=self.headers, json=payload)
        if r.status_code == 200:
            response = r.json()
            if response['code'] != 0:
                assert False
        else:
            assert False

    def get_merchant_setting(self,currency='CNY'):
        path = f'{self.api_url}/platform/admin/merchantSetting?currency={currency}'

        r = requests.request("GET", path, headers=self.headers, json={})
        if r.status_code == 200:
            response = r.json()
            if response['code'] != 0:
                assert False
            self.merchant_settings =response['data']
            
        else:
            assert False
        
    def set_merchant_livesport(self,livesport_is_on=True,limit=Live_Sport_Limit.NO_LIMIT,currency='CNY') :
        path = f'{self.api_url}/platform/admin/merchantSetting'
        if not self.merchant_settings :
            self.get_merchant_setting(currency)
        payload = self.merchant_settings
        payload['settingMap']['liveSport'] = livesport_is_on
        payload['settingMap']['liveSportQualifyType'] = limit.value

        r = requests.request("PUT", path, headers=self.headers, json=payload)
        if r.status_code == 200:
            response = r.json()
            if response['code'] != 0:
                assert False
            self.merchant_settings =response['data']
            
        else:
            assert False

    def get_sms_code(self, acc):
        try:
            mydb = pymysql.connect(            
                host = self.tiger_db_host,
                user = self.tiger_db_user,
                password = self.tiger_db_pw,
                database = 'tiger_user'
            )

            cur = mydb.cursor()
            cur.execute(f"Select uso.code "
                        f"from user_sms_otp uso  "
                        f"where account ='{acc}' and vendor='{self.vd_code}' "
                        f"order by uso.id desc;")
            row = cur.fetchone()
            return row[0]
        except Exception as e:
            
            return ''
    
    def get_transaction_status(self, type, trans_id='', currency='CNY'):

        status = -99
        date = datetime.now(timezone(timedelta(hours=-4))).strftime('%Y-%m-%d')  #查詢日期需使用 -4 時區
        params = {
                    'pageNum' : 1,
                    'pageSize' : 100,
                    'startDate' : date,
                    'endDate' : date,
                    'value' : trans_id,
                    'type' : 'orderNumber',
                    'fuzzyAccount' :False,
                    'time': 'applyTime',
                    'asc' : True,
                    'depositAuditLayerId' : 0,
                    'currency' : currency
                }
        if trans_id != '':
            if type == self.Transaction_Type.DEPOSIT:
                path = f'{self.api_url}/platform/admin/depositRecord'
                params['depositAuditLayerId'] = 0
            else :
                path = f'{self.api_url}/platform/admin/withdrawals'
                params['withdrawAuditLayerId'] = 0
                params['orderNo'] = trans_id


            r = requests.request("GET", path, headers=self.headers, params=params, json={})
            if r.status_code == 200:
                response = r.json()
                if response['code'] != 0:
                    assert False
                    
                status = response['data']['data'][0]['status']
                    
            else:
                assert False
        
        return status
    
    def c2c_enable(self, is_enable=False):
        path = f'{self.api_url}/platform/admin/ctc/paymentSetting'
               
        payload = {
        "depositAppOnOff": True,
        "bankCardLevelList": [
            -1
        ],
        "depositWebOnOff": True,
        "depositBufferRange": 100,
        "depositRangeList": [
            {
                "minAmount": "1",
                "maxAmount": "500"
            },
            {
                "minAmount": "501",
                "maxAmount": "1000"
            },
            {
                "minAmount": "1001",
                "maxAmount": "1500"
            },
            {
                "minAmount": "1501",
                "maxAmount": "2000"
            },
            {
                "minAmount": "2001",
                "maxAmount": "2500"
            },
            {
                "minAmount": "2501",
                "maxAmount": "3000"
            },
            {
                "minAmount": "10000",
                "maxAmount": "29999"
            },
            {
                "minAmount": "500000",
                "maxAmount": "1000000"
            }
        ],
        "ctcOnOff": is_enable
    }


        r = requests.request("PUT", path, headers=self.headers, json=payload)
        if r.status_code == 200:
            response = r.json()
            if response['code'] != 0:
                print(response)
                # assert False
        else:
            assert False


    def withdraw_accepted(self,trans_id):
        api_list = {
            f'{self.api_url}/platform/admin/withdraw' : {
                'orderNumber': trans_id,
                'status': 3
            },
            f'{self.api_url}/platform/admin/disbursement' : {
                'auto': False,
                'orderNumber': trans_id,
                'source': 1,
                'status': 2
            },
            f'{self.api_url}/platform/admin/disbursement' : {
                'auto': False,
                'orderNumber': trans_id,
                'source': 1,
                'status': 1
            },
        }

        for k,v in api_list.items(): 
            r = requests.request("PUT", k, headers=self.headers, json=v)
            if r.status_code == 200:
                    response = r.json()
                    if response['code'] != 0:
                        print(response)
            else:
                    assert False
            time.sleep(1)

    def deposit_audit(self, trans_id, result = Deposit_Status.CONFIRMED) :
        api_list = {
            f'{self.api_url}/platform/admin/depositRecordStatus' : {
                'memo': "",
                'orderNumber':trans_id,
                'status': 1
            },
            f'{self.api_url}/platform/admin/depositRecordStatus' : {
                'memo': "",
                'orderNumber':trans_id,
                'status': result.value
            },            
        }
        for k,v in api_list.items(): 
            r = requests.request("PUT", k, headers=self.headers, json=v)
            if r.status_code == 200:
                    response = r.json()
                    if response['code'] != 0:
                        print(response)                        
            else:
                    assert False
            time.sleep(1)

    def set_bank_card_deposit(self,currency='CNY'):
        data = ''
        path = f'{self.api_url}/platform/admin/payment_method?currency={currency}'
        r = requests.request("GET", path, headers=self.headers)
        if r.status_code == 200:
            response = r.json()
            if response['code'] == 0:
                data = response['data']
                if 1 in data['paymentMethod']['orderM']:
                    pre_index = list(data['paymentMethod']['orderM']).index(1)
                    if pre_index != 0:
                        data['paymentMethod']['orderM'][pre_index] = data['paymentMethod']['orderM'][0]
                        data['paymentMethod']['orderM'][0] = 1                        
                else : 
                    data['paymentMethod']['orderM'][0] = 1
                r = requests.request("PATCH", path, headers=self.headers,json=data)

            else:
                print(f'api response error : {response['code']} \n traceID = {response['traceId']} \n {response['msg']}')
        else:
            print(f'set bank card deposit status code : {r.status_code}')

