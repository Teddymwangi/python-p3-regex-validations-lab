# tests/test_regex.py
from lib.regex import validate_name, validate_phone_number, validate_email

def test_validate_name():
    assert validate_name("John Cena") == True
    assert validate_name("Alice") == True
    assert validate_name("Bob Smith") == True
    assert validate_name("123") == False
    assert validate_name("John123") == False
    assert validate_name("John Cena 123") == False

def test_validate_phone_number():
    assert validate_phone_number("123-456-7890") == True
    assert validate_phone_number("999-9999") == False
    assert validate_phone_number("123-456-789") == False
    assert validate_phone_number("1234567890") == False
    assert validate_phone_number("12-3456-7890") == False

def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("test.email@example.com") == True
    assert validate_email("test.email@example.co.jp") == True
    assert validate_email("invalid_email.com") == False
    assert validate_email("test@invalid@com") == False
    assert validate_email("test@example") == False
