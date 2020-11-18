### Using Selenium with remote WebDriver
To use the remote WebDriver, you should have Selenium server running. To run the server, use this command:

```java -jar selenium-server-standalone-2.x.x.jar```
While running the Selenium server, you could see a message looking like this:

```15:43:07.541 INFO - RemoteWebDriver instances should connect to: http://127.0.0.1:4444/wd/hub```
The above line says that you can use this URL for connecting to remote WebDriver. Here are some examples:


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.OPERA)

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)
   
# The desired capabilities is a dictionary, so instead of using the default dictionaries, you can specify the values explicitly:

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities={'browserName': 'htmlunit',
                         'version': '2',
                        'javascriptEnabled': True})
                        
Filling in forms

from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
WebDriver also provides features for deselecting all the selected options:

select = Select(driver.find_element_by_id('id'))
select.deselect_all()
This will deselect all OPTIONs from that particular SELECT on the page.

Suppose in a test, we need the list of all default selected options, Select class provides a property method that returns a list:

select = Select(driver.find_element_by_xpath("//select[@name='name']"))
all_selected_options = select.all_selected_options
To get all available options:

options = select.options
Once you’ve finished filling out the form, you probably want to submit it. One way to do this would be to find the “submit” button and click it:

# Assume the button has the ID "submit" :)
driver.find_element_by_id("submit").click()
Alternatively, WebDriver has the convenience method “submit” on every element. If you call this on an element within a form, WebDriver will walk up the DOM until it finds the enclosing form and then calls submit on that. If the element isn’t in a form, then the NoSuchElementException will be raised:

element.submit()


## 3.3. Drag and drop
You can use drag and drop, either moving an element by a certain amount, or on to another element:

element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()


## 3.4. Moving between windows and frames
It’s rare for a modern web application not to have any frames or to be constrained to a single window. WebDriver supports moving between named windows using the “switch_to_window” method:

driver.switch_to_window("windowName")
All calls to driver will now be interpreted as being directed to the particular window. But how do you know the window’s name? Take a look at the javascript or link that opened it:

<a href="somewhere.html" target="windowName">Click here to open a new window</a>
Alternatively, you can pass a “window handle” to the “switch_to_window()” method. Knowing this, it’s possible to iterate over every open window like so:

for handle in driver.window_handles:
    driver.switch_to_window(handle)
You can also swing from frame to frame (or into iframes):

driver.switch_to_frame("frameName")
It’s possible to access subframes by separating the path with a dot, and you can specify the frame by its index too. That is:

driver.switch_to_frame("frameName.0.child")
would go to the frame named “child” of the first subframe of the frame called “frameName”. All frames are evaluated as if from *top*.

Once we are done with working on frames, we will have to come back to the parent frame which can be done using:

driver.switch_to_default_content()

## 3.5. Popup dialogs

alert = driver.switch_to.alert
This will return the currently open alert object. With this object, you can now accept, dismiss, read its contents or even type into a prompt. This interface works equally well on alerts, confirms, prompts. Refer to the API documentation for more information.

## 3.6. Navigation: history and location

driver.get("http://www.example.com")
To move backward and forward in your browser’s history:

driver.forward()
driver.back()

## 5.0 Expected Conditions

There are some common conditions that are frequently of use when automating web browsers. Listed below are the names of each. Selenium Python binding provides some convenience methods so you don’t have to code an expected_condition class yourself or create your own utility package for them.

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present

## 6. Actions   Chains >> https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

ActionChains can be used in a chain pattern:

menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()


Example, pressing ctrl+c:

ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

## 7.3. Alerts
The Alert implementation.

class selenium.webdriver.common.alert.Alert(driver)
Bases: object

Allows to work with alerts.

Use this class to interact with alert prompts. It contains methods for dismissing, accepting, inputting, and getting text from alert prompts.

Accepting / Dismissing alert prompts:

