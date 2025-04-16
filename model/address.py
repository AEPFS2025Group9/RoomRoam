class Address:
	def __init__(self, street:str, streetnr:int, zip:int, city:str):
		self.__street = street
		self.__streetnr = streetnr
		self.__zip = zip
		self.__city = city

	@property
	def street(self):
		return self.__street

	@property
	def streetnr(self):
		return self.__streetnr

	@property
	def zip(self):
		return self.__zip

	@property
	def city(self):
		return self.__city

	def get_address_details(self):
		return f"Street: {self.__street}, Street number: {self.__streetnr}, Zip code: {self.__zip}, City: {self.__city}"