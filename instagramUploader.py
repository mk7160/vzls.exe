import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import subprocess
import pyautogui
import pygetwindow as gw

# GLOBAL VARIABLES MUST BE SET
PATH = "C:\\chromedriver-win64\\chromedriver.exe" # Path to predownloaded chrome driver (must be in C)
USER = "testermk77" # Pinterest username/email
PASS = "Maya6820!2" # Pinterest password
URL = "https://www.instagram.com"  # URL to instagram
IMAGE = r"C:\Users\mike2\Desktop\vzls\crops\output_image.jpg" # Path to image to be uuploaded (KEEP r before quotes)
WIDTH = 430 # Browser ratios
HEIGHT = 932

# -------------------------------- DONT ADJUST FROM HERE DOWN -------------------------------------------------------------------------------------------

# Create ChromeOptions object and set the executable path
chrome_options = Options()
chrome_options.add_argument(f"executable_path={PATH}")

# Use the ChromeOptions when creating the driver
driver = webdriver.Chrome(options=chrome_options)

# Set the window size to achieve the desired aspect ratio
driver.set_window_size(WIDTH, HEIGHT)

driver.get(URL)

# Wait for the login form elements to be present
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
email_input.send_keys(USER)

password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
password_input.send_keys(PASS)

time.sleep(2)

# Send the Enter key
password_input.send_keys(Keys.RETURN)

time.sleep(5)

notNow = "//div[@role='button' and @tabindex='0']"

# Wait for the button to be clickable
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
notNowButton = wait.until(EC.element_to_be_clickable((By.XPATH, notNow)))

# Click the button
notNowButton.click()

time.sleep(3)

notNowAgain = "//button[@class='_a9-- _a9_1' and @tabindex='0']"

# Wait for the button to be clickable
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
notNowAgainButton = wait.until(EC.element_to_be_clickable((By.XPATH, notNowAgain)))

# Click the button
notNowAgainButton.click()

time.sleep(3)

plus = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[4]/div/span/div/a/div/div/div/div"

# Wait for the button to be clickable
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
plusButton = wait.until(EC.element_to_be_clickable((By.XPATH, plus)))

# Click the button
plusButton.click()

time.sleep(3)

addFile = pyautogui.locateCenterOnScreen("select.png")

time.sleep(3)

# Click the button
pyautogui.moveTo(addFile)
time.sleep(2)
pyautogui.click()
print(addFile)

time.sleep(3)

uploadImage = "fileUpload.exe"
subprocess.run(uploadImage)

browser_window = gw.getActiveWindow()

time.sleep(5)#-------------------------------------------------------------WORKS UPTO HERE

next = pyautogui.locateOnScreen("next.png")
next = pyautogui.center(next)
print(next)

# Simulate a mouse click at the calculated absolute position
pyautogui.moveTo(next)
time.sleep(2)
pyautogui.click()

time.sleep(2)

# Set the window size to achieve the desired aspect ratio
driver.set_window_size(WIDTH*2, HEIGHT)

nextAgain = pyautogui.locateOnWindow("next.png")
nextAgain = pyautogui.center(nextAgain)
print(nextAgain)

pyautogui.moveTo(nextAgain)
time.sleep(2)
pyautogui.click()

time.sleep(3)

share = pyautogui.locateOnWindow("share.png")
share = pyautogui.center(share)
print(share)

pyautogui.moveTo(share)
time.sleep(2)
pyautogui.click()

time.sleep(20)

driver.quit()