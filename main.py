# main.py
from utils import prompt_user
from decoder import decode_expiry_date, calculate_julian_date

def main():
    print("Welcome to the Expiry Date Decoder!")
    print("Choose an option:")
    print("1. Decode Expiry Date")
    print("2. Calculate Julian Date")
    option = int(input("Enter your choice (1 or 2): "))

    if option == 1:
        type_, number = prompt_user()
        if type_ in (1, 2, 3):
            decoded_text = decode_expiry_date(type_, number)
            print(decoded_text)
        else:
            print("Invalid expiry date type. Please enter 1, 2, or 3.")
    elif option == 2:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))
        day = int(input("Enter the day: "))
        julian_date = calculate_julian_date(year, month, day)
        print("Julian Date:", julian_date)
    else:
        print("Invalid option. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
