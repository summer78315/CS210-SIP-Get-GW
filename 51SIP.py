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
for row in range(1, 11):  # for�`�����
    rows = table_id.find_elements(
        By.XPATH, "//body//tbody//tr[" + str(row) + "]")  # �ϥ�XPATH�վ\row
    for row_data in rows:
        col = row_data.find_elements(By.TAG_NAME, "tr")  # ��X����rtr�B
        for i in range(len(col)):
            data = open("./SIP.txt", 'a')  # ���}SIP.txt �g�J���
            print(col[i].text, file=data)  # �s�Jfor�j�骺���
            data.close()  # ����
            print(col[i].text)  # �C�L�ܲ׺ݾ�
