from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())  # مدیریت درایور به صورت جدید
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://adfgdfgmin.nxbo.ir/")
time.sleep(2)
user=driver.find_element("name","username")
user.send_keys("a.ashbtffcbtiani@nobitex.net")
password=driver.find_element("name","password")
password.send_keys("@Aov51dfgcgcdrt6tfg20fgdh5gyh120")
otp=driver.find_element("name","otp_token")
otp.send_keys("433549")
captcha=driver.find_element("name","captcha_1")
captcha.send_keys("tqlb")

