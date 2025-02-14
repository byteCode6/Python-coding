user = int(input("Plaese sir Enter your rell age: "))
vote = str(input("Enter your choice (Yes/No)")).lower()
if user >= 18 :
    if vote == "yes":
        print('Your voteing is complete.')
    else:
        print('Noon you wish to vote!')
else:
    print("You cannot vote yet.")
    


try:
    namber = int(input("Plaese enter your number sir : "))
    nam = 10 /  namber
    print(nam)
except ZeroDivisionError :
    print("0 is not defiend!")
except ValueError:
    print("Sir litter in not defiend!")