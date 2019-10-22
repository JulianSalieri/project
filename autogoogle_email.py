from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import setting

driver = webdriver.Chrome()
driver.get(
    'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

email = driver.find_element_by_css_selector('#identifierId')
email.send_keys(setting.REG_MAIL)
time.sleep(1)

next_authorization = driver.find_element_by_class_name("RveJvd.snByac").click()
time.sleep(1)

pswd = driver.find_element_by_css_selector('div>.whsOnd.zHQkBf')
pswd.send_keys(setting.REGPASS_MAIL)

next_authorization_ = driver.find_element_by_class_name("RveJvd.snByac").click()
time.sleep(10)

# next_authorization_2 =  driver.find_element_by_class_name("RveJvd.snByac").click()
# time.sleep(10)

mail_new = driver.find_element_by_class_name("T-I.J-J5-Ji.T-I-KE.L3").click()
time.sleep(1)

address_of_the_recipienе = driver.find_element_by_class_name("div.wO.nr.l1>.vO").click()
address_of_the_recipienе.send_keys(setting.OUT_MAIL)
time.sleep(1)

#while address_of_the_recipienе == True:
    #address_of_the_recipienе = driver.find_element_by_class_name("div.wO.nr.l1>.vO").click()
