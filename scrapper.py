from selenium import webdriver as web
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


class Csgo():
  def __init__(self):
    self.cards = dict()
    options = Options()
    self.browser = web.Chrome('./chromedriver', options=options)
    self.browser.set_window_size(800,600)

  def close_browser(self):
    self.browser.close()
    self.browser.quit()

  def acess(self, year_link):
    browser = self.browser
    try:
      browser.get(year_link)
      time.sleep(2)
      self.scrap_table()
    except Exception as ex:
      print('Fail to connect to the website')
      self.close_browser()

  def scrap_data(self, table_element):
    browser = self.browser
    info = table_element.text
    print(info)

  def scrap_table(self):
    browser = self.browser
    # table_header = browser.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div/table/tbody//tr//th')
    table_document = browser.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div/table/tbody//tr//td')


start_scrap = Csgo()
start_scrap.acess('https://liquipedia.net/counterstrike/Rankings/2016')