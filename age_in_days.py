class AgeInDays():
	birth_day = 1
	birth_month = 1
	birth_year = 1900
	current_day = 1
	current_month = 1
	current_year = 2000
	age = 1
	
	def __init__(self, name):
		self.name = name
	def is_leap_year(self, year):
		"""	This function is used to determine if a given year
		is a leap year. If it is, returns true. Otherwise
		returns false """
		
		if year % 4 == 0:
			if year % 100 == 0:
				if year % 400 == 0:
					return True
				else:
					return False
			else:
				return True
		else:
			return False
	
	def save_to_file(self):
		with open('user_ages.txt', 'a') as file_name:
			file_name.write(self.name + " --- " + str(self.birth_month) + "/"
				+ str(self.birth_day) + "/" + str(self.birth_year) + "---" + 
				str(self.age) + "\n")
				
	def count_days(self, birth_year, birth_month, birth_day, current_year,
		current_month, current_day):
		"""This function calculates how many days old a person is given
			their date of birth and the current date. This is the function
			that actually does 90% of the work. """
		
		month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		days = 0
	
		for birth_year_month in range(birth_month, 12):
			if self.is_leap_year(birth_year):
				month_days[1] = 29
			days += month_days[birth_year_month]
		days += (month_days[birth_month-1] - birth_day)
	
		for year in range(birth_year+1, current_year):
			if self.is_leap_year(year):
				days += 366
			else:
				days += 365
	
		for current_year_month in range(0, current_month-1):
			if self.is_leap_year(current_year):
				month_days[1] = 29
			days += month_days[current_year_month]
		days += current_day
	
		return days
		
	def print_greeting(self):
		message = "Welcome to my age calculator, " + self.name + "!\n"
		message += "The purpose of this program is to calculate your age in days and weeks.\n"
		message += "I hope this program is interesting for you!\n\n"
		message += "To start, please provide the following information:"
	
		print (message)
	
	def get_birth_date(self):
		date_of_birth = input("What is your date of birth? (mm/dd/yyyy): ").split('/')
		return (date_of_birth)
	
	def get_current_date(self):
		current_date = input("What is the current date? (mm/dd/yyyy): ").split('/')
		return current_date
				
	def print_results(self):
		self.print_greeting()
		birthday_list = self.get_birth_date()
		current_day_list = self.get_current_date()
	
		birth_year = int(birthday_list[2])
		birth_month = int(birthday_list[0])
		birth_day = int(birthday_list[1])
		current_year = int(current_day_list[2])
		current_month = int(current_day_list[0])
		current_day = int(current_day_list[1])
	
		days_old = str(self.count_days(birth_year, birth_month, birth_day, current_year,
			current_month, current_day))
	
		weeks_old = str(int(days_old) / 7)
		week_list = weeks_old.split('.')
		days_remainder = str(int(days_old) % 7)
	
		results = "\nBased on this information, you are "
		results += days_old
		results += " days old.\nThis means you are "
		results += week_list[0]
		results += " weeks, and "
		results += days_remainder
		results += " days old.\n"
		
		self.age = days_old
		
		self.save_to_file()
		return results
