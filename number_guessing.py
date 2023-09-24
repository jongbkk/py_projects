import random

num = random.randint(1, 10)

print("Guessing a Number\n")

while True:
    user = input("Enter your number from 1 to 10:")
    if not user.isdigit():
        print("Please enter a positive integer from 1 to 10\n")
    else:
        user = int(user)
        if user > 10:
            print("Please enter a number less than 10\n")
        elif user == num:
            print("You guessed the number right")
            print('and the number is ', user)
            break
        else:
            print("Try again\n")
