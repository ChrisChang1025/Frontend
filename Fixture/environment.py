import pytest
import os


@pytest.fixture(scope="session")
def env_url(env,vend):
    global url, admin_url
    if env == "pre-prod":
        url = "https://test_domain"
        admin_url = "https://test_domain"
    else:
        url = f"https://test_domain"
        admin_url = f"https://test_domain"

    return url, admin_url

@pytest.fixture(scope="session")
def get_user():
    return "test_account", "test_password"

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

