import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import shutil

# GLOBAL VARIABLES MUST BE SET
PATH = "C:\\chromedriver-win64\\chromedriver.exe" # Path to predownloaded chrome driver (must be in C)
USER = "soccervinesmk@gmail.com" # Pinterest username/email
PASS = "Maya6820!3" # Pinterest password
URL = "https://www.pinterest.ca/mike200972/vzlsexe/?invite_code=6be2cbbedb664fffb616b95f3c099655&sender=707346822632555060"  # URL to Pinterest folder
DOWNLOADS = r"C:\Users\mike2\Downloads" # Path to downloads folder (KEEP r before quotes)
TARGET = r"C:\Users\mike2\Desktop\vzls\imgs" # Path to target image folder (KEEP r before quotes)

# -------------------------------- DONT ADJUST FROM HERE DOWN -------------------------------------------------------------------------------------------

# Create ChromeOptions object and set the executable path
chrome_options = Options()
chrome_options.add_argument(f"executable_path={PATH}")

# Use the ChromeOptions when creating the driver
driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# Using XPath to locate the button inside the div with data-test-id="login-button"
button_xpath = "//div[@data-test-id='login-button']//button"

# Wait for the login button to be clickable
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

# Click the button
login_button.click()

# Wait for the login form elements to be present
email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-test-id='emailInputField']//input[@id='email']")))
email_input.send_keys(USER)

password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-test-id='passwordInputField']//input[@id='password']")))
password_input.send_keys(PASS)

time.sleep(2)

# Send the Enter key
password_input.send_keys(Keys.RETURN)

time.sleep(15)

# Locate the image element to hover over
image_to_hover = driver.find_element(By.XPATH, "//img[contains(@alt, 'This contains an image of:')]")

# Create an ActionChains instance
actions = ActionChains(driver)

# Hover over the image to trigger the dropdown
actions.move_to_element(image_to_hover).perform()

time.sleep(2)

# Wait for the dropdown to be visible
wait = WebDriverWait(driver, 10)
dropdown_visible = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-test-id="overflow-menu-button"]')))

# Click the dropdown menu button to open the menu
dropdown_visible.click()

time.sleep(2)  # Adjust the sleep time as needed to allow the menu to fully open

# Locate the download button within the dropdown
download_button = driver.find_element(By.ID, 'pin-action-dropdown-item-1')

# Click the download button
download_button.click()

time.sleep(2)

# Get a list of all files in the Downloads folder
files = os.listdir(DOWNLOADS)
    
# Filter out directories and get the most recently modified file
newest_file = max([f for f in files if os.path.isfile(os.path.join(DOWNLOADS, f))], key=lambda x: os.path.getmtime(os.path.join(DOWNLOADS, x)))
    
# Construct the full path of the newest file in the Downloads folder
source_path = os.path.join(DOWNLOADS, newest_file)
    
# Construct the destination path
destination_full_path = os.path.join(TARGET, newest_file)
    
# Move the newest file to the destination path
shutil.move(source_path, destination_full_path)
print(f"Newest file '{newest_file}' moved to '{destination_full_path}'.")

driver.quit()