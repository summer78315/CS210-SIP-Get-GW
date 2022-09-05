from selenium import webdriver
import time
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
cookies = [
    {
        "domain": "192.168.5.1",
        "name": "PHPSESSID",
        "path": "/",
        "sameSite": "Strict",
        "storeId": "0",
        "value": "o3fphvul2bk35dk6ialqn26hm2",
        "id": 1
    }
]
browser.get('https://192.168.5.1:5088/checkgw.php')
for cookie in cookies:
    browser.add_cookie(cookie)
time.sleep(3)
browser.get('https://192.168.5.1:5088/checkgw.php')
time.sleep(3)
table_id = browser.find_element(By.XPATH, "//table[@class='acerTbl']")
for row in range(1, 11):  # for蒐集資料
    rows = table_id.find_elements(
        By.XPATH, "//body//tbody//tr[" + str(row) + "]")  # 使用XPATH調閱row
    for row_data in rows:
        col = row_data.find_elements(By.TAG_NAME, "tr")  # 找出關鍵字tr處
        for i in range(len(col)):
            data = open("./SIP.txt", 'a')  # 打開SIP.txt 寫入資料
            print(col[i].text, file=data)  # 存入for迴圈的資料
            data.close()  # 關閉
            print(col[i].text)  # 列印至終端機