Alert(driver).accept()
Alert(driver).dismiss()
Inputting a value into an alert prompt:

name_prompt = Alert(driver) name_prompt.send_keys(“Willian Shakesphere”) name_prompt.accept()
Reading a the text of a prompt for verification:

alert_text = Alert(driver).text self.assertEqual(“Do you wish to quit?”, alert_text)

# II. Using Selenium with remote WebDriver   

https://selenium-python.readthedocs.io/getting-started.html#using-selenium-with-remote-webdriver

I https://selenium-python.readthedocs.io/api.html#desired-capabilities

To use the remote WebDriver, you should have Selenium server running. To run the server, use this command:

java -jar selenium-server-standalone-2.x.x.jar
While running the Selenium server, you could see a message looking like this:

15:43:07.541 INFO - RemoteWebDriver instances should connect to: http://127.0.0.1:4444/wd/hub
The above line says that you can use this URL for connecting to remote WebDriver. Here are some examples:

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.OPERA)

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)
The desired capabilities is a dictionary, so instead of using the default dictionaries, you can specify the values explicitly:

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities={'browserName': 'htmlunit',
                         'version': '2',
                        'javascriptEnabled': True})
                        
 class selenium.webdriver.common.desired_capabilities.DesiredCapabilities
Bases: object

Set of default supported desired capabilities.

Use this as a starting point for creating a desired capabilities object for requesting remote webdrivers for connecting to selenium server or selenium grid.

Usage Example:

from selenium import webdriver

selenium_grid_url = "http://198.0.0.1:4444/wd/hub"

## Create a desired capabilities object as a starting point.
capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['platform'] = "WINDOWS"
capabilities['version'] = "10"

## Instantiate an instance of Remote WebDriver with the desired capabilities.
driver = webdriver.Remote(desired_capabilities=capabilities,
                          command_executor=selenium_grid_url)
Note: Always use ‘.copy()’ on the DesiredCapabilities object to avoid the side effects of altering the Global class instance.

ANDROID = {'browserName': 'android', 'platform': 'ANDROID', 'version': ''}
CHROME = {'browserName': 'chrome', 'platform': 'ANY', 'version': ''}
EDGE = {'browserName': 'MicrosoftEdge', 'platform': 'WINDOWS', 'version': ''}
FIREFOX = {'acceptInsecureCerts': True, 'browserName': 'firefox', 'marionette': True}¶
HTMLUNIT = {'browserName': 'htmlunit', 'platform': 'ANY', 'version': ''}
HTMLUNITWITHJS = {'browserName': 'htmlunit', 'javascriptEnabled': True, 'platform': 'ANY', 'version': 'firefox'}
INTERNETEXPLORER = {'browserName': 'internet explorer', 'platform': 'WINDOWS', 'version': ''}
IPAD = {'browserName': 'iPad', 'platform': 'MAC', 'version': ''}
IPHONE = {'browserName': 'iPhone', 'platform': 'MAC', 'version': ''}
OPERA = {'browserName': 'opera', 'platform': 'ANY', 'version': ''}
PHANTOMJS = {'browserName': 'phantomjs', 'javascriptEnabled': True, 'platform': 'ANY', 'version': ''}
SAFARI = {'browserName': 'safari', 'platform': 'MAC', 'version': ''}
WEBKITGTK = {'browserName': 'MiniBrowser', 'platform': 'ANY', 'version': ''}

## 7.7. Touch Actions
The Touch Actions implementation

class selenium.webdriver.common.touch_actions.TouchActions(driver)
Bases: object

Generate touch actions. Works like ActionChains; actions are stored in the TouchActions object and are fired with perform().

## 7.8. Proxy
The Proxy implementation.

class selenium.webdriver.common.proxy.Proxy(raw=None)
Bases: object

Proxy contains information about proxy type and necessary proxy settings.

## 7.9. Utilities
The Utils methods.

