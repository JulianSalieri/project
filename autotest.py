from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import setting
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='autotestlog.log',
                    filemode="w")

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options,
                          executable_path=r'C:\chromedriver\chromedriver.exe')

# РАЗВОРАЧИВАЕТ ОКНО БРАУЗЕРА НА ВЕСЬ ЭКРАН
# driver.maximize_window()
# myHeader= {}
# myHeader['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
'''def setup_class(self):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("enable-automation")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=chrome_options,
                              executable_path=r'C:\chromedriver\chrome.exe')
    driver = browser.set_driver(driver)
    return driver'''

driver.get(
    'https://accounts.google.com/signin/v2/identifier?hl=ru&continue=https%3A%2F%2Fwww.google.com%3Fhl%3Dru&flowName=GlifWebSignIn&flowEntry=AddSession')
email = driver.find_element_by_css_selector('#identifierId')
email.send_keys('Hello')
logging.info(u'Шаг1: Ввод приветсвия')



# Регистрации почты
def creat_account():
    try:
        creat_account = driver.find_element_by_class_name("NlWrkb")
        creat_account.click()
        logging.info(u'Шаг2: Выбор типа акаунта для регистрации ')
        time.sleep(3)
        if True:
            choice_account()
        else:
            print("ScreenShot")
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_2.png')
        driver.quit()


# Выбор типа акаунта для регистрации

def choice_account():
    try:
        choice_account = driver.find_element_by_class_name("jO7h3c")
        choice_account.click()
        logging.info(u'Шаг3: Выбор типа акаунта для регистрации ')
        time.sleep(3)
        if True:
            first_name()
        else:
            driver.save_screenshot('screenie.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_3.png')
        driver.quit()


# ВВОД ИМЕНИ
def first_name():
    try:
        first_name = driver.find_element_by_css_selector("#firstName")
        first_name.click()
        first_name.send_keys(setting.MY_NAME)
        logging.info(u'Шаг4: Ввод имени пользователя')
        time.sleep(3)
        if True:
            last_name()
        else:
            driver.save_screenshot('screenie_2.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_4.png')
        driver.quit()


# ВВОД ФАМИЛИИ
def last_name():
    try:
        last_name = driver.find_element_by_css_selector("#lastName")
        last_name.click()
        last_name.send_keys(setting.MY_LAST_NAME)
        logging.info(u'Шаг4: Ввод фамилии пользователя')
        time.sleep(3)
        if True:
            user_name()
        else:
            driver.save_screenshot('screenie_3.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_4.png')
        driver.quit()


# АДРЕС ПОЧТЫ
def user_name():
    try:
        user_name = driver.find_element_by_css_selector('#username')
        user_name.send_keys(setting.MAIL_NAME)
        logging.info(u'Шаг5: Ввод адрес почты')
        time.sleep(3)
        if True:
            user_password()
        else:
            driver.save_screenshot('screenie_4.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_5.png')
        driver.quit()


# ПАРОЛЬ
def user_password():
    try:
        user_password = driver.find_element_by_name('Passwd')
        user_password.send_keys(setting.MAIL_PASS)
        logging.info(u'Шаг6: Ввод пароля пользователя')
        time.sleep(3)
        if True:
            user_password_return()
        else:
            driver.save_screenshot('screenie_5.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_6.png')
        driver.quit()


# ПОВТОРЕНИЕ ПАРОЛЯ
def user_password_return():
    try:
        user_password_return = driver.find_element_by_name('ConfirmPasswd')
        user_password_return.send_keys(setting.MAIL_PASS)
        logging.info(u'Шаг7: Подтверждение пароля')
        time.sleep(3)
        if True:
            next_registration()
        else:
            driver.save_screenshot('screenie_6.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_7.png')
        driver.quit()


# КНОПКА ДАЛЕЕ
def next_registration():
    try:
        next_registration = driver.find_element_by_class_name("CwaK9")
        next_registration.click()
        logging.info(u'Шаг7: Переход на следующий шаг')
        time.sleep(3)
        if True:
            user_number()
        else:
            driver.save_screenshot('screenie_7.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_7.png')
        driver.quit()


# ВВОД НОМЕРА ТЕЛЕФОНА
def user_number():
    try:
        user_number = driver.find_element_by_css_selector('#phoneNumberId')
        user_number.send_keys(setting.MY_NUMBER)
        logging.info(u'Шаг8: Ввод номера телефона')
        time.sleep(3)
        if True:
            next_registration_two_step()
        else:
            driver.save_screenshot('screenie_8.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_8.png')
        driver.quit()


# НАЖАТИЕ НА КНОПКУ ДАЛЕЕ ПОСЛЕ ВВОДА НОМЕРА ТЕЛЕФОНА
def next_registration_two_step():
    try:
        next_registration_two_step = driver.find_element_by_class_name("CwaK9")
        next_registration_two_step.click()
        logging.info(u'Шаг9: Переход к форме ввода смс кода')
        time.sleep(5)
        if True:
            driver.find_element_by_xpath('//div[text()="Этот номер нельзя использовать для подтверждения ID."]') #or driver.find_element_by_xpath('//div[text()="Этот телефонный номер был использован слишком много раз."]')
            driver.save_screenshot('screenie_919.png') and driver.quit()
            logging.error(u'Ошибка при вводе номера телефона')
        else:
            next_registration_three()
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_9.png')
        #driver.quit()


# НАЖАТИЕ НА КНОПКУ ДАЛЕЕ ПОСЛЕ ВВОДА КОДА ИЗ СМС
def next_registration_three():
    try:
        next_registration_three = driver.find_element_by_class_name("CwaK9")
        next_registration_three.click()
        logging.info(u'Шаг10: Подтверждение смс кода')
        time.sleep(3)
        if True:
            next_registration_two_step()
        else:
            driver.save_screenshot('screenie_10.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_10.png')
        driver.quit()


def day():
    try:
        day = driver.find_element_by_css_selector('#day')
        day.send_keys(setting.MY_DAY)
        logging.info(u'Шаг11: Ввод даты рождения')
        time.sleep(1)
        if True:
            select()
        else:
            driver.save_screenshot('screenie_11.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_11.png')
        driver.quit()


def select():
    try:
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_value(setting.MY_MOUNTH)
        logging.info(u'Шаг12: Ввод месяца рождения')
        time.sleep(1)
        if True:
            year()
        else:
            driver.save_screenshot('screenie_12.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_12.png')
        driver.quit()


def year():
    try:
        year = driver.find_element_by_css_selector('#year')
        year.send_keys(setting.MY_YEAR)
        logging.info(u'Шаг13: Ввод года рождения')
        time.sleep(1)
        if True:
            gender()
        else:
            driver.save_screenshot('screenie_13.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_13.png')
        driver.quit()


def gender():
    try:
        gender = driver.find_element_by_css_selector('#gender>option:nth-child(3)').click()
        logging.info(u'Шаг13: Выбор пола')
        time.sleep(1)
        if True:
            next_registration_four()
        else:
            driver.save_screenshot('screenie_14.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_14.png')
        driver.quit()


def next_registration_four():
    try:
        next_registration_four = driver.find_element_by_class_name("RveJvd.snByac").click()
        logging.info(u'Шаг15: Переход к следующей форме завершения регистрации')
        time.sleep(10)
        if True:
            next_registration_four = driver.find_element_by_class_name("RveJvd.snByac").click()
            logging.info(u'Шаг16: Завершение регистрации')
        else:
            driver.save_screenshot('screenie_15.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_15.png')
        driver.quit()


creat_account()



