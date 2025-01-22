def factrial (f):
    if f < 0 :
        return "Eroor: Factrial is not Defined for negtive number."
    elif f == 0:
        return 1
    else:
        result = 1
        for i in range(1, f+1):
            result *= i
        return result

a = factrial(5)
print(a,'!')   
    
    