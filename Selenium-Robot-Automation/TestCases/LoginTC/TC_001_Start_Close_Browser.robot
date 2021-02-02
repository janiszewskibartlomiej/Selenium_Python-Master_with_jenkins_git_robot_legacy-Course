*** Settings ***
Library  SeleniumLibrary
Resource  ../../Resources/Resources1.robot
Documentation  This File having testcase of testing ABC Functionality
Test Setup  Start Browser and Maximize
Test Teardown  Close Browser Window
Suite Setup  Before Each Test Suite
suite teardown  After Each Test Suite
default tags  DFLT
force tags  ALL_TC
Library  ../../ExternalKeywords/Locators.py


*** Variables ***
${Browser}  Chrome
${Url}  http://www.thetestingworld.com/testings

*** Test Cases ***
Robot First Test Case
    [Tags]  Smoke
    ${username}=  Read Element Locator  Registration.username_textbox_name
    Input Text  name:${username}  Testing
    ${password}=  Read Element Locator  Registration.password_textbox_name
    Input Text  name:fld_email  testingworldinida@gmail.com
    Input Text  name:${password}  123456

Robot Next Test Case
    Select Radio Button  add_type  office

*** Keywords ***
Read Element Locator
    [Arguments]  ${JsonPath}
    ${result}=  read_locator_from_json  ${JsonPath}
    [return]  ${result}