selenium.webdriver.common.utils.find_connectable_ip(host, port=None)
Resolve a hostname to an IP, preferring IPv4 addresses.

We prefer IPv4 so that we don’t change behavior from previous IPv4-only implementations, and because some drivers (e.g., FirefoxDriver) do not support IPv6 connections.

If the optional port number is provided, only IPs that listen on the given port are considered.

Args:	
host - A hostname.
port - Optional port number.
Returns:	
A single IP address, as a string. If any IPv4 address is found, one is returned. Otherwise, if any IPv6 address is found, one is returned. If neither, then None is returned.

## 7.11. Application Cache
The ApplicationCache implementaion.

class selenium.webdriver.common.html5.application_cache.ApplicationCache(driver)

## 7.20. Remote WebDriver
The WebDriver implementation.

class selenium.webdriver.remote.webdriver.WebDriver(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=None, browser_profile=None, proxy=None, keep_alive=False, file_detector=None, options=None)
Bases: object

Controls a browser by sending commands to a remote server. This server is expected to be running the WebDriver wire protocol as defined at https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol

Attributes:	
session_id - String ID of the browser session started and controlled by this WebDriver.
capabilities - Dictionaty of effective capabilities of this browser session as returned
by the remote server. See https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities
command_executor - remote_connection.RemoteConnection object used to execute commands.
error_handler - errorhandler.ErrorHandler object used to handle errors.
__init__(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=None, browser_profile=None, proxy=None, keep_alive=False, file_detector=None, options=None)
Create a new driver that will issue commands using the wire protocol.

Args:	
command_executor - Either a string representing URL of the remote server or a custom
remote_connection.RemoteConnection object. Defaults to ‘http://127.0.0.1:4444/wd/hub’.
desired_capabilities - A dictionary of capabilities to request when
starting the browser session. Required parameter.
browser_profile - A selenium.webdriver.firefox.firefox_profile.FirefoxProfile object.
Only used if Firefox is requested. Optional.
proxy - A selenium.webdriver.common.proxy.Proxy object. The browser session will
be started with given proxy settings, if possible. Optional.
keep_alive - Whether to configure remote_connection.RemoteConnection to use
HTTP keep-alive. Defaults to False.
file_detector - Pass custom file detector object during instantiation. If None,
then default LocalFileDetector() will be used.
options - instance of a driver options.Options class

komendy  https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webdriver

web element https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement

## 7.22. Remote WebDriver Command¶ https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.command

## 7.28. Android WebDriver
class selenium.webdriver.android.webdriver.WebDriver(host='localhost', port=4444, desired_capabilities={'browserName': 'android', 'platform': 'ANDROID', 'version': ''})
Bases: selenium.webdriver.remote.webdriver.WebDriver

Simple RemoteWebDriver wrapper to start connect to Selendroid’s WebView app

For more info on getting started with Selendroid http://selendroid.io/mobileWeb.html

__init__(host='localhost', port=4444, desired_capabilities={'browserName': 'android', 'platform': 'ANDROID', 'version': ''})
Creates a new instance of Selendroid using the WebView app

Args:	
host - location of where selendroid is running
port - port that selendroid is running on
desired_capabilities: Dictionary object with capabilities

## 7.32. Safari WebDriver
class selenium.webdriver.safari.webdriver.WebDriver(port=0, executable_path='/usr/bin/safaridriver', reuse_service=False, desired_capabilities={'browserName': 'safari', 'platform': 'MAC', 'version': ''}, quiet=False, keep_alive=True, service_args=None)
Bases: selenium.webdriver.remote.webdriver.WebDriver

Controls the SafariDriver and allows you to drive the browser.

__init__(port=0, executable_path='/usr/bin/safaridriver', reuse_service=False, desired_capabilities={'browserName': 'safari', 'platform': 'MAC', 'version': ''}, quiet=False, keep_alive=True, service_args=None)
Creates a new Safari driver instance and launches or finds a running safaridriver service.

