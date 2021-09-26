############################### CHAPTER 4.3

# LAB: 4.3.1.6 A leap year: writing your own functions
# This function takes an argument (year) and check if its a leap year or not
# If its a leap year it will return True else it will return False
def is_year_leap(year):
    if year >= 1582:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

# LAB: 4.3.1.7 How many days: writing and using your own functions
# This lab uses the function from the previous lab in conjuntion with a new funtion 
# The new function will take two arguments (year and month) and return the number of days in that month for that year.
def is_year_leap(year):
    if year >= 1582:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True
    else:
        return False
        
def days_in_month(year, month):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31] # An extra element was added at the start of the list "0", so the remaining elements aligns to the correct number of months (1-12)
    if is_year_leap(year) and month == 2: # Checks if year is a leap year and the month is feb and return 29 days
        return 29
    else: # Else return the correct number of days from the list, using the month relating to the list index.
        return days[month]
           
# The below code simply check the above function are outputting the correct results.    
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")




def is_year_leap(year):
    if year >= 1582:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31] 
    if is_year_leap(year) and month == 2: 
        return 29
    else: 
        return days[month]

def day_of_year(year, month, day):
    

print(day_of_year(2000, 12, 31))
