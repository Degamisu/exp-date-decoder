# decoder.py
import math

def decode_expiry_date(type_, number):
    decoded_text = ""
    if type_ == 1:
        decoded_text = decode_type_1(number)
    elif type_ == 2:
        decoded_text = decode_type_2(number)
    elif type_ == 3:
        decoded_text = decode_type_3(number)
    else:
        decoded_text = decode_complex_format(number)
    return decoded_text

def decode_type_1(number):
    # Example decoding logic for type 1: YYMMDD
    year = "20" + number[:2]
    month = number[2:4]
    day = number[4:]
    return f"Expiry Date: {month}/{day}/{year}"

def decode_type_2(number):
    # Example decoding logic for type 2: MMDDYY
    month = number[:2]
    day = number[2:4]
    year = "20" + number[4:]
    return f"Expiry Date: {month}/{day}/{year}"

def decode_type_3(number):
    # Example decoding logic for type 3: DDMMYY
    day = number[:2]
    month = number[2:4]
    year = "20" + number[4:]
    return f"Expiry Date: {day}/{month}/{year}"

def decode_complex_format(number):
    parts = number.split()
    if len(parts) != 6 or parts[-1] != "2023": # check if the format is correct
        return "Invalid complex format. Please enter in the format 'PN23 J 27351 10:22 EXP 05/31/2023'."

    product_code = parts[0]
    category = parts[1]
    serial_number = parts[2]
    time = parts[3]
    expiry_date = parts[4]

    return f"Product Code: {product_code}, Category: {category}, Serial Number: {serial_number}, Time: {time}, Expiry Date: {expiry_date}"

def decode_expiry_date(type_, number):
    decoded_text = ""
    if type_ == 1:
        decoded_text = decode_type_1(number)
    elif type_ == 2:
        decoded_text = decode_type_2(number)
    elif type_ == 3:
        decoded_text = decode_type_3(number)
    elif type_ == 4:
        decoded_text = decode_julian_date(number)
    else:
        decoded_text = decode_complex_format(number)
    return decoded_text

def decode_julian_date(number):
    # Convert Julian date to number of days since January 1, 2000
    days = number - 2440000

    # Determine the year, month, and day
    y = 2000
    while True:
        jd = 365 * y + (y + math.floor((y - 1) / 4) - math.floor((y - 1) / 100) + math.floor((y - 1) / 400)) / 2
        if jd <= days < jd + 366:
            break
        y += 1

    m = math.floor((days - jd) / 30.6001) + 1
    d = days - jd - math.floor((m - 1) * 30.6001)

    # Format the date as a string
    return f"Expiry Date: {d}/{m}/{y}"