Args:	
port - The port on which the safaridriver service should listen for new connections. If zero, a free port will be found.
executable_path - Path to a custom safaridriver executable to be used. If absent, /usr/bin/safaridriver is used.
reuse_service - If True, do not spawn a safaridriver instance; instead, connect to an already-running service that was launched externally.
desired_capabilities: Dictionary object with desired capabilities (Can be used to provide various Safari switches).
quiet - If True, the driver’s stdout and stderr is suppressed.
keep_alive - Whether to configure SafariRemoteConnection to use
HTTP keep-alive. Defaults to False.
service_args : List of args to pass to the safaridriver service
debug()
get_permission(permission)
quit()
Closes the browser and shuts down the SafariDriver executable that is started when starting the SafariDriver

set_permission(permission, value)


## 7.33. Safari WebDriver Service

class selenium.webdriver.safari.service.Service(executable_path, port=0, quiet=False, service_args=None)
Bases: selenium.webdriver.common.service.Service

Object that manages the starting and stopping of the SafariDriver

__init__(executable_path, port=0, quiet=False, service_args=None)
Creates a new instance of the Service

Args:	
executable_path : Path to the SafariDriver
port : Port the service is running on
quiet : Suppress driver stdout and stderr
service_args : List of args to pass to the safaridriver service
command_line_args()
service_url
Gets the url of the SafariDriver Service

https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.wait


## 7.38. Abstract Event Listener Support
class selenium.webdriver.support.abstract_event_listener.AbstractEventListener
Bases: object

Event listener must subclass and implement this fully or partially

after_change_value_of(element, driver)
after_click(element, driver)
after_close(driver)
after_execute_script(script, driver)
after_find(by, value, driver)
after_navigate_back(driver)
after_navigate_forward(driver)
after_navigate_to(url, driver)
after_quit(driver)
before_change_value_of(element, driver)
before_click(element, driver)
before_close(driver)
before_execute_script(script, driver)
before_find(by, value, driver)
before_navigate_back(driver)
before_navigate_forward(driver)
before_navigate_to(url, driver)
before_quit(driver)
on_exception(exception, driver)

## 7.39. Expected conditions Support  https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions


## 7.39. Expected conditions Support

