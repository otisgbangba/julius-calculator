def welcome():
    print("welcome to julius calculator.")
    proceed = input("""Please select what you will like to do C for continue,E for exit""")
    if proceed.upper() == 'C':
        calculate()
    elif proceed.upper() == 'E':
        proceeding = input("""Do you really want to exit? Y for yes,N for no""")
    if proceeding.upper() == 'Y':
        print("Thanks for using julius calculator,See you again.")
    elif proceeding.upper() == 'N':
        exit()
    else:welcome()
def calculate():
    operation = input("""Please type in the math operation you will like to run
+ for addition
- for subtraction
* for multiplication
/ for division
""")

    number_1 = float(input("please input 1st number\n"))
    number_2 = float(input("please input your 2nd number\n"))
    if operation== '+':
        print("{} + {}= ".format(number_1, number_2))
        print(number_1+number_2)

# here we write a code for other operations
# we also add if and else if (elif) statements
    elif operation=='-':
        print("{} - {}= ".format(number_1, number_2))
        print(number_1-number_2)

    elif operation=='*':
        print("{} * {}= ".format(number_1, number_2))
        print(number_1*number_2)

    elif operation=='/':
        print("{} / {}= ".format(number_1, number_2))
        print(number_1/number_2)
    else:print("You have not typed in a 'valid' operation, please run through the program again. ")
    again()
# we add the again function to the calculate as a loop
# to make the calculator continuous we define another variable for continuity called again
def again():
# we will need to take input form user
    calc_again = input(""" please say if you want to calculate again
    say Y for Yes and N for No""")
# if the usr selects Y, then call calculate
# we can make the program accept Y or y by adding the .upper()
    if calc_again.upper() == 'Y':
        calculate()
# if the user types N, say thanks and goodbye
# we can make the program accept N or n by adding the .upper()
    elif calc_again.upper() == "N":
        print("Thanks for using My Calculator, See you again. ")
# if the user types any other key aside N, call calculate
    else:again()
# Call the function Welcome
welcome()
# Call calculate() outside of the function
calculate()

 
    
