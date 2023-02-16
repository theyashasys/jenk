from datetime import date
import time

def calculateAge(birthDate):
	today = date.today()
	age = today.year - birthDate.year -
		((today.month, today.day) <
		(birthDate.month, birthDate.day))

	return age
	
# Driver code
print(calculateAge(date(1997, 2, 3)), "years")
print("hey")
