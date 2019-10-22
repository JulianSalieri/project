from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import setting

driver = webdriver.Chrome()
#РАЗВОРАЧИВАЕТ ОКНО БРАУЗЕРА НА ВЕСЬ ЭКРАН
#driver.maximize_window()
#myHeader= {}
#myHeader['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
driver.get('https://accounts.google.com/signin/v2/identifier?hl=ru&continue=https%3A%2F%2Fwww.google.com%3Fhl%3Dru&flowName=GlifWebSignIn&flowEntry=AddSession')
email = driver.find_element_by_css_selector('#identifierId')
email.send_keys('Hello')

def creat_account():
    try:
        creat_account =  driver.find_element_by_class_name("NlWrkb")
        creat_account.click()
        time.sleep(1)
        if True:
            choice_account()
        else:
            print("ScreenShot")
    except NoSuchElementException:
        print("Error blay")

def choice_account():
    try:
        choice_account = driver.find_element_by_class_name("jO7h3c")
        choice_account.click()
        time.sleep(3)
        if True:
            first_name()
        else:
            driver.save_screenshot('screenie.png')
    except NoSuchElementException:
        print("Error")
#ВВОД ИМЕНИ
def first_name():
    try:
        first_name = driver.find_element_by_css_selector("#firstName")
        first_name.click()
        first_name.send_keys(setting.MY_NAME)
        time.sleep(1)
        if True:
            last_name()
        else:
            driver.save_screenshot('screenie_2.png')
    except NoSuchElementException:
        print("Error")
#ВВОД ФАМИЛИИ
def last_name():
    try:
        last_name = driver.find_element_by_css_selector("#lastName")
        last_name.click()
        last_name.send_keys(setting.MY_LAST_NAME)
        time.sleep(1)
        if True:
            user_name()
        else:
            driver.save_screenshot('screenie_3.png')
    except NoSuchElementException:
        print("Error")
#АДРЕС ПОЧТЫ
def user_name():
    try:
        user_name = driver.find_element_by_css_selector('#username')
        user_name.send_keys(setting.MAIL_NAME)
        if True:
            user_password()
        else:
            driver.save_screenshot('screenie_4.png')
    except NoSuchElementException:
        print("Error")
#ПАРОЛЬ
def user_password():
    try:
        user_password = driver.find_element_by_name('Passwd')
        user_password.send_keys(setting.MAIL_PASS)
        if True:
            user_password_return()
        else:
            driver.save_screenshot('screenie_5.png')
    except NoSuchElementException:
        print("Error")
#ПОВТОРЕНИЕ ПАРОЛЯ
def user_password_return():
    try:
        user_password_return = driver.find_element_by_name('ConfirmPasswd')
        user_password_return.send_keys(setting.MAIL_PASS)
        time.sleep(3)
        if True:
            next_registration()
        else:
            driver.save_screenshot('screenie_6.png')
    except NoSuchElementException:
        print("Error")
#КНОПКА ДАЛЕЕ
def next_registration():
    try:
        next_registration = driver.find_element_by_class_name("CwaK9")
        next_registration.click()
        time.sleep(3)
        if True:
            user_number()
        else:
            driver.save_screenshot('screenie_7.png')
    except NoSuchElementException:
        print("Error")
#ВВОД НОМЕРА ТЕЛЕФОНА
def user_number():
    try:
        user_number = driver.find_element_by_css_selector('#phoneNumberId')
        user_number.send_keys(setting.MY_NUMBER)
        time.sleep(3)
        if True:
            next_registration_two_step()
        else:
            driver.save_screenshot('screenie_8.png')
    except NoSuchElementException:
        print("Error")
#НАЖАТИЕ НА КНОПКУ ДАЛЕЕ ПОСЛЕ ВВОДА НОМЕРА ТЕЛЕФОНА
def next_registration_two_step():
    try:
        next_registration_two_step = driver.find_element_by_class_name("CwaK9")
        next_registration_two_step.click()
        time.sleep(40)
        if True:
            next_registration_three()
        else:
            driver.save_screenshot('screenie_9.png')
    except NoSuchElementException:
        print("Error")
#НАЖАТИЕ НА КНОПКУ ДАЛЕЕ ПОСЛЕ ВВОДА КОДА ИЗ СМС
def next_registration_three():
    try:
        next_registration_three = driver.find_element_by_class_name("CwaK9")
        next_registration_three.click()
        time.sleep(3)
        if True:
            next_registration_two_step()
        else:
            driver.save_screenshot('screenie_10.png')
    except NoSuchElementException:
        print("Error")

def day():
    try:
        day = driver.find_element_by_css_selector('#day')
        day.send_keys(setting.MY_DAY)
        time.sleep(1)
        if True:
            select()
        else:
            driver.save_screenshot('screenie_11.png')
    except NoSuchElementException:
        print("Error")

def select():
    try:
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_value(setting.MY_MOUNTH)
        time.sleep(1)
        if True:
            year()
        else:
            driver.save_screenshot('screenie_12.png')
    except NoSuchElementException:
        print("Error")

def year():
    try:
        year = driver.find_element_by_css_selector('#year')
        year.send_keys(setting.MY_YEAR)
        time.sleep(1)
        if True:
            gender()
        else:
            driver.save_screenshot('screenie_13.png')
    except NoSuchElementException:
        print("Error")

def gender():
    try:
        gender = driver.find_element_by_css_selector('#gender>option:nth-child(3)').click()
        time.sleep(1)
        if True:
            gender()
        else:
            driver.save_screenshot('screenie_14.png')
    except NoSuchElementException:
        print("Error")

def next_registration_four():
    try:
        next_registration_four =  driver.find_element_by_class_name("RveJvd.snByac").click()
        time.sleep(1)
        if True:
            time.sleep(5)
            next_registration_four =  driver.find_element_by_class_name("RveJvd.snByac").click()
        else:
            driver.save_screenshot('screenie_15.png')
    except NoSuchElementException:
        print("Error")

creat_account()


#    scr = 'screenie'+ 'i' +'.png'
#    screen =  driver.save_screenshot('screenie.png')


#class="RveJvd snByac 