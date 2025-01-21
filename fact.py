# User own number will be input ther factorial number
user =  int(input('Enter !x number number: '))

fact = 1
a = 1

#The factorial of the number provided by the user will be calculated, its value will be returned, and the answer will be displayed

while a <= user:
    fact*= a
    a += 1
    print(fact)