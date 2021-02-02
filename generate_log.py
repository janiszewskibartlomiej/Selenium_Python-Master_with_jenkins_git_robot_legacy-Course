import logging
from selenium import webdriver


logger = logging.getLogger(str(__name__))
logger.setLevel(logging.INFO)

# Create a file handler
handler_warn = logging.FileHandler('warning_log.txt')
handler_warn.setLevel(logging.WARNING)

handler_info = logging.FileHandler('info_log.txt')
handler_info.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_warn.setFormatter(formatter)
handler_info.setFormatter(formatter)

# add the handler to the logger

logger.addHandler(handler_warn)
logger.addHandler(handler_info)

logger.info('Information')
logger.warning('warning')


path = "D:\\GITHUB\\Selenium_Python_beginner_to_advanced_with_jenkins_git_robot_legacy-Course\\drivers\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
mainWin = ""
driver.maximize_window()
driver.get("https://www.thetestingworld.com/testings")
driver.find_element_by_xpath("//label[text()='Login']").click()
driver.find_element_by_name("_txtUserName").send_keys("test")
driver.find_element_by_name("_txtPassword").send_keys("test")
driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
logger.info("This is log info")
driver.close()
