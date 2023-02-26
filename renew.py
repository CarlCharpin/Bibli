from selenium.webdriver.firefox.service import Service
from selenium import webdriver

service = Service(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome(service=service)