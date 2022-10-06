from selenium import webdriver as web
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

years_to_scrap = range(2013, 2022)

class Csgo():
  def __init__(self):
    self.cards = dict()
    self.storaged_data = ''
    options = Options()
    self.browser = web.Chrome('./chromedriver', options=options)
    self.browser.set_window_size(800,600)

  def close_browser(self):
    self.browser.close()
    self.browser.quit()

  def set_file_name(self, link):
    link_splited = link.split('/')
    self.file_name = f"{link_splited[-2]} {link_splited[-1]}"

  def acess(self, year_link):
    browser = self.browser
    try:
      browser.get(year_link)
      self.set_file_name(year_link)
      time.sleep(2)
      self.scrap_table()
    except Exception as ex:
      print('Fail to connect to the website')
      print(f'error cause: {ex}')
      self.close_browser()

  def save_data(self):
    try:
      file = open(f'{self.file_name}.txt', 'w', encoding='utf-8')
      file.write(f'{self.storaged_data}')
    except Exception as ex:
      print(ex)
  
  def scrapper_end(self):
    self.close_browser()
  
  def storage_data(self, text):
    self.storaged_data += f'{text} \n'

  def scrap_data(self, table_element):
    browser = self.browser
    scrapped_info = f'{table_element.text}'
    print(scrapped_info)
    self.storage_data(scrapped_info)

  def scrap_table(self):
    browser = self.browser
    table_document = browser.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div/table/tbody//tr//td')
    for element in table_document:
      self.scrap_data(element)
    self.save_data()


scrapper = Csgo()
for year in years_to_scrap:
  scrapper.acess(f'https://liquipedia.net/counterstrike/Rankings/{year}')
scrapper.scrapper_end()