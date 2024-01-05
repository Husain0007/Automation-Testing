from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # used to create Drivers
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

driver.get("https://www.google.com/")

'''
Locators:
By.ID
By.NAME
By.CLASS_NAME
By.TAG_NAME
By.LINK_TEXT
By.PARTIAL_LINK_TEXT
By.CSS_SELECTOR
By.XPATH
'''

#driver.find_element(By.LINK_TEXT, 'Weitere Optionen').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Weitere').click()

driver.quit()
