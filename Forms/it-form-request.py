from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import chromedriver_binary  # Adds chromedriver binary to path
import functools #for error handling
import re

from time import sleep #to pause execution

def exception(fn):
    """
    A decorator that wraps the passed in function and logs exceptions should one occur
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except NoSuchElementException:
            print("There was a NoSuchElementException in " + fn.__name__) 

    return wrapper

class IT_Request_Automator():
	browser = ""
	user_name, email, phone = "", "", ""
	"""
	A Class for automating it requests
	"""
	def __init__(self):
		self.user_name = "Jeremy Marino"
		self.user_email = "Jeremy@ccbf.net"
		self.user_phone = "951-764-2881"
		# self.browser = ""

	def start_browser(self):
		self.browser = webdriver.Chrome()
		return self.browser

	def is_valid_email(self, email_input):
		email_regex = re.compile(r"\b\w+@{1}\w+.{1}\w+\b")
		match = email_regex.search(email_input)
		if match:
			return True
		return False

	def get_email(self):
		self.user_email = input("What's the email? ")
		if not (self.is_valid_email(self.user_email)):
			print("That's not valid try again\n")
			self.get_email()

		return self.user_email

	def get_user_info(self):
		# global user_name, user_email, user_phone

		default_email = input("Do you want to proceed with e-mail 'Jeremy@ccbf.net'? (y/n): ")
		if default_email == "y":
			self.email = "Jeremy@ccbf.net"
		else: 
			self.email = self.get_email()

	@exception
	def get_request_page(self):
		self.browser.get("https://ccbf.atlassian.net/servicedesk/customer/portal/2/group/2/create/10002")# go straifght to the page
		return self.browser

	@exception
	def type_email(self):
		email_field = self.browser.find_element_by_css_selector("#email")
		email_field.click()
		email_field.send_keys(self.user_email)

def main():
    it_form = IT_Request_Automator()
    it_form.get_user_info()
    global browser_automate #stops browser from closing
    browser_automate = it_form.start_browser()
    it_form.get_request_page()
    it_form.type_email()

main()