```pthon
class selenium.webdriver.support.expected_conditions.alert_is_present
Bases: object

Expect an alert to be present.

class selenium.webdriver.support.expected_conditions.element_located_selection_state_to_be(locator, is_selected)
Bases: object

An expectation to locate an element and check if the selection state specified is in that state. locator is a tuple of (by, path) is_selected is a boolean

class selenium.webdriver.support.expected_conditions.element_located_to_be_selected(locator)
Bases: object

An expectation for the element to be located is selected. locator is a tuple of (by, path)

class selenium.webdriver.support.expected_conditions.element_selection_state_to_be(element, is_selected)
Bases: object

An expectation for checking if the given element is selected. element is WebElement object is_selected is a Boolean.”

class selenium.webdriver.support.expected_conditions.element_to_be_clickable(locator)
Bases: object

An Expectation for checking an element is visible and enabled such that you can click it.

class selenium.webdriver.support.expected_conditions.element_to_be_selected(element)
Bases: object

An expectation for checking the selection is selected. element is WebElement object

class selenium.webdriver.support.expected_conditions.frame_to_be_available_and_switch_to_it(locator)
Bases: object

An expectation for checking whether the given frame is available to switch to. If the frame is available it switches the given driver to the specified frame.

class selenium.webdriver.support.expected_conditions.invisibility_of_element(locator)

Bases: selenium.webdriver.support.expected_conditions.invisibility_of_element_located

An Expectation for checking that an element is either invisible or not present on the DOM.

element is either a locator (text) or an WebElement

class selenium.webdriver.support.expected_conditions.invisibility_of_element_located(locator)
Bases: object

An Expectation for checking that an element is either invisible or not present on the DOM.

locator used to find the element

class selenium.webdriver.support.expected_conditions.new_window_is_opened(current_handles)
Bases: object

An expectation that a new window will be opened and have the number of windows handles increase

class selenium.webdriver.support.expected_conditions.number_of_windows_to_be(num_windows)
Bases: object

An expectation for the number of windows to be a certain value.

class selenium.webdriver.support.expected_conditions.presence_of_all_elements_located(locator)
Bases: object

An expectation for checking that there is at least one element present on a web page. locator is used to find the element returns the list of WebElements once they are located

class selenium.webdriver.support.expected_conditions.presence_of_element_located(locator)
Bases: object

An expectation for checking that an element is present on the DOM of a page. This does not necessarily mean that the element is visible. locator - used to find the element returns the WebElement once it is located

class selenium.webdriver.support.expected_conditions.staleness_of(element)
Bases: object

Wait until an element is no longer attached to the DOM. element is the element to wait for. returns False if the element is still attached to the DOM, true otherwise.

class selenium.webdriver.support.expected_conditions.text_to_be_present_in_element(locator, text_)
Bases: object

An expectation for checking if the given text is present in the specified element. locator, text

class selenium.webdriver.support.expected_conditions.text_to_be_present_in_element_value(locator, text_)
Bases: object

An expectation for checking if the given text is present in the element’s locator, text

class selenium.webdriver.support.expected_conditions.title_contains(title)
Bases: object

An expectation for checking that the title contains a case-sensitive substring. title is the fragment of title expected returns True when the title matches, False otherwise

class selenium.webdriver.support.expected_conditions.title_is(title)
Bases: object

An expectation for checking the title of a page. title is the expected title, which must be an exact match returns True if the title matches, false otherwise.


class selenium.webdriver.support.expected_conditions.url_changes(url)
Bases: object

An expectation for checking the current url. url is the expected url, which must not be an exact match returns True if the url is different, false otherwise.


class selenium.webdriver.support.expected_conditions.url_contains(url)
Bases: object

An expectation for checking that the current url contains a case-sensitive substring. url is the fragment of url expected, returns True when the url matches, False otherwise

class selenium.webdriver.support.expected_conditions.url_matches(pattern)
Bases: object

An expectation for checking the current url. pattern is the expected pattern, which must be an exact match returns True if the url matches, false otherwise.

class selenium.webdriver.support.expected_conditions.url_to_be(url)
Bases: object

An expectation for checking the current url. url is the expected url, which must be an exact match returns True if the url matches, false otherwise.

class selenium.webdriver.support.expected_conditions.visibility_of(element)
Bases: object

An expectation for checking that an element, known to be present on the DOM of a page, is visible. Visibility means that the element is not only displayed but also has a height and width that is greater than 0. element is the WebElement returns the (same) WebElement once it is visible

class selenium.webdriver.support.expected_conditions.visibility_of_all_elements_located(locator)
Bases: object

An expectation for checking that all elements are present on the DOM of a page and visible. Visibility means that the elements are not only displayed but also has a height and width that is greater than 0. locator - used to find the elements returns the list of WebElements once they are located and visible


class selenium.webdriver.support.expected_conditions.visibility_of_any_elements_located(locator)
Bases: object

An expectation for checking that there is at least one element visible on a web page. locator is used to find the element returns the list of WebElements once they are located


class selenium.webdriver.support.expected_conditions.visibility_of_element_located(locator)
Bases: object

An expectation for checking that an element is present on the DOM of a page and visible. Visibility means that the element is not only displayed but also has a height and width that is greater than 0. locator - used to find the element returns the WebElement once it is located and visible
```

### Relative Locators
Selenium 4 brings Relative Locators which are previously called as Friendly Locators. This functionality was added to help you locate elements that are nearby other elements. The Available Relative Locators are:

above
below
toLeftOf
toRightOf
near







