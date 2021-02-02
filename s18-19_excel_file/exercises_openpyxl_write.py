import openpyxl

# load workbook

wk = openpyxl.Workbook()
sh = wk.active
sh.title = "Testing_write"
print(sh.title)

sh["A4"].value = "test to write cell"

wk.create_sheet(title="Testing2")
sh1 = wk["Testing2"]
sh1["A3"] = "+91-85492145"

# remove sheet
wk.remove(wk["Testing_write"])

wk.save("D:/GITHUB/Selenium_Python_beginner_to_advanced_with_jenkins_git_robot_legacy-Course/test_write_openpyxl.xlsx")
