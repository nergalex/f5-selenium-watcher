import pprint
import time
import unittest
import random
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import urllib.parse as urlparse
from urllib.parse import parse_qs
import json
import requests
import re


class Flow1(unittest.TestCase):

    def setUp(self):
        global URI, LOGIN_USER, LOGIN_PASSWORD, LOGIN_BIRTHDAY, CAPTCHA_API_KEY, solver, USER_AGENT, LOOP_ITERATION
        URI = "https://www.fdj.fr"
        LOGIN_USER = "nergalex@hotmail.com"
        LOGIN_PASSWORD = "K4moul0x!"
        LOGIN_BIRTHDAY = "24/06/1981"
        CAPTCHA_API_KEY = "INPUT"

        # local
        PATH = "./_files/chromedriver.exe"
        USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-web-security")
        options.add_argument("---user-data-dir=./_chromeTemp")
        options.add_argument("--disable-features=CrossSiteDocumentBlockingIfIsolating")
        options.add_argument("--disable-site-isolation-for-policy")
        options.add_argument("–-allow-file-access-from-files")
        options.add_argument("--auto-open-devtools-for-tabs")
        options.add_argument("--show-taps")
        options.add_experimental_option('w3c', False)

        self.driver = webdriver.Chrome(
            executable_path=PATH,
            options=options
        )
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": USER_AGENT})
        print("Run Selenium bot with User Agent: %s" % self.driver.execute_script("return navigator.userAgent;"))

    def test_login(self):
        self.session = requests.session()

        # goto welcome page
        self.driver.get(URI)
        time.sleep(2)

        # Accept data privacy
        element = self.getElementId("popin_tc_privacy_button_2")
        self.clickButton(element)

        infinite = True
        while infinite:

            # tous-les-jeux
            tmp_uri = URI + "/tous-les-jeux?t=&o=new"
            self.driver.get(tmp_uri)
            time.sleep(1)

            # tous-les-jeux-de-tirage
            element = self.getElementId("tous-les-jeux-de-tirage")
            self.clickButton(element)
            time.sleep(0.25)

            # tous-les-jeux-bingo-live-multijoueur
            element = self.getElementId("tous-les-jeux-bingo-live-multijoueur")
            self.clickButton(element)
            time.sleep(0.25)

            # euromillions-my-million
            tmp_uri = URI + "/jeux-de-tirage/euromillions-my-million"
            self.driver.get(tmp_uri)
            time.sleep(1)

            # loto
            tmp_uri = URI + "/jeux-loto"
            self.driver.get(tmp_uri)
            time.sleep(1)

            # illiko
            tmp_uri = URI + "/jeux-illiko"
            self.driver.get(tmp_uri)
            time.sleep(1)

            # bingo-live
            tmp_uri = URI + "/bingo-live-et-multijoueur/bingo-live"
            self.driver.get(tmp_uri)
            time.sleep(1)

            # bingo-live game
            tmp_uri = URI + "/bingo-live-et-multijoueur/bingo-live/bingo-live-one"
            self.driver.get(tmp_uri)
            time.sleep(6)

            # keno
            tmp_uri = URI + "/jeux-keno"
            self.driver.get(tmp_uri)
            time.sleep(1)

            # resultats
            tmp_uri = URI + "/jeux-de-tirage/resultats"
            self.driver.get(tmp_uri)
            time.sleep(1)

            # mag
            tmp_uri = URI + "/mag"
            self.driver.get(tmp_uri)
            time.sleep(1)

            # User account
            element = self.getElementClass("icon-header-user")
            self.clickButton(element)

            # Login
            element = self.getElementId("wsi-login-credentials-form-email-input-input")
            self.setForm(element=element, input_data=LOGIN_USER)

            # Password
            element = self.getElementId("wsi-login-credentials-form-password-input-input")
            self.setForm(element=element, input_data=LOGIN_PASSWORD)

            # Birth date
            element = self.getElementId("wsi-login-credentials-form-birthdate-input-input")
            self.setForm(element=element, input_data=LOGIN_BIRTHDAY)

            # Submit
            element = self.getElementId("wsi-authenticate-button")
            self.clickButton(element)
            time.sleep(1)

            # Skip
            # element = self.getElementId("wsi-post-authentication-skip-optional-layers")
            # if element is not None:
            #     self.clickButton(element)
            #     time.sleep(1)

            # MyAccount
            element = self.getElementClass("main-nav_connect-user_myaccount")
            self.clickButton(element)
            time.sleep(2)

            # Retrait
            element = self.getElementId("wsi-connected-layer-summary-wallets-withdrawal-button")
            self.clickButton(element)
            time.sleep(1)

            # Completer
            element = self.getElementClass("action-link-btFournirMapiece-origin")
            self.clickButton(element)
            time.sleep(1)

            # User account
            element = self.getElementClass("main-nav_connect-user_notif-icon")
            self.clickButton(element)

            # User account
            element = self.getElementId("wsi-connected-layer-summary-disconnect-button")
            self.clickButton(element)

    def tearDown(self):
        self.driver.close()

    def clickButton(self, element):
        interval_think = random.uniform(1.1, 1.5)
        interval_get_mouse = random.uniform(1.1, 1.5)
        interval_click = random.uniform(0.1, 0.3)
        offset_x = random.uniform(1, 10)
        offset_y = random.uniform(1, 10)

        ActionChains(self.driver).pause(interval_think).\
            move_by_offset(offset_x, offset_y).\
            move_to_element(element).pause(interval_get_mouse).\
            click_and_hold(element).pause(interval_click).release(element).\
            perform()

    def setForm(self, element, input_data):
        interval_think = random.uniform(1.1, 1.5)
        interval_get_mouse = random.uniform(1.1, 1.5)
        interval_click = random.uniform(0.1, 0.3)
        offset_x = random.uniform(50, 100) * -1
        offset_y = random.uniform(50, 100) * -1

        ActionChains(self.driver).pause(interval_think).\
            move_by_offset(offset_x, offset_y).\
            move_to_element(element).pause(interval_get_mouse).\
            click_and_hold(element).pause(interval_click).release(element).\
            perform()
        element.clear()
        string = []
        string[:0] = input_data
        for character in string:
            element.send_keys(character)
            interval = random.uniform(0.1, 0.35)
            time.sleep(interval)

    def getElementId(self, element_id):
        try:
            WebDriverWait(self.driver, 2).until(
                expected_conditions.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            print("Oops!  Too long to retrieve element '%s'" % element_id)
        try:
            element = self.driver.find_element_by_id(element_id)
        except NoSuchElementException:
            print("Oops!  There is no valid element '%s'" % element_id)
            return None
        return element

    def getElementTagName(self, tag_name):
        try:
            WebDriverWait(self.driver, 2).until(
                expected_conditions.presence_of_element_located((By.TAG_NAME, tag_name))
            )
        except TimeoutException:
            print("Oops!  Too long to retrieve element '%s'" % tag_name)
        try:
            elements = self.driver.find_elements_by_tag_name(tag_name)
        except NoSuchElementException:
            print("Oops!  There is no valid element '%s'" % tag_name)
            return None
        return elements

    def getElementClass(self, element_class):
        try:
            WebDriverWait(self.driver, 2).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, element_class))
            )
        except TimeoutException:
            print("Oops!  Too long to retrieve element '%s'" % element_class)
        try:
            element = self.driver.find_element_by_class_name(element_class)
        except NoSuchElementException:
            print("Oops!  There is no valid element '%s'" % element_class)
        return element

    def getElementName(self, element_name):
        try:
            WebDriverWait(self.driver, 2).until(
                expected_conditions.presence_of_element_located((By.NAME, element_name))
            )
        except TimeoutException:
            print("Oops!  Too long to retrieve element '%s'" % element_name)
        try:
            element = self.driver.find_element_by_name(element_name)
        except NoSuchElementException:
            print("Oops!  There is no valid element '%s'" % element_name)
        return element


if __name__ == "__main__":

    unittest.main()
