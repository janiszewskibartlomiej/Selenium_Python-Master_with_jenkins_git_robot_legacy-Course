import csv

# Opening a File Here
f = open('../s20_web_scaping/hipp_links.csv')
csv_data = csv.reader(f)
list1 = list(csv_data)
print(list1)

l = len(list1)

for i in range(0, l):
    print(list1[i][0])

assert list1[0] is  None, "Test printowania message"

#CSV Write

import csv

f = open("RES1.csv", 'w', newline='')
csv_w = csv.writer(f)
csv_w.writerow(['hello', 12, 131])
csv_w.writerow(['hello1', 13, 132])
csv_w.writerow(['hello2', 14, 133])
csv_w.writerow(['hello3', 15, 134])

f.close()