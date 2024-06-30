import os
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)

os.system("cls")
print("请先在baidu.com搜索关键词，之后点击顶栏“图片”进入图片详情页，然后复制页面URL")
print("爬取张数最好不要小于10张，否则训练效果差")
url = str(input("URL链接："))
num = int(input("爬取张数:"))

driver.get(url)
time.sleep(3)

for _ in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(1, 3))

soup = BeautifulSoup(driver.page_source, 'html.parser')
images = soup.find_all('img', class_='main_img img-hover')[:num]

if not os.path.exists('image'):
    os.makedirs('image')

for i, img in enumerate(images):
    img_url = img['src']
    if not img_url.startswith('http'):
        img_url = 'https:' + img_url

    img_data = requests.get(img_url).content
    with open(os.path.join('image', f"{i}.jpg"), 'wb') as handler:
        handler.write(img_data)

    time.sleep(random.uniform(1, 3))

driver.quit()
