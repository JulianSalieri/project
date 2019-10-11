from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()

driver.get('https://accounts.google.com/signin/v2/identifier?hl=ru&continue=https%3A%2F%2Fwww.google.com%3Fhl%3Dru&flowName=GlifWebSignIn&flowEntry=AddSession')
email = driver.find_element_by_css_selector('#identifierId')
email.send_keys('dfwef')

creat_account =  driver.find_element_by_class_name("NlWrkb")
creat_account.click()
time.sleep(1)

choice_account = driver.find_element_by_class_name("jO7h3c")
choice_account.click()
time.sleep(3)

first_name = driver.find_element_by_css_selector("#firstName")
first_name.send_keys('Денис')
time.sleep(1)

last_name = driver.find_element_by_css_selector("#lastName")
last_name.click()
last_name.send_keys('Асеев')
time.sleep(1)

user_name = driver.find_element_by_css_selector('#username')
user_name.send_keys('dsdfsdfsdfsd123123')


user_password = driver.find_element_by_name('Passwd')
user_password.send_keys('!@#$%1234QWERTy')

user_password_return = driver.find_element_by_name('ConfirmPasswd')
user_password_return.send_keys('!@#$%1234QWERTy')
time.sleep(3)

next_registration = driver.find_element_by_class_name("CwaK9")
next_registration.click()
time.sleep(4)

user_number = driver.find_element_by_css_selector('#phoneNumberId') 
user_number.send_keys('89266807190') 

next_registration = driver.find_element_by_class_name("CwaK9") # смс код надо ввести руками, после чего тест продолжится
next_registration.click()
time.sleep(40)

next_registration = driver.find_element_by_class_name("CwaK9")
next_registration.click()
time.sleep(4)

day = driver.find_element_by_css_selector('#day')
day.send_keys('15')

select = Select(driver.find_element_by_tag_name('select'))
select.select_by_value('10')

year = driver.find_element_by_css_selector('#year')
year.send_keys('15')

gender = driver.find_element_by_css_selector('#gender').click()
gender.select_by_value('2')

