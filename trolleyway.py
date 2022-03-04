import time
from alphabets import Alphabet
from unicodedata import name
from numpy import product
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://127.0.0.1:8000/')
driver.maximize_window()
alphabet = Alphabet()
email_address = alphabet.generate_email()

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def wait():
    time.sleep(3)

def register():
    login = driver.find_element_by_xpath("//div[@class='cnt-account']//a[.='Login | Register']")
    login.click()

    wait()

    username = driver.find_element_by_xpath("//div[@class='col-md-6 col-sm-6 create-new-account']//input[@name='email']")
    username.send_keys(f'{email_address}')

    wait()

    name = driver.find_element_by_xpath("//input[@name='name']")
    name.send_keys("Test")

    wait()

    password = driver.find_element_by_xpath("//div[@class='col-md-6 col-sm-6 create-new-account']//input[@name='password']")
    password.send_keys("password")

    wait()

    confirm_password = driver.find_element_by_xpath("//input[@name='password_confirmation']")
    confirm_password.send_keys("password")

    wait()

    submit = driver.find_element_by_xpath("//button[@class='btn-upper btn btn-primary checkout-page-button']")
    submit.click()

def login():
    login = driver.find_element_by_xpath("//div[@class='cnt-account']//a[.='Login | Register']")
    login.click()

    wait()

    username = driver.find_element_by_xpath("//div[@class='col-md-6 col-sm-6 sign-in']//input[@name='email']")
    username.send_keys("princerakomana@gmail.com")

    wait()

    password = driver.find_element_by_xpath("//div[@class='col-md-6 col-sm-6 sign-in']//input[@name='password']")
    password.send_keys("password")

    wait()

    submit = driver.find_element_by_xpath("//button[@class='btn-upper btn btn-primary']")
    submit.click()

def social_login_facebook():
    login = driver.find_element_by_xpath("//div[@class='cnt-account']//a[.='Login | Register']")
    login.click()

    wait()

    facebook = driver.find_element_by_xpath("//a[.='acebook']")
    facebook.click()

def social_login_google():
    login = driver.find_element_by_xpath("//div[@class='cnt-account']//a[.='Login | Register']")
    login.click()

    wait()

    google = driver.find_element_by_xpath("//a[.='oogle']")
    google.click()

def order():
    category = driver.find_element_by_xpath("//i[@class='icon fa fa-laptop']")
    category.click()

    wait()

    product = driver.find_element_by_xpath("//div[@id='grid-container']//a[@href='http://127.0.0.1:8000/detail/01a3b937-3de6-4a32-a628-a56482409e43']/img[@alt='alt']")
    product.click()

    wait()

    add_to_cart = driver.find_element_by_xpath("//div[@class='col-sm-7']//button[@class='btn btn-primary cart-btn']")
    add_to_cart.click()

    cart()

def cart():
    cart = driver.find_element_by_xpath("//div[@class='basket']")
    cart.click()

    wait()
    if check_exists_by_xpath("//div[@class='dropdown dropdown-cart open']//li[1]/div[1]//div[@class='image']"):
        checkout = driver.find_element_by_xpath("//a[.='Checkout']")
        checkout.click()

        wait()

        proceed = driver.find_element_by_xpath("//a[.='PROCCED TO CHEKOUT']")
        proceed.click()

        wait()

    else:
        order()

def checkout():
    payment = driver.find_element_by_xpath("//a[contains(.,'5Checkout')]")
    payment.click()

    wait()

    terms = driver.find_element_by_xpath("//form[contains(.,'I’ve read and accept the  terms & conditions*')]")
    terms.click()

def billing():
    if check_exists_by_xpath("//i[@class='fa fa-trash-o']"):
        checkout()
    else:
        username = driver.find_element_by_xpath("//input[@name='email']")
        username.send_keys(email_address)

        wait()

        name = driver.find_element_by_xpath("//input[@name='first_name']")
        name.send_keys("Cecil")

        wait()

        last_name = driver.find_element_by_xpath("//input[@name='last_name']")
        last_name.send_keys("Laka")

        wait()

        phone_number = driver.find_element_by_xpath("//input[@name='phone_number']")
        phone_number.send_keys("0720606418")

        wait()

        # courier journey
        # option = driver.find_element_by_xpath("//input[@value='courier']")
        # option.click()
        # driver.implicitly_wait(10)

        # address = driver.find_element_by_xpath("//input[@name='address']")
        # address.send_keys("639 Francis Baard, Pretoria")

        # wait()

        # unit = driver.find_element_by_xpath("//input[@name='unit']")
        # unit.send_keys("Vicardia")

        # wait()

        # submit = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
        # submit.click()

        # wait()

        # pep journey
        option = driver.find_element_by_xpath("//input[@value='pep']")
        option.click()
        driver.implicitly_wait(10)

        store = driver.find_element_by_xpath("//select[@name='store']")
        store.click()

        select = Select(store)

        # select by value 
        select.select_by_value('Centurion Mall, Centurion')

        checkout()

register()
cart()
billing()