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

def submit_event_form():
	global browser, name
	# open the hyperlink
	event_planning_link = browser.find_element_by_css_selector("body > div.sticky_top > section > div > ol > li:nth-child(1) > a")
	event_planning_link.click()

	# switch to the tab that opened the form
	browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
	# print(len(browser.window_handles)) #check how many windows we have open, should be 2
	browser.switch_to.window(browser.window_handles[1])

	# type in name
	name_field = browser.find_element_by_id("nf-field-721")
	name_field.click()
	# name_field.send_keys(name)
	name_field.send_keys("test")

	# type in email
	email_field = browser.find_element_by_id("nf-field-723")
	email_field.click()
	# name_field.send_keys(name)
	email_field.send_keys("test@test.com")

	# type in phone
	phone_field = browser.find_element_by_id("nf-field-728")
	phone_field.click()
	# name_field.send_keys(name)
	phone_field.send_keys("9511234567")

	#type in event name
	event_field = browser.find_element_by_id("nf-field-730")
	event_field.click()
	# name_field.send_keys(name)
	event_field.send_keys("camp")

	#type in event purpose
	event_field = browser.find_element_by_id("nf-field-731")
	event_field.click()
	# name_field.send_keys(name)
	event_field.send_keys("purps")

	#choose ministry sponsoring event
	event_field = browser.find_element_by_id("nf-field-820")
	event_field.click()
	# name_field.send_keys(name)
	event_field.send_keys("Jr. High")

	#insert date of event
	date_field = browser.find_element_by_css_selector("#nf-field-732-wrap > div.nf-field-element > div > input.pikaday__display.pikaday__display--pikaday.ninja-forms-field.nf-element.datepicker")
	date_field.click()
	# name_field.send_keys(name)
	date_field.send_keys("12052012")
	date_field.click()

	#type end time of event
	event_end_time_field = browser.find_element_by_css_selector("#nf-field-800")
	event_end_time_field.click()
	# name_field.send_keys(name)
	event_end_time_field.send_keys("12am")

	#type location of event
	location_field = browser.find_element_by_id("nf-field-856")
	location_field.click()
	# name_field.send_keys(name)
	location_field.send_keys("Grace")
	location_field.click()

	# #type start time of event ###DEBUG
	# event_start_time_field = browser.find_element_by_css_selector("#nf-field-856")
	# event_start_time_field.click()
	# # name_field.send_keys(name)
	# event_start_time_field.send_keys("7pm")

	return browser

# get_user_info()
browser = get_forms_page()
browser = submit_event_form()