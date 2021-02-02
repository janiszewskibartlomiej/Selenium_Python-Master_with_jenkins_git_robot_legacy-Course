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
Robot Fetch Data
    Concatenate Username and Password  Testing  World
    Open Browser  ${Url}  ${Browser}
    Maximize Browser Window
