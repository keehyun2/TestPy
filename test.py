import sys
import html
import yaml
import pymongo
import os

from selenium import webdriver
from bs4 import BeautifulSoup as bs

def jobsCrawl(event, context):

  # 몽도 디비 접속

  with open('application.yml','r') as f:
      conf = yaml.load(f, Loader=yaml.FullLoader)

  username = conf['musername']
  password = conf['mpassword']

  client = pymongo.MongoClient('mongodb://%s:%s@ds335648.mlab.com:35648/okky_job?retryWrites=false' % (username, password))

  db = client.get_default_database()
  jobs = db["jobs"]

  # 필요한 파이썬 라이브러리 
  # # pip3 install pymongo schedule selenium beautifulsoup4 pyyaml

  # chromedriver 는 설치된 크롬에 호환되는 버전을 받아서 사용할것
  # 크롬 드라이버 다운로드 - https://chromedriver.chromium.org/downloads
  # 크롬버전 확인 - chrome://settings/help


  driver = None
  if sys.platform == "linux" or sys.platform == "linux2":
    # driver = webdriver.Chrome(os.getcwd() + '\chromedriver', options=options)
    driver = webdriver.PhantomJS(service_log_path='/var/log/phantomjs/ghostdriver.log')
  elif sys.platform == "win32":
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(os.getcwd() + '\chromedriver.exe', options=options)
  # driver = webdriver.PhantomJS('phantomjs-2.1.1-windows/bin/phantomjs.exe') # deprecate 됨

  # driver.get('https://okky.kr/articles/jobs')
  driver.get('https://okky.kr/articles/recruit?sort=id&order=desc&filter.act=Y&filter.city=%EC%84%9C%EC%9A%B8&max=20&offset=0')

  soup = bs(driver.page_source, "html.parser")

  # 목록 태그 수집
  article_list = soup.select("#list-article > div.panel.panel-default > ul > li")

  a = []
  # 반복 처리
  for article in article_list:

    try:
      title = article.select("div.list-title-wrapper.clearfix > h5")[0].get_text().strip()
      print(title)    
      article_id = article.select("span.article-id")[0].get_text().replace('#','').strip()
      # print(article_id)
      area = article.select(".list-tag > span")[1].get_text().strip()
      # print(area)
      nickname = article.select(".nickname")[0].get_text().strip()
      timeago = article.select(".timeago")[0].get_text().strip()

      if jobs.find_one({"article_id": article_id}) is None:
        a.append({ "article_id": article_id, "area": area, "title": title, "nickname": nickname, "timeago": timeago })
          
    except:
      print("Unexpected error:", sys.exc_info()[0])
      pass

  print(a)
  if a: # 배열 empty 체크
    x = jobs.insert_many(a)

  driver.quit()

# import schedule
# import time

# 300초에 한번씩 실행
# schedule.every(300).seconds.do(jobsCrawl)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# jobsCrawl()