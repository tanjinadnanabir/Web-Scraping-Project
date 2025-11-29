from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# PROXY = "51.158.105.94:31826"

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--headless")
# options.add_argument(f'--proxy-server=http://{PROXY}')

driver = webdriver.Chrome(options=options)

driver.get('https://www.rokomari.com/book/authors')

driver.maximize_window()

author_list = []
for page in range(1, 209):
    driver.get(f'https://www.rokomari.com/book/authors?page={page}')

    for i in range(1,49):
        j = str(i)
        author = driver.find_element(By.XPATH,'//*[@id="author-list"]/div[3]/section/div[2]/div['+j+']/a/h2').text 
        author_list.append(author)

import pandas as pd

df = pd.DataFrame({'Author': author_list})
df.to_csv('authors.csv', index=False, encoding='utf-8')

print(len(author_list))