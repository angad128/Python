##ValueError occurs if user inpur strings like 'five' instead of 5
# x = int(input("Enter Your fav number"))
# print(x)

# handling ValueError
while True:
    try:
        x = int(input("Enter Your fav number"))
        print('answer: ',  100/x)
        break
    except ValueError:
        print("make sure you enter number.")
