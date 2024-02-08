# decoder.py

def calculate_julian_date(year, month, day):
    """
    Calculate Julian date from the given date.
    Algorithm source: https://en.wikipedia.org/wiki/Julian_day
    """
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    julian_day = day + ((153 * m + 2) // 5) + 365 * y + (y // 4) - (y // 100) + (y // 400) - 32045
    return julian_day

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
    if len(parts) != 4:
        return "Invalid complex format. Please enter in the format 'PN23 J 27351 10:22'."

    product_code = parts[0]
    category = parts[1]
    serial_number = parts[2]
    time = parts[3]

    decoded_text = f"Product Code: {product_code}, Category: {category}, Serial Number: {serial_number}, Time: {time}"
    return decoded_text
