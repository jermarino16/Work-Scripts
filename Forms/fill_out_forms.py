from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary  # Adds chromedriver binary to path

browser = webdriver.Chrome()
name, email = "", ""

def get_user_info():
	global name, email

	name = input("Who's filling out the form? ")
	email = input("What's the email? ")

def get_form_page():
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

def submit_event_form():
	global browser
	# open the hyperlink
	event_planning_link = browser.find_element_by_css_selector("body > div.sticky_top > section > div > ol > li:nth-child(1) > a")
	event_planning_link.click()

	# switch to the tab that opened the form
	browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
	# print(len(browser.window_handles)) #check how many windows we have open, should be 2
	browser.switch_to.window(browser.window_handles[1])

	print(browser.current_url) #what url are we on
	# #type in name
	# name_field = browser.find_element_by_id("nf-field-721")
	# name_field.click()
	# # name_field.send_keys(name)
	# name_field.send_keys("test")

	return browser

# get_user_info()
browser = get_form_page()
browser = submit_event_form()