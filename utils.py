# utils.py

def prompt_user():
    print("Welcome to the Expiry Date Decoder!")
    type_ = int(input("Enter the type of expiry date (1, 2, or 3): "))
    number = input("Enter the expiry date number: ")
    return type_, number
