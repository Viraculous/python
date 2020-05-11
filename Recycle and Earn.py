#Excercise 1:

'''In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places'''

#Here is my Advertisement tag
Ad = "Recycle your bottles for every drink you buy here and get paid"

#This executes my Advertisement tag
print(Ad)

#This is intended to collect the user data assuming the platform requires the users data for records,reference or rebates
print("Start recycling today by registering with us first")
print("REGISTER HERE")

#This recieves the user data on specified input requirement
Firstname = str(input("Firstname: "))
Middlename = str(input("Middlename: "))
Surname = str(input("Surname: "))
Email = str(input("Email:"))

#This receives data from users to know weather or not they want to recycle.
Type = str(input("Enter YES if you want to start recycling, else enter NO:"))

#This states the condition and exceptions for the execution of user input
if Type == "YES":
    
#Error handling using try-except functions
    try:
        number_of_bottles = int(input("How many bottle do you want to recycle?: "))
    except ValueError:
        print("Error...numbers only. Retry")
        quit()

#Error handling using try-except functions
    try:
        litre = float(input("What are their sizes respectively(ltr)?:"))
    except ValueError:
        print("Error...numbers only. Retry")
        quit()

#This states the condition for execution for the ranges of size stipulated in this excercise and its return value
    def bottle_deposit(litre):
        if litre <= 1:
            return 0.10 * number_of_bottles
        elif litre > 1:
            return 0.25 * number_of_bottles
        elif number_of_bottles == 0:
            return 0
        else:
            pass
        
#This print function is executed if the expected input is "YES" and fulfills the sub-conditions preceding it.
    print("Congratulations! ", Firstname + " " + Surname, "you have recieved,","$"+ format(bottle_deposit(litre),".2f"),"for recycling your bottle")

elif Type == "NO":  
#This print function is executed if the alternate expected input "NO" is met
    print("Thanks")     
       
else:
#This print function is executed when neither of the first conditional requirement("YES" or"NO") of the Type function is met. i.e for anything else than "YES" or "NO".
    print("wrong entry: input either uppercase YES/NO")