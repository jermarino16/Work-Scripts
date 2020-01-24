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

	def get_facility_form():
		pass

	def get_facility_request_info(self):
		pass

	def select_location_of_request(self):
		pass

	def type_description_of_request(self):
		pass

	def fill_out_page():
		super.type_name()
		super.type_email()
		self.select_location_of_request()

	def main():
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




