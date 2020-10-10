### Using Selenium with remote WebDriver
To use the remote WebDriver, you should have Selenium server running. To run the server, use this command:

```java -jar selenium-server-standalone-2.x.x.jar```
While running the Selenium server, you could see a message looking like this:

```15:43:07.541 INFO - RemoteWebDriver instances should connect to: http://127.0.0.1:4444/wd/hub```
The above line says that you can use this URL for connecting to remote WebDriver. Here are some examples:

```python 
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


3.3. Drag and drop
You can use drag and drop, either moving an element by a certain amount, or on to another element:

element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()


3.4. Moving between windows and frames
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

3.5. Popup dialogs

alert = driver.switch_to.alert
This will return the currently open alert object. With this object, you can now accept, dismiss, read its contents or even type into a prompt. This interface works equally well on alerts, confirms, prompts. Refer to the API documentation for more information.

3.6. Navigation: history and location

driver.get("http://www.example.com")
To move backward and forward in your browser’s history:

driver.forward()
driver.back()

5.0

Expected Conditions

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

6. Actions   Chains >> https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

ActionChains can be used in a chain pattern:

menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

7.3. Alerts
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


Example, pressing ctrl+c:

ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
```
