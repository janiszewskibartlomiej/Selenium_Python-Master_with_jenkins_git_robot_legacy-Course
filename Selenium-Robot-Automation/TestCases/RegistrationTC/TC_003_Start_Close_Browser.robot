*** Settings ***
Library  SeleniumLibrary
Resource  ../../Resources/Resources1.robot
Documentation  This File having testcase of testing ABC Functionality
Test Setup  Start Browser and Maximize
Test Teardown  Close Browser Window
default tags  DFLT


*** Variables ***
${Browser}  Chrome
${Url}  http://www.thetestingworld.com/testings

*** Test Cases ***
Robot Third Test Case
    [Tags]  Sanity
    Input Text  name:fld_username  Testing
    Input Text  name:fld_email  testingworldinida@gmail.com
    Input Text  name:fld_password  123456

Robot Third Next Test Case
    [Tags]  Regression  Testing
    Select Radio Button  add_type  office

