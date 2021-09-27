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

# LAB: 4.3.1.8 Day of the year: writing and using your own functions
# This lab build upon the previous two, the function takes three arguments and returns the total days in a year for a given year, month, day
# If the arguments value do not meet the requirements it will return a "none"
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
    if year < 1582 or month < 1 or month > 12 or day < 1 or day > 31: # Validates input if false return none
        return 
    days_sum = 0
    for x in range(month): # Takes month as a range for number of iteration, for this loop it will call the function X amount of times
        days_sum += days_in_month(year, x) # For each iteration add the value to the previous value to produce a total sum (days)
    return days_sum + day # Add the specified days from the user to the days_sum and return the result

# A few test case
print(day_of_year(2000, 12, 1))
print(day_of_year(1999, 12, 1))
print(day_of_year(2000, 3, 1))
print(day_of_year(2001, 3, 1))
print(day_of_year(2000, 3, 31))
print(day_of_year(1999, 3, 31))

# LAB: 4.3.1.9 Prime numbers - how to find them
# This lab takes a number and checks if it is a prime number or not
def is_prime(num):
    is_num_prime = True # Create a variable to store true or false
    for x in range(2, num): # Iterates through nth times checking if num mod (%) equals 0, if yes its not prime so is_num_prime becomes False, start of range is 2 and finishes one before num so not to check itself.
        if num % x == 0:
            is_num_prime = False
            break # If false jump out of code and return value
        else: # If num can not be divided equal its prime, return True
            is_num_prime = True
    return is_num_prime 

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

# LAB: 4.3.1.10 Converting fuel consumption
def liters_100km_to_miles_gallon(liters):
    a = 100000 / 1609.344 # Converts 100km into miles
    b = 1 / 3.785411784   # Converts 1 liter into gallons
    c = liters * b        # Calculates liters used in gallons
    mpg = a / c           # Calculates miles per gallons (MPG)
    return mpg

def miles_gallon_to_liters_100km(miles):
    a = 100000 / 1609.344 # Converts 100km into miles
    b = 1 / 3.785411784   # Converts 1 liter into gallons
    c = a / miles         # Calculates miles per litres 
    litre_100km = c / b   # Calculates litres/100Km
    return litre_100km
    
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

