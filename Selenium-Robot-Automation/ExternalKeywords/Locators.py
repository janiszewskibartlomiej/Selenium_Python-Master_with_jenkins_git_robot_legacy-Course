import json
import jsonpath

def read_locator_from_json(locatoname):
    f = open('D:/GITHUB/Selenium_Python_beginner_to_advanced_with_jenkins_git_robot_legacy-Course/Selenium-Robot-Automation/JsonFiles/Elements.json','r')
    response = json.loads(f.read())
    value = jsonpath.jsonpath(response,locatoname)
    return value[0]
