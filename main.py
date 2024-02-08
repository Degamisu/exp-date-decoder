# main.py
from utils import prompt_user
from decoder import decode_expiry_date

def main():
    type_, number = prompt_user()
    decoded_text = decode_expiry_date(type_, number)
    print(decoded_text)

if __name__ == "__main__":
    main()