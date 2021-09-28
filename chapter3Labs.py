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

############################### CHAPTER 3.2

    # LAB: 3.2.1.3 Essentials of the while loop - Guess the secret number
    secret_number = 777

    print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)

    user_num = int(input("Have a guess, enter a number: "))

    while user_num != secret_number:
        user_num = int(input("Ha ha! You're stuck in my loop!......guess again: "))
    print("Correct!",user_num,"is the magic number.","Well done, muggle! You are free now.")

    # LAB: 3.2.1.6 Essentials of the for loop - counting mississippily
    import time # Imports a module called time to use (call) the sleep() function

    for count in range(1,6):
        print(count,"Mississippi")
        time.sleep(1) # Will output the print statement at 1 interval seconds
    print("Ready or not, here I come!")

    # LAB: 3.2.1.9 The break statement - Stuck in a loop
    # The while will keeping looping round until the correct word is inputted, which then it will break (jump out of the while loop)
    while True: 
        user_guess = input("What is the magic word?...")
        if user_guess == "chupacabra":
            break
    print("You've successfully left the loop.")

    # LAB: 3.2.1.11 The continue statement - the Pretty Vowel Eater
    word_without_vowels = ""

    # Prompt the user to enter a word and assign it to the user_word variable.
    user_word = input("Enter a word: ")
    user_word = user_word.upper() # This converts the user word to uppercase
    # Checks each letter in turn to see if it matches one the vowels 
    # If it matches it skips and move to the next letter.
    for letter in user_word:
        if letter == "A":
            continue
        elif letter == "E":
            continue
        elif letter == "I":
            continue
        elif letter == "O":
            continue
        elif letter == "U":
            continue
        else:
            word_without_vowels += letter # Any letters not a vowel will be concatenated to this variable
    # Print the word assigned to word_without_vowels.
    print(word_without_vowels)

    # LAB: 3.2.1.14 Essentials of the while loop
    blocks = int(input("Enter the number of blocks: "))
    height = 0

    while blocks > 0:
        height += 1
        blocks -= height
        if blocks <= height:
            break
    print("The height of the pyramid:", height)

    # LAB: 3.2.1.15 Collatz's hypothesis
    c0 = int(input("Enter any non-negative and non-zero integer number: "))
    steps = 0

    while c0 != 1:
        steps += 1
        if c0 % 2 == 0:
            c0 //= 2
            print(c0)
        else:
            c0 = 3 * c0 + 1
            print(c0)
    print("Steps =", steps)

    # LAB: 3.4.1.6 The basics of lists
    hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

    # Step 1: write a line of code that prompts the user
    # to replace the middle number with an integer number entered by the user.
    hat_list[2] = int(input("Enter a number: "))
    # Step 2: write a line of code that removes the last element from the list.
    del hat_list[-1]
    # Step 3: write a line of code that prints the length of the existing list.
    print(len(hat_list))
    print(hat_list)

    # LAB: 3.4.1.13 The basics of lists - the Beatles
    # step 1 - Creates a list
    beatles = [] 
    print("Step 1:", beatles)

    # step 2 - Adds new entry to list
    beatles.append("John Lennon")
    beatles.append("Paul McCartney")
    beatles.append("George Harrison")
    print("Step 2:", beatles)

    # step 3 - Prompts the user to add the below values to the list
    for i in range(1):
        beatles.append(input("Please add the following band member\nStu Sutcliffe: "))
        beatles.append(input("Please add the following band member\nPete Best: "))
    print("Step 3:", beatles)

    # step 4 - Removes the last two entries from the list
    del beatles[-1]
    del beatles[-1]
    print("Step 4:", beatles)

    # step 5 - Add a new value to new but in the first position(Left most)
    beatles.insert(0, "Ringo Starr")
    print("Step 5:", beatles)

    # testing list legth
    print("The Fab", len(beatles))

    # LAB: 3.6.1.9 Operating with lists - basics
    # This labs iterates through a list and filters out repeated values.
    # It does so by comparing x list to y list(y is an empty list)
    # If a value in x is not in y it will add it to y
    # y should now only have unique values
    # On completion of the loop x will copy the values from y and print x with the unique values
    my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    my_unique_list = []

    for i in range(len(my_list)):
        if my_list[i] not in my_unique_list:
            my_unique_list.append(my_list[i])
    my_list = my_unique_list[:]
        
    print("The list with unique elements only:")
    print(my_list)

    # An alternative method but using the values instead of the indices
    my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    my_unique_list = []

    for i in my_list:
        if i not in my_unique_list:
            my_unique_list.append(i)
    my_list = my_unique_list[:]
            
    print("The list with unique elements only:")
    print(my_list)

    # #################################### END OF LABS ###############################
    # Below are examples of coded used during chapter for future references

    # This is a shorthand version to creating a 2D list
    temps = [[0.0 for h in range(24)] for d in range(31)]

    # This is a shorthand version to creating a 3D list
    rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]