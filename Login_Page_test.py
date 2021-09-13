from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.chrome.options import Options


#options = Options()
#options.headless = True
#options=options -> skopírovať pred (executable_path)

print("Otváranie driver-u")
driver = webdriver.Chrome(executable_path="C:\Python\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/V4/")
driver.implicitly_wait(10)
print("Štart testu")
time.sleep(1)

from skuska_def import alert_text

#TC-02
print("Štart Testu TC-02")
driver.find_element(By.XPATH, "//input[@name='uid']").send_keys("mr7invalid")
time.sleep(0.7)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("yqUhytY")
time.sleep(0.7)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(0.5)
alert_text(driver)
print("Test TC-02 ukončený")
time.sleep(1)

#TC-03
print("Štart Testu TC-03")
driver.find_element(By.XPATH, "//input[@name='uid']").send_keys("mngr350387")
time.sleep(0.7)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("bsdr47d")
time.sleep(0.7)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(0.5)
alert_text(driver)
print("Test TC-03 ukončený")
time.sleep(1)

#TC-04
print("Štart Testu TC-04")
driver.find_element(By.XPATH, "//input[@name='uid']").send_keys("mngr350387")
time.sleep(0.7)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(0.5)
alert_text(driver)
print("Test TC-04 ukončený")
time.sleep(1)

#TC-05
print("Štart Testu TC-05")
driver.find_element(By.XPATH, "//input[@name='uid']").send_keys("mngr350387")
time.sleep(0.7)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("yqUhytY")
time.sleep(0.7)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(0.5)
time.sleep(1)
driver.find_element(By.XPATH, "//a[.='Log out']").click()
alert_text(driver)
time.sleep(1)
print("Test TC-05 ukončený")
time.sleep(1)

#TC-06
print("Štart Testu TC-06")
driver.find_element(By.XPATH, "//input[@name='uid']").send_keys("yqUhytY")
time.sleep(0.7)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("mngr350387")
time.sleep(0.7)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(0.5)
alert_text(driver)
print("Test TC-06 ukončený")
time.sleep(1)

#TC-07
print("Štart Testu TC-07")
driver.find_element(By.XPATH, "//input[@name='uid']").send_keys("mngr350387")
time.sleep(0.7)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("yqUhytY")
time.sleep(0.7)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(1)
print("Test TC-07 ukončený")
time.sleep(2)
print("Vyhodnotenie testu")
time.sleep(3)
print("Test prebehol v poriadku.")

driver.quit()