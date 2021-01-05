from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import playsound
import sys
import time
from datetime import datetime
sys.setrecursionlimit(10000)

class bol():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = None


    def login(self):
        self.open_browser()
        self.driver.get("https://www.bol.com/nl/account/login.html?redirectUrl=https%3A%2F%2Fwww.bol.com%2Fnl%2Frnwy%2Faccount%2Foverzicht")

        username_input = '//*[@id="login_email"]'
        password_input = '//*[@id="login_password"]'
        submit_button = '//*[@id="existinguser"]/fieldset/div[3]/input'


        state = self.driver.execute_script('return document.readyState')
        if state == 'complete':
            self.driver.find_element_by_xpath(username_input).send_keys(self.username)
            self.driver.find_element_by_xpath(password_input).send_keys(self.password)
            self.driver.find_element_by_xpath(submit_button).click()

            time.sleep(0.1)

            cookie_message_button = '//*[@id="modalWindow"]/div[2]/div[2]/wsp-consent-modal/div[2]/div/div[1]/button/span'
            self.driver.find_element_by_xpath(cookie_message_button).click()

            time.sleep(0.1)



    def orderProductById(self, productId, directPay=0):
        self.login()

        time.sleep(0.1)

        self.driver.get("https://www.bol.com/nl/p/product/"+str(productId)+"/")

        # wait for dom loaded, inject headless detection script and submit form
        state = self.driver.execute_script('return document.readyState')
        if state == 'complete':
            cart_button = '//*[@id="'+str(productId)+'"]'
            self.driver.find_element_by_xpath(cart_button).click()

            time.sleep(0.2)
            go_to_cart_button = '/html/body/div[4]/div[2]/div[3]/div[1]/div/div[2]/div/a'
            self.driver.find_element_by_xpath(go_to_cart_button).click()

            time.sleep(0.2)
            continue_order_button = '//*[@id="continue_ordering_bottom"]'
            self.driver.find_element_by_xpath(continue_order_button).click()

            if directPay > 0:
                time.sleep(0.2)
                to_payment_button = '//*[@id="executepayment"]/form/div/button'
                self.driver.find_element_by_xpath(to_payment_button).click()

            time.sleep(10)
            ## generate error to not close te browser
            self.driver.find_element_by_xpath(continue_order_button).click()


    ## Start Browser
    def open_browser(self):

        DRIVER_PATH = '/usr/local/bin/chromedriver'
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--auto-open-devtools-for-tabs")
        options.add_argument("--whitelisted-ips")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,800")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        self.driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})

    def check_availabity_of_productId(self, productId, check_time=120, attempt=0):
        print(attempt)
        attempt = attempt +1

        DRIVER_PATH = '/usr/local/bin/chromedriver'
        options = Options()
        options.headless = True
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--auto-open-devtools-for-tabs")
        options.add_argument("--whitelisted-ips")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,800")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        self.driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})

        self.driver.get("https://www.bol.com/nl/p/sony-playstation-5-console/" + str(productId) + "/?ruleRedirect=1&sI=playstation%205&variants=")
        state = self.driver.execute_script('return document.readyState')
        if state == 'complete':
            cookie_message_button = '//*[@id="modalWindow"]/div[2]/div[2]/wsp-consent-modal/div[2]/div/div[1]/button/span'
            self.driver.find_element_by_xpath(cookie_message_button).click()

            cart_button = '//*[@id="' + str(productId) + '"]'
            try:
                self.driver.find_element_by_xpath(cart_button).click()
                return 'Available !'
            except NoSuchElementException:
                date_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
                print("Timestamp: ", date_time)
                print('Not available check over ' + str(check_time) + ' seconds')
                self.driver.close()
                time.sleep(check_time)
                self.check_availabity_of_productId(productId, check_time, attempt)
            except:
                playsound('sounds/bad.mp3')