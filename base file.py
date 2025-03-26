from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())  # مدیریت درایور به صورت جدید
driver = webdriver.Chrome(service=service, options=options)