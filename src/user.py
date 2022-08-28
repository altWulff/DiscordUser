"""Selenium User"""
import random
from datetime import datetime
from time import sleep

import requests
import undetected_chromedriver as webdriver
from rich.console import Console
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SeleniumUser:
    """Selenium User, auto register and login user on browser"""

    def __init__(self, email: str, username: str, password: str):
        self.email = email
        self.username = username
        self.password = password
        self.url = "https://discord.com"
        self.driver = webdriver.Chrome()
        self.driver.set_window_position(0, 0)
        self.actions = ActionChains(self.driver)

        # requests session
        self.session = requests.Session()
        selenium_user_agent = self.driver.execute_script("return navigator.userAgent;")
        self.session.headers.update({"user-agent": selenium_user_agent})
        for cookie in self.driver.get_cookies():
            self.session.cookies.set(
                cookie["name"], cookie["value"], domain=cookie["domain"]
            )

    def _fill_date_fields(self) -> None:
        """Filler date fields with random data"""
        sleep(1.0)
        self.driver.find_elements(By.CLASS_NAME, "css-1hwfws3")[0].click()
        self.actions.send_keys(str(random.randint(1, 12)))
        self.actions.send_keys(Keys.ENTER)
        self.actions.send_keys(str(random.randint(1, 28)))
        self.actions.send_keys(Keys.ENTER)
        self.actions.send_keys(str(random.randint(1990, 2001)))
        self.actions.send_keys(Keys.ENTER)
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(Keys.ENTER)
        self.actions.perform()

    def _fill_reg_fields(self) -> None:
        """
        Filler user registration data: email, username, and password
        """
        self.driver.find_element(By.NAME, "email").send_keys(self.email)
        self.driver.find_element(By.NAME, "username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self._fill_date_fields()
        self.actions.send_keys(Keys.ENTER)

    def _fill_login_field(self) -> None:
        """Filler user login data: email and password"""
        self.driver.find_element(By.NAME, "email").send_keys(self.email)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

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

    def get_token(self) -> str:
        """
        Get user token, after login
        """
        self.session.headers.update({"content-type": "application/json"})
        payload = {
            "login": self.email,
            "password": self.password,
            "undelete": False,
            "captcha_key": "null",
            "login_source": "null",
            "gift_code_sku_id": "null",
        }
        response = self.session.post(f"{self.url}/api/v9/auth/login", data=payload)
        self.log(f"Request status codee {response.status_code}")
        try:
            return response.json()["token"]
        except AttributeError:
            return "<None>"

    @staticmethod
    def log(message) -> None:
        """Messages log"""
        console = Console()
        time = datetime.now().strftime("%H:%M:%S")
        console.print(f"[{time}] {message}")
