############################### CHAPTER 2.1

    # LAB 1 
        print("Hello,World!")
        print("Phil")
        # error: print(Phil)
        # error: print"Phil"

    #  LAB 2
        print("Programming","Essentials","in", sep="***", end="...")
        print("Python")

    # LAB 3
        print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

        print("        *")
        print("       * *")
        print("      *   *")
        print("     *     *")
        print("    *       *")
        print("   *         *")
        print("  *           *")
        print(" *             *")
        print("******     ******")
        print("     *     *")
        print("     *     *")
        print("     *     *")
        print("     *     *")
        print("     *     *")
        print("     *     *")
        print("     *******")

        print("         *         "*2)
        print("        * *        "*2)
        print("       *   *       "*2)
        print("      *     *      "*2)
        print("     *       *     "*2)
        print("    *         *    "*2)
        print("   *           *   "*2)
        print("  *             *  "*2)
        print(" ******     ****** "*2)
        print("      *     *      "*2)
        print("      *     *      "*2)
        print("      *     *      "*2)
        print("      *     *      "*2)
        print("      *     *      "*2)
        print("      *     *      "*2)
        print("      *******      "*2)

############################### CHAPTER 2.2

    # LAB 1
        print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")

############################### CHAPTER 2.4

    # LAB 1: VARIABLES

        john = 3
        mary = 5 
        adam = 6

        print(john, mary, adam, sep=", ")

        total_apples = john + mary + adam

        print(total_apples)

        print("Total number of apples:", total_apples)

    # LAB 2: Variables: a simple converter

        kilometers = 12.25
        miles = 7.38

        miles_to_kilometers = miles * 1.61
        kilometers_to_miles = kilometers / 1.61

        print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
        print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

    # LAB 3: Operators and expressions
        
        x = 0
        x = float(x)
        y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
        print("y =", y)

        x = 1
        x = float(x)
        y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
        print("y =", y)

        x = -1
        x = float(x)
        y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
        print("y =", y)

############################### CHAPTER 2.5

    # LAB 1: Comments

    # Before editing - Original code

        #this program computes the number of seconds in a given number of hours
        # this program has been written two days ago

        a = 2 # number of hours
        seconds = 3600 # number of seconds in 1 hour

        print("Hours: ", a) #printing the number of hours
        # print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

        #here we should also print "Goodbye", but a programmer didn't have time to write any code
        #this is the end of the program that computes the number of seconds in 3 hour

    # After editing

        #this program computes the number of seconds in a given number of hours
        hours = 2 # number of hours
        seconds = 60 # number of seconds in 1 hour

        print("Hours:", hours) #printing the number of hours
        print("Seconds in Hours:", hours * seconds) # printing the number of seconds in a given number of hours
        print("Goodbye")

############################### CHAPTER 2.6

    # LAB 2.6.1.9: Simple input and output

        a = float(input("Enter a number above zero: ")) # This will take a users input (string) and convert it to a float type
        b = float(input("Enter another number above zero: "))

        print("Addition:",a+b) 
        print("Subtraction:",a-b) 
        print("Multiplication:",a*b) 
        print("Division:",a/b) 
        print("\nThat's all, folks!")

    # LAB 2.6.1.10 Operators and expressions

        x = float(input("Enter value for x: "))
        y = 1./(x + 1./(x + 1./(x + 1./x)))
        print("y =", y)

    # LAB 2.6.1.11 Operators and expressions

        hour = int(input("Starting time (hours): "))
        mins = int(input("Starting time (minutes): "))
        dura = int(input("Event duration (minutes): "))

        mins += dura # Find total minutes
        hour += mins // 60 # We are adding start hour to total mins (Start mins + duration) and dividing by 60 
        mins %= 60 # This will convert the total mins into a traditional 59 mins format
        hour %= 24 # This will turn the previous calculated hours in a 24hr format
        print("The event finishes at:", str(hour)+":"+ str(mins))

