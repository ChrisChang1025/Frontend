import pytest
import os
import requests

@pytest.fixture(scope="session")
def env_url(env,vend):
    global url, admin_url
    try:
        url = "https://{test_domain}/env-url?password={password}"
        if env :
            url += f"&env={env}"
            if vend :
                url += f"&vend={vend}"

        r = requests.get(url)
        obj = r.json()

        env_config = {
            'env' : env,
            'vend' : vend,
            'vd_code' : obj['vd_code'],
            'url' : obj['platform_url'],
            'api_url' : obj['api_url'],
            'admin_url' : obj['admin_url'],
            'tiger_db_host' : obj['tiger_db_host'],
            'tiger_db_user' : obj['tiger_db_user'],
            'tiger_db_pw' : obj['tiger_db_pw']
        }
        return env_config
        # return url, api_url, admin_url
    except Exception as e :
        pytest.exit(f'get env url error. ({repr(e)})')

@pytest.fixture(scope="session")
def get_admin_user():
    return "qarobot4", "test1234", ""

@pytest.fixture(scope="session")
def get_user():
    return "atrobot001", "test1234"

@pytest.fixture(scope="session")
def screenshot_dir():
    if not os.path.isdir("./Screenshot/"):
        os.mkdir("./Screenshot/")
    return "./Screenshot/"

@pytest.fixture(scope="session")
def log_dir():
    return "./Log/"

@pytest.fixture(scope="class")
def get_screenshot_path(request,screenshot_dir):
    request.cls.screenshot_path = screenshot_dir + request.cls.__name__ + "/"
    if not os.path.isdir(request.cls.screenshot_path):
        os.mkdir(request.cls.screenshot_path)

