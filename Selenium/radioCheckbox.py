from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

# Navigate to the registration page
driver.get("https://demo.automationtesting.in/Register.html")

# Wait for consent pop-up to appear and click 'Consent' button
try:
    consent_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'fc-cta-consent')]"))
    )
    consent_button.click()
    print("Consent accepted.")
except Exception as e:
    print(f"Failed to accept consent: {e}")

# Now, select the 'Male' radio button.
driver.find_element(By.XPATH, "//input[@value='Male']").click()

# Check Box and get Attribute
li = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for element in li:
    val = element.get_attribute('value')
    print(val)
    if val == 'Cricket':
        element.click()