import ninja_forms_automator

purchase_description, purchase_ministry, purchase_category = "", "", ""
purchase_amount, payment_type, payment_to, notes = "", "", "", ""

def exception(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kwargs):
		try:
			return fn(*args, **kwargs)
		except NoSuchElementException:
			print("There was a NoSuchElementException in " + fn.__name__) 

	return wrapper

def get_purchase_info():
	global purchase_description, purchase_ministry, purchase_category, purchase_amount, payment_type, payment_to, notes
	
	purchase_description  = input("What's the purchase? ")
	purchase_ministry = input("What ministry is this for? ")
	purchase_category = input("What category does this apply to? ")
	purchase_amount = input("What is the amount? ")
	payment_type = input("What payment did you use? ")
	payment_to = input("Who's the payment for? ")
	notes = input("Do you have any additional notes? ")

@exception
def get_expenditure_form():
	#click the hyperlink
	expenditure_hyperlink = browser.find_element_by_css_selector("body > div.sticky_top > section > div > ol > li:nth-child(2) > a")
	expenditure_hyperlink.click()
	switch_tabs()

def fill_out_page_1():

	#have to call ninja forms class for this
	# type_name()
	# type_phone()
	# type_email()
	# next_page()
	# switch_tabs()

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
	#create a ninja forms object and create a browser
	# global browser
	# get_user_info()
	# browser = webdriver.Chrome()
	get_forms_page()
	get_expenditure_form()
	fill_out_page_1()
	fill_out_page_2()




main()
