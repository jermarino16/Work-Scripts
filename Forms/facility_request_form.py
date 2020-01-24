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