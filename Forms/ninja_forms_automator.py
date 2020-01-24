from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import chromedriver_binary  # Adds chromedriver binary to path
import functools #for error handling
import re

from time import sleep #to pause execution

class Ninja_Forms_Automator():
	browser = ""
	user_name, email, phone = "", "", ""
	"""
	A Class for automatic generic ninja forms information
	"""
	def __init__(self):
		self.user_name = "Jeremy Marino"
		self.user_email = "Jeremy@ccbf.net"
		self.user_phone = "951-764-2881"
		# self.browser = ""

	def start_browser(self):
		self.browser = webdriver.Chrome()
		return self.browser

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

	def is_valid_email(self, email_input):
		email_regex = re.compile(r"\b\w+@{1}\w+.{1}\w+\b")
		match = email_regex.search(email_input)
		if match:
			return True
		return False

	def is_valid_phone(self, phone_input):
		standard_phone_regex = re.compile(r"\b\d{3}?-?\d{3}-?\d{4}\b")
		parentheses_phone_regex = re.compile(r"\(\d{3}\)\s?\d{3}\s?-?\d{4}\b")
		whitespace_phone_regex = re.compile(r"\b\d{3}\s?\d{3}\s?\d{4}\b")
		match1 = standard_phone_regex.search(phone_input)
		match2 = parentheses_phone_regex.search(phone_input)
		match3 = whitespace_phone_regex.search(phone_input)
		if match1 or match2 or match3:
			return True
		return False

	def get_default_user_values(self):
		# global user_name, user_email, user_phone
		print("Proceeding with default values")

		self.user_name = "Jeremy Marino"
		self.user_email = "Jeremy@ccbf.net"
		self.user_phone = "951-764-2881"

	def get_email(self):
		self.user_email = input("What's the email? ")
		if not (self.is_valid_email(self.user_email)):
			print("That's not valid try again\n")
			self.get_email()

		return self.user_email

	def get_phone(self):
		self.user_phone = input("What's the phone number? ")
		if not (self.is_valid_phone(self.user_phone)):
			print("That's not valid try again\n")
			self.get_phone()

		return self.user_phone

	def get_user_info(self):
		# global user_name, user_email, user_phone

		default_values = input("Do you want to use default values? 1 for yes : ")
		if default_values == "1":
			self.get_default_user_values()
		else: 
			self.user_name = input("Who's filling out the form? ")
			self.user_email = self.get_email()
			self.user_phone = self.get_phone()

	@exception
	def get_forms_page(self):
		# global browser

		self.browser.get("https://ccbf.net/wp-login.php?loggedout=true")#make sure you are logged out of ccbf
		self.browser.get("https://ccbf.net/administrative-forms/") #get the forms login page

		#get the password text box
		password_element = self.browser.find_element_by_css_selector("#pwbox-1637") #get the password box
		password_element.click()
		password_element.send_keys("p@ssw0rd")

		#click enter to enter password
		submit_element = self.browser.find_element_by_name("Submit") #get the password box
		submit_element.click()
		# pause()
		return self.browser

	@exception
	def switch_tabs(self):
		# switch to the tab that opened the form
		self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
		# print(len(browser.window_handles)) #check how many windows we have open, should be 2
		self.browser.switch_to.window(self.browser.window_handles[-1])

	@exception
	def type_name(self):
		# #find by css_selector --- this works for this page
		# name_field = browser.find_element_by_css_selector("#nf-field-740")
		# name_field.click()
		# name_field.send_keys(user_name)

		#find
		name_field = self.browser.find_element_by_name("fname")
		name_field.click()
		name_field.send_keys(self.user_name)

	@exception
	def next_page(self):
		next_button = self.browser.find_element_by_class_name("nf-next")
		next_button.click()

	@exception
	def type_phone(self):
		#find by css_selector --- this works for this page	
		# phone_field = browser.find_element_by_css_selector("#nf-field-741")
		# phone_field.click()
		# phone_field.send_keys(user_phone)

		phone_field = self.browser.find_element_by_name("phone")
		phone_field.click()
		phone_field.send_keys(self.user_phone)

	@exception
	def type_email(self):
		#find by css_selector --- this works for this page	
		# email_field = browser.find_element_by_css_selector("#nf-field-742")
		# email_field.click()
		# email_field.send_keys(user_email)

		email_field = self.browser.find_element_by_name("email")
		email_field.click()
		email_field.send_keys(self.user_email)	

	@exception
	def get_expenditure_form(self):
		#click the hyperlink
		expenditure_hyperlink = self.browser.find_element_by_css_selector("body > div.sticky_top > section > div > ol > li:nth-child(2) > a")
		expenditure_hyperlink.click()
		self.switch_tabs()



# ALL OF THESE WORK NEED TO IMPLEMENT ON EXPENDITURE FORM
# ninja_forms = Ninja_Forms_Automator()
# # ninja_forms.start_browser()
# # ninja_forms.get_forms_page()
# # ninja_forms.get_expenditure_form()
# # ninja_forms.type_name()
# # ninja_forms.type_phone()
# # ninja_forms.type_email()
# # ninja_forms.next_page()
# phone = ninja_forms.get_phone()

# print("Woohoo got a valid phone its: " + phone)




