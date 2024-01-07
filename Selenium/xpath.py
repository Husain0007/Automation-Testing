from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # used to create Drivers
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

driver.get("https://demo.automationtesting.in/Register.html")

# Xpath is a relative path used to identify tag(s) in the page that may not have a unique "id" attribute
# Syntax: //tagname[@attribute='value'] or //*[@attribute='value']

# This
#//input[@placeholder='First Name']

# or this 
#//*[@placeholder='First Name']

# Finding text between tags
#//label[text()='Full Name* ']

# contains
#//label[contains(text(), 'Full Name')]

# index
# //label[2]

# OR and AND logic
#//*[@placeholder='First Name' and @ng-mode="FirstName"]
#//*[@placeholder='First Name' or @np-model="FirstName"]

# parent - Child - ancestor
#//form[@id='basicBootstrapForm']/child::div

# following - sibling - preceding
# //input[@id='checkbox1']//following-sibling::label
# //input[@id='checkbox1']//preceding-sibling::label