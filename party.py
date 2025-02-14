# number = range(1, 7)
# la = list(map(lambda a: a ** 2, number))
# print(la)

# b = range(1, 6)
# c = []
# for i in b:
#     c.append(i ** 2)
    
# print(c)

number = range(1, 10)
even_number = list(filter(lambda a: a % 2 == 0, number))
print(even_number)
