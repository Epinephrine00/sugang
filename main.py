
import time
from lib34 import *

with open('password.d', 'r') as f:
    password = f.read().strip()
while True:
    try:
        if 'https://sugang.ut.ac.kr/common/frame.do' in driver.current_url:
            break
    except:
        pass
    driver.get('https://sugang.ut.ac.kr/')
    send('//*[@id="HAKBEON"]', '이곳에 학번을 입력하세요')
    send('//*[@id="PWD"]', password)

    click('//*[@id="loginBtn"]')
    time.sleep(2)
    try:
        driver.switch_to.alert.accept()
        driver.switch_to.window(driver.window_handles[0])
    except:
        pass

driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="frameMain2"]'))
#click('//*[@id="tab_left"]/tbody/tr[1]/th[2]/input')

driver.execute_script("doSincheong('1','009199','1','','','','','','');")
#driver.close()

# click('//*[@id="tab_left"]/tbody/tr[1]/th[2]/input')
# time.sleep(0.2)
# click('/html/body/div/form/table/tbody/tr[3]/td[11]/input')

#doSincheong('1','009508','1','','','','','','');

