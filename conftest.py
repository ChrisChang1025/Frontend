import tarfile
import traceback
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
                tarFileName = f"{new_file_name}.tar"
                with tarfile.open(tarFileName, "w:gz") as tar:
                    tar.add(os.path.normpath(os.getcwd() + '/Temp'), arcname=os.path.basename(os.path.normpath(os.getcwd() + '/Temp')))                            
                sftp.put(os.path.normpath(os.getcwd()+ '/' + tarFileName).replace('\\', '/'), '/var/www/html/frontend_test_report/' + tarFileName ,preserve_mtime=True)
                sftp.execute(f'tar xf /var/www/html/frontend_test_report/{tarFileName} -C /var/www/html/frontend_test_report/')
                sftp.execute(f'mv /var/www/html/frontend_test_report/Temp/* /var/www/html/frontend_test_report/{new_file_name}')
                sftp.execute(f'rm -rf /var/www/html/frontend_test_report/Temp /var/www/html/frontend_test_report/{tarFileName}')
                os.system(f"rmdir /s /q {os.getcwd()}\\Temp")
                os.remove(tarFileName)
            else:
                sftp.put_r('Temp/', '/var/www/html/frontend_test_report/%s/' % (new_file_name))  
                os.system('rm -rf ./Temp')    
            print('Allure Report Path : http://'+sHostName+'/frontend_test_report/%s/index.html' % (new_file_name))  
                    
    except:
        print(traceback.format_exc())
        print(sys.exc_info())

if __name__ == "__main__":
    pytest.main(['-sv','--alluredir','./Report','--clean-alluredir','--vend','vd004'])
    # pytest.main(['-sv','-m','wap','--alluredir','./Report','--clean-alluredir','--vend','vd004']) # Run WAP test case
    # pytest.main(['-sv','-m','DB_used','--alluredir','./Report','--clean-alluredir','--vend','vd004'])  # Run DB_used test case
    generate_allure_report()
    upload_allure_report()
