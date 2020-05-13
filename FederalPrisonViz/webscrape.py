from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.bop.gov/coronavirus/#')
time.sleep(20)
link = driver.find_element_by_partial_link_text('Full')
link.click()
# print(driver.page_source)
print(driver.find_element_by_tag_name('tr'))