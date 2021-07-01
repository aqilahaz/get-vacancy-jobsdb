from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import pickle
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np


drv_path = "C:\\Users\\LENOVO\\Documents\\chromedriver\\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(drv_path, options=chrome_options)
# driver.minimize_window()

# yay Alhamdulillah

links = []
for i in range(36,51):
	url = 'https://id.jobsdb.com/ID/id/Search/FindJobs?AD=30&Blind=1&Host=J%2cS&JSRV=1&page='+str(i)
	driver.get(url)
	print("--------------------------------")
	print('Page '+str(i))
	print("--------------------------------")
	element = driver.find_elements_by_class_name("posLink")
	for elem in element:
		link = elem.get_attribute('href')
		links.append(link)
		# print(link)
	time.sleep(5)


import csv

with open("jobsdb-2.csv", "w") as output:
    output.write(str(links))