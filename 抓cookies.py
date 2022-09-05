import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://192.168.5.1:5088/checkgw.php')
time.sleep(20)
with open('cookies.txt', 'w') as f:
    f.write(json.dumps(driver.get_cookies()))
driver.close()
