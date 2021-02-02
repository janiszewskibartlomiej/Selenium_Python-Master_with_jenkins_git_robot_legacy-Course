*** Settings ***
Library  SeleniumLibrary
Library  SeleniumLibrary
Resource  ../../Resources/Resources1.robot

*** Variables ***
${Browser}  Chrome
${URL}  http://www.thetestingworld.com/testings

*** Test Cases ***
test_TC001_moje
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    Input Text  name:fld_username  tests
    Input Text  xpath://input[@name='fld_email']  test@wp.pl
    Clear Element Text  name:fld_username
    Input Text  name:fld_username  tests11111
    Select Radio Button  add_type  office
    Select Checkbox  xpath://input[@name='terms']
    Click Link  xpath://a[text()='Read Details']
    Select Checkbox  name:terms
    Click Button  type:submit
    Set Selenium Speed  2seconds
    Select From List By Index  name:sex 2
    Select From List By Value  name:sex 1
    Select From List By Label  name:sex Female
    Enter Username Password Email
    Enter Argument  testing  wp@wp.pl  1234

    Close Browser


*** Keywords ***
Enter Username Password Email
    Input Text  name:fld_username  tests
    Input Text  name:fld_email  test@wp.pl
    Input Text  name:fld_password  123

Enter Argument
    [Arguments]  ${username}  ${email}  ${password}
    Input Text  name:fld_username  ${username}
    Input Text  name:fld_email  ${email}
    Input Text  name:fld_password  ${password}