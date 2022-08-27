"""Selenium User"""
import json
import random

import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import undetected_chromedriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
from rich.console import Console


class SeleniumUser:
    """Selenium User, auto register and login user on browser"""
    def __init__(
            self, email: str, username: str, password: str, url: str="https://discord.com"
    ):
        self.email = email
        self.username = username
        self.password = password
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.set_window_position(0, 0)
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

        # requests session
        self.session = requests.Session()
        selenium_user_agent = self.driver.execute_script(
            "return navigator.userAgent;")
        self.session.headers.update({"user-agent": selenium_user_agent})
        for cookie in self.driver.get_cookies():
            self.session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])

    def _fill_date_fields(self) -> None:
        """Filler date fields with random data"""
        self.driver.find_elements(By.CLASS_NAME, 'css-1hwfws3')[0].click()
        self.actions.send_keys(str(random.randint(1, 12)))
        self.actions.send_keys(Keys.ENTER)
        self.actions.send_keys(str(random.randint(1, 28)))
        self.actions.send_keys(Keys.ENTER)
        self.actions.send_keys(
            str(random.randint(1990, 2001)))
        self.actions.send_keys(Keys.ENTER)
        self.actions.send_keys(Keys.TAB)

    def _fill_reg_fields(self) -> None:
        """
        Filler user registration data: email, username, and password
        """
        self.driver.find_element(By.NAME, 'email').send_keys(self.email)
        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self._fill_date_fields()
        self.actions.send_keys(Keys.ENTER)

    def _fill_login_field(self) -> None:
        """Filler user login data: email and password"""
        self.driver.find_element(By.NAME, 'email').send_keys(self.email)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.NAME, 'password').send_keys(Keys.ENTER)

    def register(self) -> None:
        """
        Registration user
        """
        self.log(f"Registration {self.username.capitalize()} to {self.url} ...")
        self.driver.get(f"{self.url}/register")
        self._fill_reg_fields()

    def login(self) -> None:
        """
        Login user
        """
        self.log(f"Login {self.username.capitalize()} to {self.url} ...")
        self.driver.get(f"{self.url}/login")
        self._fill_login_field()

        payload = {
            "login": self.email,
            "password": self.password,
            "undelete": "false",
            "captcha_key": "null",
            "login_source": "null",
            "gift_code_sku_id": "null"
        }
        headers = {
            ""
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'referer': 'https://www.google.com/'
        }

        #resp = self.session.post("https://discord.com/api/v9/auth/login", data=payload, headers=headers)
        #print(resp, resp.headers)

    def get_token(self) -> str:
        """
        Get user token, after login
        """
        current_url = self.driver.current_url
        print(current_url)
        self.wait.until(EC.url_changes(current_url))
        self.wait.until(EC.url_to_be(f"{self.url}/channels/@me"))
        current_url = self.driver.current_url
        print(current_url)
        token = self.driver.execute_script(f"return window.localStorage.getItem('token');")
        return token

    @staticmethod
    def log(message) -> None:
        """Messages log"""
        console = Console()
        time = datetime.now().strftime('%H:%M:%S')
        console.print(f'[{time}] MESSAGE: {message}')

