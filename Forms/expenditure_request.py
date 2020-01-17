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

def switch_tabs():
	# switch to the tab that opened the form
	browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
	# print(len(browser.window_handles)) #check how many windows we have open, should be 2
	browser.switch_to.window(browser.window_handles[1])

def fill_out_page_1():
	name_field = browser.find_element_by_css_selector("#nf-field-740")
	name_field.click()
	name_field.send_keys("Jeremy is cool")

get_forms_page()
get_expenditure_form()
switch_tabs()
fill_out_page_1()



