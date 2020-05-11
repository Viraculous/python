#Excercise 3:
'''Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.'''

#Formula P(1+(r/n))^nt
'''
r =interest rate
p = principal
n = how is the interest compounded?(monthly,bi-monthly,weekly, quarterly or annually)
nt = how long was the principal compounded?(a year, two or three)'''

#In our excercise 'n' was compounded annually i.e 12 months)

r = 0.04
n = 12
nt = [1,2,3]
p = int(input("Principal: "))
def A(p,r,n):
    print("Your compounded interest for the first, second and third year is ",",", p * (1+(r/n))**nt[0],",",p * (1+(r/n))**nt[1],",",p * (1+(r/n))**nt[2], "respectively")
    
print("The value of your savings for ",nt," years is ","$" + format(A(p,r,n),",.2f"), " on compounded interest")
