import xlwt

# object of workbook

wk = xlwt.Workbook()

ws = wk.add_sheet("Testing")
ws.write(0, 0, "Testing Word") # row, column, data to write
ws.write(0, 1, "Testing Word 2")

# zapis workbook  ta biblioteka moze zapisywac w 2 formatach

wk.save("D:/GITHUB/Selenium_Python_beginner_to_advanced_with_jenkins_git_robot_legacy-Course/write_excel_first1.xls")
wk.save("D:/GITHUB/Selenium_Python_beginner_to_advanced_with_jenkins_git_robot_legacy-Course/write_excel_first2.xlsx")