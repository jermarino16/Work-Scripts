import ninja_forms_automator as ninja
import functools #for error handling
from selenium.common.exceptions import NoSuchElementException


def exception(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kwargs):
		try:
			return fn(*args, **kwargs)
		except NoSuchElementException:
			print("There was a NoSuchElementException in " + fn.__name__) 

	return wrapper

class Expenditure_Request_Automator(ninja.Ninja_Forms_Automator):
	purchase_description, purchase_ministry, purchase_category = "", "", ""
	purchase_amount, payment_type, payment_to, notes = "", "", "", ""

	def __init__(self):
		super().__init__()

	def get_payment_info(self):
		acceptable_inputs = ["1", "2", "CHECK", "CREDIT CARD"]
		print("What payment will you use?")
		print("1. Credit Card")
		self.payment_type = input("2. Check\n")
		self.payment_type = self.payment_type.upper()
		# print(self.payment_type == test)
		if self.payment_type not in acceptable_inputs:
			print("\nInput is not valid, either type 1, 2, or check, or credit card")
			self.get_payment_info() #start over and get a better input 
		#if check ask for vendor information
		if self.payment_type == "CREDIT CARD" or self.payment_type == "1":
			self.payment_type = "Credit" #set payment type to check
			self.payment_to = input("Who's Card? ")

		elif self.payment_type == "CHECK" or self.payment_type == "2":
			#if check ask
			self.payment_type = "Check" #set payment type to check
			self.payment_to = input("Who is it written to? ")

	def get_purchase_info(self):		
		self.purchase_description  = input("What's the purchase? ")
		self.purchase_ministry = input("What ministry is this for? ")
		self.purchase_category = input("What category does this apply to? ")
		self.purchase_amount = input("What is the amount? ")
		self.get_payment_info()
		self.notes = input("Do you have any additional notes? ")

	@exception
	def get_expenditure_form(self):
		#click the hyperlink
		expenditure_hyperlink = self.browser.find_element_by_css_selector("body s> div.sticky_top > section > div > ol > li:nth-child(2) > a")
		expenditure_hyperlink.click()
		super().switch_tabs()

	def fill_out_page_1(self):
		super().type_name()
		super().type_phone()
		super().type_email()
		super().next_page()
		super().switch_tabs()

	@exception
	def type_description(self):
		description_field = self.browser.find_element_by_css_selector("#nf-field-747")
		description_field.click()
		# print("Purchase description is: " + self.purchase_description)
		description_field.send_keys(self.purchase_description)
		# description_field.send_keys("purchase_description")

	@exception
	def select_ministry(self):
		ministry_field = self.browser.find_element_by_css_selector("#nf-field-755")
		ministry_field.click()
		ministry_field.send_keys(self.purchase_ministry)
		ministry_field.click()	

	@exception
	def select_category(self):
		category_field = self.browser.find_element_by_css_selector("#nf-field-764")
		category_field.click()
		category_field.send_keys(self.purchase_category)
		category_field.click()	

	@exception
	def type_amount(self):
		amount_field = self.browser.find_element_by_css_selector("#nf-field-750")
		amount_field.click()
		amount_field.send_keys(self.purchase_amount)
		# amount_field.send_keys("10")

	@exception
	def type_payment_info(self):
		if (self.payment_type == "Check"):
			check_field = self.browser.find_element_by_css_selector("#nf-field-794")
			check_field.click()
			check_field.send_keys(self.payment_to)

		elif (self.payment_type == "Credit"):
			credit_field = self.browser.find_element_by_css_selector("#nf-field-766")
			credit_field.click()
			credit_field.send_keys(self.payment_to)

	@exception
	def select_payment_type(self):
		payment_type_field = self.browser.find_element_by_css_selector("#nf-field-758")
		payment_type_field.click()
		payment_type_field.send_keys(self.payment_type)
		payment_type_field.click()

	@exception
	def type_notes(self):
		notes_field = self.browser.find_element_by_css_selector("#nf-field-797")
		notes_field.click()
		notes_field.send_keys(self.notes)

	def fill_out_page_2(self):
		# sleep(2) #sleep for 2 secodns to let page load 
		self.type_description()
		self.select_ministry()
		self.select_category()
		self.type_amount()
		self.select_payment_type()
		self.type_payment_info()
		self.type_notes()
		return super().browser

	@exception	
	def get_expenditure_form(self):
		#click the hyperlink
		expenditure_hyperlink = self.browser.find_element_by_css_selector("body > div.sticky_top > section > div > ol > li:nth-child(2) > a")
		expenditure_hyperlink.click()
		self.switch_tabs()

def main():
	# create a ninja forms object and create a browser
	form_automation = Expenditure_Request_Automator()
	form_automation.get_user_info()
	form_automation.get_purchase_info()
	# browser = webdriver.Chrome()
	global browser_automate #stops browser from closing
	browser_automate = form_automation.start_browser()
	form_automation.get_forms_page()
	form_automation.get_expenditure_form()
	form_automation.fill_out_page_1()
	form_automation.fill_out_page_2()




main()
# form_automation = Expenditure_Request_Automator()

# form_automation.get_payment_info()
