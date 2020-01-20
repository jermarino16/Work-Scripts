from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import chromedriver_binary  # Adds chromedriver binary to path
import functools #for error handling

from time import sleep #to pause execution

browser = ""
user_name, email, phone = "", "", ""
purchase_description, purchase_ministry, purchase_category = "", "", ""
purchase_amount, payment_type, payment_to, notes = "", "", "", ""

def get_default_user_values():
	global user_name, user_email, user_phone
	print("Proceeding with default values")

	user_name = "Jeremy Marino"
	user_email = "Jeremy@ccbf.net"
	user_phone = "951-764-2881"

def get_user_info():
	global user_name, user_email, user_phone

	default_values = input("Do you want to use default values? 1 for yes : ")
	if default_values == "1":
		get_default_user_values()
	else: 
		user_name = input("Who's filling out the form? ")
		user_email = input("What's the email? ")
		user_phone = input("What's your phone number? ")

	get_purchase_info()

def get_purchase_info():
	global purchase_description, purchase_ministry, purchase_category, purchase_amount, payment_type, payment_to, notes
	
	purchase_description  = input("What's the purchase? ")
	purchase_ministry = input("What ministry is this for? ")
	purchase_category = input("What category does this apply to? ")
	purchase_amount = input("What is the amount? ")
	payment_type = input("What payment did you use? ")
	payment_to = input("Who's the payment for? ")
	notes = input("Do you have any additional notes? ")

def exception(fn):
	"""
	A decorator that wraps the passed in function and logs exceptions should one occur
	"""
	@functools.wraps(fn)
	def wrapper(*args, **kwargs):
		try:
			return fn(*args, **kwargs)
		except NoSuchElementException:
			print("There was a no such element exception in " + fn.__name__) 

	return wrapper

@exception
def get_forms_page():
	global browser

	browser.get("https://ccbf.net/wp-login.php?loggedout=true")#make sure you are logged out of ccbf
	browser.get("https://ccbf.net/administrative-forms/") #get the forms login page

	#get the password text box
	password_element = browser.find_element_by_css_selector("#pwbox-1637") #get the password box
	password_element.click()
	password_element.send_keys("p@ssw0rd")

	#click enter to enter password
	submit_element = browser.find_element_by_name("Submit") #get the password box
	submit_element.click()
	# pause()
	return browser

@exception
def get_expenditure_form():
	#click the hyperlink
	expenditure_hyperlink = browser.find_element_by_css_selector("body > div.sticky_top > section > div > ol > li:nth-child(2) > a")
	expenditure_hyperlink.click()
	switch_tabs()

@exception
def switch_tabs():
	# switch to the tab that opened the form
	browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
	# print(len(browser.window_handles)) #check how many windows we have open, should be 2
	browser.switch_to.window(browser.window_handles[-1])

@exception
def type_name():
	# #find by css_selector --- this works for this page
	# name_field = browser.find_element_by_css_selector("#nf-field-740")
	# name_field.click()
	# name_field.send_keys(user_name)

	#find
	name_field = browser.find_element_by_name("fname")
	name_field.click()
	name_field.send_keys(user_name)

@exception
def type_phone():
	phone_field = browser.find_element_by_css_selector("#nf-field-741")
	phone_field.click()
	phone_field.send_keys(user_phone)

@exception
def type_email():
	email_field = browser.find_element_by_css_selector("#nf-field-742")
	email_field.click()
	email_field.send_keys(user_email)

@exception
def next_page():
	next_button = browser.find_element_by_class_name("nf-next")
	next_button.click()

def fill_out_page_1():
	type_name()
	type_phone()
	type_email()
	next_page()
	switch_tabs()

@exception
def type_description():
	description_field = browser.find_element_by_css_selector("#nf-field-747")
	description_field.click()
	print("Purchase description is: " + purchase_description)
	description_field.send_keys(purchase_description)
	# description_field.send_keys("purchase_description")

@exception
def select_ministry():
	ministry_field = browser.find_element_by_css_selector("#nf-field-755")
	ministry_field.click()
	ministry_field.send_keys(purchase_ministry)
	ministry_field.click()	

@exception
def select_category():
	category_field = browser.find_element_by_css_selector("#nf-field-764")
	category_field.click()
	category_field.send_keys(purchase_category)
	category_field.click()	

@exception
def type_amount():
	amount_field = browser.find_element_by_css_selector("#nf-field-750")
	amount_field.click()
	amount_field.send_keys(purchase_amount)
	# amount_field.send_keys("10")

@exception
def type_check_info():
	# try:
	# 	check_field = browser.find_element_by_css_selector("#nf-field-794")
	# 	check_field.click()
	# 	check_field.send_keys(payment_to)
	# except NoSuchElementException:
	# 	print("That element doesn't exist")
	check_field = browser.find_element_by_css_selector("#nf-field-794")
	check_field.click()
	check_field.send_keys(payment_to)

@exception
def select_payment_type():
	payment_type_field = browser.find_element_by_css_selector("#nf-field-758")
	payment_type_field.click()
	payment_type_field.send_keys(payment_type)
	payment_type_field.click()

@exception
def type_notes():
	notes_field = browser.find_element_by_css_selector("#nf-field-797")
	notes_field.click()
	notes_field.send_keys(notes)

def fill_out_page_2():
	# sleep(2) #sleep for 2 secodns to let page load 
	type_description()
	select_ministry()
	select_category()
	type_amount()
	select_payment_type()
	type_check_info()
	type_notes()

def main():
	global browser
	get_user_info()
	browser = webdriver.Chrome()
	get_forms_page()
	get_expenditure_form()
	fill_out_page_1()
	fill_out_page_2()




main()
