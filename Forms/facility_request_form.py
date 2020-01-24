import ninja_forms_automator as ninja
import functools #for error handling
from selenium.common.exceptions import NoSuchElementException


class Facility_Request_Automator(ninja.Ninja_Forms_Automator):

	def __init__(self):
		super().__init__()

	def exception(fn):
		@functools.wraps(fn)
		def wrapper(*args, **kwargs):
			try:
				return fn(*args, **kwargs)
			except NoSuchElementException:
				print("There was a NoSuchElementException in " + fn.__name__) 

		return wrapper

	def get_facility_form(self):
		#click the hyperlink
		facility_hyperlink = self.browser.find_element_by_css_selector("body > div.sticky_top > section > div > ol > li:nth-child(4) > a")
		facility_hyperlink.click()
		self.switch_tabs()

	def get_location(self):
		valid_inputs = {"1": "Sanctuary", "2": "Children's Ministry", "3": "Office",
						"4": "Potter's House", "5": "Grace Building", "6": "Foyer",
						"7": "Overflow Room", "8": "Kitchen", "9": "Parking Lot",
						"10": "Other" }
		#display possible locations
		print("Where is the request?")
		print("1. Sanctuary")
		print("2. Children's Ministry")
		print("3. Office")
		print("4. Potter's House")
		print("5. Grace Building")
		print("6. Foyer")
		print("7. Overflow Room")
		print("8. Kitchen")
		print("9. Parking Lot")
		self.location = input("10. Other\n")

		if self.location not in valid_inputs.keys():
			print("\nYour input is invalid, please type the number of the location")
			self.get_location()

		self.location = valid_inputs[self.location]#get dictionary value of input
		return self.location

	def get_description(self):
		#prompt for user input
		
		#save user input
		pass

	def get_facility_request_info(self):
		self.get_location()
		#get description
		pass

	def select_location_of_request(self):
		#select the location
		pass

	def type_description_of_request(self):
		#get box, type keys
		pass

	def fill_out_page(self):
		super.type_name()
		super.type_email()
		self.select_location_of_request()

	def main(self):
		# create a ninja forms object and create a browser
		form_automation = Facility_Request_Automator()
		form_automation.get_user_info()
		form_automation.get_facility_request_info()
		# browser = webdriver.Chrome()
		global browser_automate #stops browser from closing
		browser_automate = form_automation.start_browser()
		form_automation.get_forms_page()
		form_automation.get_facility_form()
		form_automation.fill_out_page()

form_automation = Facility_Request_Automator()
form_automation.get_user_info()
# form_automation.get_facility_request_info()

location = form_automation.get_location()



