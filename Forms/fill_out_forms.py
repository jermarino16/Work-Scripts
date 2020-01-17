from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path

def get_form_page():
	browser = webdriver.Chrome()

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

browser = get_form_page()