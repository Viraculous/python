Ad = "Recycle your bottles for every drink you buy here and get paid"
print(Ad)
print("Start recycling today by registering with us first")
print("REGISTER HERE")
Firstname = str(input("Firstname: "))
Middlename = str(input("Middlename: "))
Surname = str(input("Surname: "))
Email = str(input("Email:"))
Type = str(input("Enter YES if you want to start recycling, else enter NO:"))
if Type == "YES":
    number_of_bottles = int(input("How many bottle do you want to recycle?: "))
    litre = float(input("What are their sizes respectively(ltr)?:"))
    def bottle_deposit(litre):
        if litre <= 1:
            return 0.10 * number_of_bottles
        elif litre > 1:
            return 0.25 * number_of_bottles
        elif number_of_bottles == 0:
            return 0
        else:
            pass
    print("Congratulations! ", Firstname + " " + Surname, "you have recieved,","$"+ format(bottle_deposit(litre),".2f"),"for recycling your bottle")
elif Type == "NO":
    print("Thanks")        
else:
    pass
# I think I have successfully integrated my github with my vs code
