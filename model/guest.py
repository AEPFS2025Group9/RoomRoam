class Guest:
	def __init__(self, firstname:str, lastname:string, birthdate:date, nationality:str, email:str, telnr:int):
		self.__firstname = firstname
		self.__lastname = lastname
		self.__birthdate = birthdate
		self.__nationality = nationality
		self.__email = email
		self.__telnr = telnr

	@property
	def firstname(self):
		return self.__firstname

	@property
	def lastname(self):
		return self.__lastname

	@property
	def birthdate(self):
		return self.__birthdate

	@property
	def nationality(self):
		return self.__nationality

	@property
	def email(self):
		return self.__email

	@property
	def telnr(self):
		return self.__telnr

	def get_guest_details(self):
		return f"First name: {self.__firstname}, Last name: {self.__lastname}, Birthdate: {self.__birthdate}, 				Nationality: {self.__nationality}, E-mail: {self.__email}, Telephone number: {self.__telnr}"