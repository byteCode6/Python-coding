# The function calculates the factorial
def factorial (a):
    if a == 0 :
        return 1
    elif a < 0 :
        if True :
            print('Factorial is not valid for numbers less than zero.')
            return None
    else:
        fact = 1
        for b in range(1, a + 1):
            fact *= b
        return fact # calculated the factorial
   
# Get user input in integer numbers  

# chake if the input is valid
try:
    user_input = int(input('Enter your number: '))
    result = factorial(user_input)
    if user_input < 0 :
        print('Please enter a non-negative numbers.')
        if True:
            print('I will try again.')
    elif result is not None :
        print('Factorial of', user_input,'is =', result)
except ValueError("Opps! That's not a number. Please try again."):
    
        
            