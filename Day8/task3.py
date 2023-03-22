import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.online.citibank.co.in/")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@class='fancybox-item fancybox-close']").click()
driver.find_element(By.XPATH, "//span[contains(text(),'Login')]").click()

print(driver.window_handles)

# switch to window-2
driver.switch_to.window(driver.window_handles[1])

# click on forget user id and select Credit card from dropdown
driver.find_element(By.XPATH, "//div[contains(text(),' Forgot User ID? ')]").click()
driver.find_element(By.LINK_TEXT, "select your product type").click()
driver.find_element(By.LINK_TEXT, "Credit Card").click()

# Enter Credit Card Number
driver.find_element(By.NAME, "citiCard1").send_keys(4545)
driver.find_element(By.NAME, "citiCard2").send_keys(5656)
driver.find_element(By.NAME, "citiCard3").send_keys(8887)
driver.find_element(By.NAME, "citiCard4").send_keys(9998)
driver.find_element(By.NAME, "CCVNO").send_keys(123)


driver.execute_script("document.querySelector('#bill-date-long').value='14/04/2022'")

driver.find_element(By.XPATH, "//input[@value='PROCEED']").click()
error_propmt=driver.find_element(By.XPATH,"//li[contains(text(),'Terms')]").text
print(error_propmt)


time.sleep(10)
driver.quit()