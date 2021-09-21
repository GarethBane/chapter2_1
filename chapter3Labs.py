############################### CHAPTER 3.1 

# LAB: 3.1.1.4 Questions and answers
n = int(input("Enter a number: "))
print(n >= 100)

# LAB: 3.1.1.10 Comparison operators and conditional execution
plant = input("what is your favourite plant?: ")

if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not " + plant + "!")

# LAB: 3.1.1.11 Essentials of the if-else statement
income = float(input("Enter the annual income: "))

if income < 85528:
    tax = income * .18 - 556.02
else:
    tax = (income - 85528) * .32 + 14839.02
    
if tax <= 0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

# LAB: 3.1.1.12 Essentials of the if-elif-else statement
year = int(input("Enter a year: "))

# First checks to see if year falls within the Gregorian calendar period, if not it will jump to the last else statement.
# If year falls within the Gregorian calendar period, it will execute the nested if statements
if year >= 1582:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
else:
    print("Not within the Gregorian calendar period")