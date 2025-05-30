from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

driver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")

chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Change this if needed

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.google.com")
