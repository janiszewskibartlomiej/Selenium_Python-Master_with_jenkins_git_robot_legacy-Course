import pytest
from selenium import webdriver



@pytest.fixture(params=["firefox_driver", "chrome_driver"])
def driver(request):
    print(dir(request))
    print(request.module)
    print(request.function.__name__)
    print("instance: ", request.instance)
    global driver
    if request.param == "chrome_driver":
        path = "D:\\GITHUB\\Selenium_Python_beginner_to_advanced_with_jenkins_git_robot_legacy-Course\\drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=path)

    if request.param == "firefox_driver":
        path = "D:\\GITHUB\\Selenium_Python_beginner_to_advanced_with_jenkins_git_robot_legacy-Course\\drivers\\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=path)

    driver.maximize_window()
    yield driver
    driver.close()


def data_generator():
    li = [["user1", "pass1"], ["user2", "pass2"], ["user3", "pass3"]]
    return li


@pytest.mark.parametrize('enter_username_and_password', data_generator())
def test_validation(enter_username_and_password, driver):
    driver.get("http://www.theTestingWorld.com/testings")
    driver.find_element_by_xpath("//label[text()='Login']").click()
    driver.find_element_by_name("_txtUserName").send_keys(enter_username_and_password[0])
    driver.find_element_by_name("_txtPassword").send_keys(enter_username_and_password[1])
