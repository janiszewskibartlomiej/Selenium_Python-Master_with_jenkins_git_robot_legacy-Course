import os
import shutil
import sys

from selenium import webdriver
import requests
import bs4

URL = 'https://www.hipp.pl'

response = requests.get(URL)
print(response.status_code)
print(response.text)

with open(file="result_hipp_home.txt", mode="wb") as file:
    for data in response.iter_content(10000):
        file.write(data)

parse_data = bs4.BeautifulSoup(response.text)
all_links = parse_data.select('a')  # CSS locator
print(len(all_links))

file_name = "hipp_links.csv"
with open(file=file_name, mode="w+", encoding="utf-8") as file_with_link:

    for link in all_links:
        # print(link.getText())
        print(link.get("title"))
        print(link.attrs) #atrybuty
        one_link = "".join(URL + link.get("href") + ",\n")
        file_with_link.write(one_link)

