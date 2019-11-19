import sys
import html
# 아래 명령어로 설치 먼저 해야함. 
# pip3 install selenium BeautifulSoup

from selenium import webdriver
from bs4 import BeautifulSoup as bs

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)

driver.get('https://okky.kr/articles/jobs')

soup = bs(driver.page_source, "html.parser")

# 목록 태그 수집
article_list = soup.select("#list-article > div.panel.panel-default > ul > li")

# 반복 처리
for article in article_list:

  try:
    title = article.select("div.list-title-wrapper.clearfix > h5")[0].get_text()
    title = title.strip()
    print(title)
  except:
    print("Unexpected error:", sys.exc_info()[0])
    pass

driver.quit()
