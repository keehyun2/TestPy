import sys
import html
# pip3 install selenium BeautifulSoup

from selenium import webdriver
from bs4 import BeautifulSoup as bs

options = webdriver.ChromeOptions()
options.add_argument('headless')

# replace 'chromedriver_path' with path where your chromedriver is located.
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)

driver.get('https://okky.kr/articles/jobs')

soup = bs(driver.page_source, "html.parser")

#li1_title = soup.select("#list-article > div.panel.panel-default > ul > li:nth-child(1) > div.list-title-wrapper.clearfix > h5")[0]
article_list = soup.select("#list-article > div.panel.panel-default > ul > li")

for article in article_list:

  try:
    title = article.select("div.list-title-wrapper.clearfix > h5")[0].get_text()
    title = title.strip()
    print(title)
  except:
    print("Unexpected error:", sys.exc_info()[0])
    pass

driver.quit()
