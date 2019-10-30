from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import setting
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='autotestlogneg.log',
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


# Этот телефонный номер был использован слишком много раз.
# QWERTYa12345
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
            next_registration1()
        else:
            driver.save_screenshot('screenie.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_3.png')
        driver.quit()


def next_registration1():
    try:
        next_registration = driver.find_element_by_class_name("CwaK9")
        next_registration.click()
        logging.info(u'Шаг7: Переход на следующий шаг')
        time.sleep(3)
        a = 0
        while a != 1:
            if driver.find_element_by_class_name('GQ8Pzc'):
                logging.error(u'!!!Element not founddsds!!!!22')
                if driver.find_element_by_xpath('//div[text()="Укажите имя"]'):
                    logging.error(u'Укажите имя')
                    if driver.find_element_by_xpath('//div[text()="Укажите фамилию"]'):
                        logging.error(u'Укажите фамилию')
                        if driver.find_element_by_xpath('//div[text()="Укажите адрес Gmail"]'):
                            logging.error(u'!Укажите адрес Gmail')
                            if driver.find_element_by_xpath('//div[text()="Введите пароль"]'):
                                logging.error(u'Введите пароль')
                                if True:
                                    a += 1
                                    logging.error(u'STOP')
                                    first_name()

    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_7.png')
        driver.quit()


def first_name():
    try:
        first_name = driver.find_element_by_css_selector("#firstName")
        first_name.click()
        first_name.send_keys(setting.MY_NAME)
        logging.info(u'Шаг4: Ввод имени пользователя')
        time.sleep(2)
        if True:
            last_name()
        else:
            driver.save_screenshot('screenie_2.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_4.png')
        driver.quit()


def last_name():
    try:
        last_name = driver.find_element_by_css_selector("#lastName")
        last_name.click()
        last_name.send_keys(setting.MY_LAST_NAME)
        logging.info(u'Шаг4: Ввод фамилии пользователя')
        time.sleep(1)
        if True:
            user_name()
        else:
            driver.save_screenshot('screenie_3.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_4.png')
        driver.quit()


def user_name():
    try:
        user_name = driver.find_element_by_css_selector('#username')
        user_name.send_keys(setting.MAIL_NAME)
        logging.info(u'Шаг5: Ввод адрес почты')
        time.sleep(2)
        if True:
            user_password()
        else:
            driver.save_screenshot('screenie_4.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_5.png')
        driver.quit()


def user_password():
    try:
        user_password = driver.find_element_by_name('Passwd')
        user_password.send_keys(setting.MAIL_PASS)
        logging.info(u'Шаг6: Ввод пароля пользователя')
        time.sleep(2)
        if True:
            user_password_return()
        else:
            driver.save_screenshot('screenie_5.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_6.png')
        driver.quit()


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
            driver.find_element_by_xpath('//div[text()="Имя пользователя должно содержать от 6 до 30 символов."]')
        else:
            driver.save_screenshot('screenie_7.png')
    except NoSuchElementException:
        logging.error(u'Element not found')
        driver.save_screenshot('notfound_7.png')
        driver.quit()


creat_account()

# Имя пользователя должно содержать от 6 до 30 символов.
