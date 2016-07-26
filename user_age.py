from age_in_days import AgeInDays

"""	This program will take the user's birthday as input and will return 
	how old the user is in days. """
	
# Dane Cravens, 5/24/2016
# Morehead State University, m1006242

def username():
	name = input("Please tell me your name! ")
	return name
	
user = AgeInDays(username())
print (user.print_results())



########################################
########Current Issue is that ##########
########the save_to_file 	  ##########
########function is saving the##########
########default values, not   ##########
########updated birthday data.##########
########################################
