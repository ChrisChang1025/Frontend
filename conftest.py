import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure, os, sys, platform, pysftp, datetime

def pytest_addoption(parser):
    parser.addoption("--env", default="uat", choices=["uat", "pre-prod", "demo"], help="enviroment parameter")
    parser.addoption("--vend", default="vd002", help="enviroment parameter")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def vend(request):
    return request.config.getoption("--vend")

@pytest.fixture(scope="class")
def get_pc_options():
    global pc_options, pc_capabilities
    pc_capabilities = DesiredCapabilities.CHROME.copy()
    pc_capabilities['loggingPrefs'] = {'performance': 'ALL'}
    pc_capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}  # for Chrome 75 版本之後的更新
    pc_options = webdriver.ChromeOptions()
    # pc_options.add_argument('--headless')      # Hide chrome window
    pc_options.add_argument('--log-level=3')   # Hide console log
    pc_options.add_argument('--fixlaunch=0')
    pc_options.add_argument('--no-sandbox')
    pc_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    pc_options.add_argument('--window-size=1920,1080')
    return pc_options, pc_capabilities


@pytest.fixture(scope="class")
def get_wap_options():
    global wap_options, wap_capabilities
    wap_capabilities = DesiredCapabilities.CHROME.copy()
    wap_capabilities['loggingPrefs'] = {'performance': 'ALL'}
    wap_capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}  # for Chrome 75 版本之後的更新
    wap_options = webdriver.ChromeOptions()
    # wap_options.add_argument('--headless')      # Hide chrome window
    wap_options.add_argument('--log-level=3')   # Hide console log
    wap_options.add_argument('--fixlaunch=0')
    wap_options.add_argument('--no-sandbox')
    wap_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wap_options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone 12 Pro'})
    return wap_options, wap_capabilities

@pytest.fixture(scope="class")
def get_pc_driver(request,get_pc_options):
    global driver
    pc_options,pc_capabilities = get_pc_options
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=pc_options)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="class")
def get_wap_driver(request,get_wap_options):
    global driver
    wap_options,wap_capabilities = get_wap_options
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=wap_options)
    request.cls.driver = driver
    yield 
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            allure.attach(driver.get_screenshot_as_png(), "失敗截圖", allure.attachment_type.PNG)
        except Exception as e:
            print(f"fail to take screenshot : {e}")

def generate_allure_report():
    os.system('allure generate ./Report -o ./Temp --clean')

def upload_allure_report():
    sHostName = 'remote_url'
    sUserName = 'remote_user'
    sPassWord = 'remote_password'
    new_file_name = f"{datetime.datetime.now():%Y%m%d_%H%M%S}"
    try:
        _cnopts = pysftp.CnOpts()
        _cnopts.hostkeys = None
        with pysftp.Connection(sHostName, username=sUserName, password=sPassWord, cnopts=_cnopts) as sftp:
            to_dir = '/var/www/html/frontend_test_report/%s/' % (new_file_name)
            sftp.mkdir(to_dir)
            if platform.system() == 'Windows':
                sftp.cwd(to_dir)
                from_dir =  os.path.normpath(os.getcwd() + '/report')
                for _root, _dirs, _files in os.walk(from_dir):
                    for f in _files:
                        _folder = ".{}".format(_root.split(from_dir)[1].replace('\\','/'))
                        try:
                            sftp.mkdir(_folder)
                        except Exception as error:
                            pass

                        fileName = os.path.join(_root, f).replace('\\', '/')
                        sftp.put(fileName, "./{}/{}".format(_folder, f), preserve_mtime=True)
            else:
                sftp.put_r('Temp/', '/var/www/html/frontend_test_report/%s/' % (new_file_name))  
            print('Allure Report Path : http://'+sHostName+'/frontend_test_report/%s/index.html' % (new_file_name))  
            os.system('rm -rf ./Temp')            
    except:
        print(sys.exc_info())

if __name__ == "__main__":
    pytest.main(['-sv','--alluredir','./Report','--clean-alluredir','--vend','vd004'])
    # pytest.main(['-sv','-m','wap','--alluredir','./Report','--clean-alluredir','--vend','vd004']) # Run WAP test case
    # pytest.main(['-sv','-m','pc','--alluredir','./Report','--clean-alluredir','--vend','vd004'])  # Run PC test case
    generate_allure_report()
    upload_allure_report()