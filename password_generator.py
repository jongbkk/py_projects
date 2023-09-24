import random
import string


def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length should be at least 1")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def final_password():
    print("Password Generator")
    while True:
        length = int(input("Enter the desired password length(1 to 12): "))
        if length <= 1 or length > 12:
            print("please enter the valid length")
        else:
            break
    while True:
        use_uppercase = input("Include uppercase letters? (y/n): ").lower()
        if use_uppercase.lower() == "y" or use_uppercase.lower() == "n":
            break
        else:
            print("please enter the valid answer")
    while True:
        use_digits = input("Include digits? (y/n): ").lower()
        if use_digits.lower() == "y" or use_digits.lower() == "n":
            break
        else:
            print("please enter the valid answer")
    while True:
        use_special = input("Include special characters? (y/n): ").lower()
        if use_special.lower() == "y" or use_special.lower() == "n":
            break
        else:
            print("please enter a valid answer")
    password = generate_password(length, use_uppercase, use_digits, use_special)
    print("Generated Password:", password)


final_password()
