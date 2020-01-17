from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import chromedriver_binary  # Adds chromedriver binary to path

browser = webdriver.Chrome()
name, email = "", ""

def get_user_info():
	global name, email

	name = input("Who's filling out the form? ")
	email = input("What's the email? ")
	phone = input("What's your phone number? ")

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

def get_expenditure_form():
	#click the hyperlink
	expenditure_hyperlink = browser.find_element_by_css_selector("body > div.sticky_top > section > div > ol > li:nth-child(2) > a")
	expenditure_hyperlink.click()
	switch_tabs()

def switch_tabs():
	# switch to the tab that opened the form
	browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
	# print(len(browser.window_handles)) #check how many windows we have open, should be 2
	browser.switch_to.window(browser.window_handles[-1])

def type_name():
	name_field = browser.find_element_by_css_selector("#nf-field-740")
	name_field.click()
	name_field.send_keys("Jeremy is cool")

def type_phone():
	phone_field = browser.find_element_by_css_selector("#nf-field-741")
	phone_field.click()
	phone_field.send_keys("951-764-2881")

def type_email():
	email_field = browser.find_element_by_css_selector("#nf-field-742")
	email_field.click()
	email_field.send_keys("jeremy@ccbf.net")

def next_page():
	next_button = browser.find_element_by_class_name("nf-next")
	next_button.click()

def fill_out_page_1():
	type_name()
	type_phone()
	type_email()
	next_page()
	switch_tabs()

def type_description():
	description_field = browser.find_element_by_css_selector("#nf-field-747")
	description_field.click()
	description_field.send_keys("Jeremy So cool")

def select_ministry():
	ministry_field = browser.find_element_by_css_selector("#nf-field-755")
	ministry_field.click()
	ministry_field.send_keys("Junior High")
	ministry_field.click()	
	
def fill_out_page_2():
	type_description()
	select_ministry()


get_forms_page()
get_expenditure_form()
fill_out_page_1()
fill_out_page_2()



