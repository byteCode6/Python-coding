age = int(input("Please sir enter your age: "))
money = float(input("How much money do you have? $"))

if age >= 18 and money >= 500 :
    print("You're invited to the lexury VIP party!")
elif age >= 18 and money < 430 :
    print("You're invited to the regular party.")   
elif age >= 18 and money < 50 :
    print("You're invited to the affordable party.")
else:
    print("You're invited to the kids' party")