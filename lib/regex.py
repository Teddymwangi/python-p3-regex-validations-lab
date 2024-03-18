# lib/regex.py
import re

def validate_name(name):
    name_regex = r'^[A-Za-z]+(?: [A-Za-z]+)?$'
    return re.match(name_regex, name) is not None

def validate_phone_number(phone_number):
    phone_regex = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(phone_regex, phone_number) is not None

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None
