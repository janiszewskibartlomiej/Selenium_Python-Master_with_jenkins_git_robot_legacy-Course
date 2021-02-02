*** Settings ***
Library  SeleniumLibrary
Resource  ../../Resources/Resources1.robot
Documentation  This File having testcase of testing ABC Functionality
Test Setup  Start Browser and Maximize
Test Teardown  Close Browser Window
default tags  DFLT
force tags  ALL_TC

*** Variables ***
${Browser}  Chrome
${Url}  http://www.thetestingworld.com/testings

*** Test Cases ***
Robot Second Test Case
    Input Text  name:fld_username  Testing
    Input Text  name:fld_email  testingworldinida@gmail.com
    Input Text  name:fld_password  123456

Robot Second Next Test Case
    [Tags]  Regression
    Select Radio Button  add_type  office

