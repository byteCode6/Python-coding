def call():
    word = input("Enter your words: ")
    with open("list.txt", "r") as list:
        data = list.read()
        if (data.find(word)) != -1:
            print('Found')
        else:
            print("Not found!")
call()