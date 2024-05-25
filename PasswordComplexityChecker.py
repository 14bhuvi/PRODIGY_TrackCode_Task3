import re

def check_digit(pwd: str) -> bool:
    return bool(re.search(r'[0-9]', pwd))
  
def check_uppercase(pwd: str) -> bool:
    return bool(re.search(r'[A-Z]', pwd))
  
def check_lowercase(pwd: str) -> bool:
    return bool(re.search(r'[a-z]', pwd))
  
def check_special_char(pwd: str) -> bool:
    return bool(re.search(r'[~!@#$%^&*?]', pwd))
  
def check_white_space(pwd: str) -> bool:
    return bool(re.search(r'\s', pwd))
  
def check_length(pwd: str) -> bool:
    return 6 <= len(pwd) <= 8

while True:
    pwd = input("Write your password for your account: ")

    if all([check_digit(pwd),
            check_lowercase(pwd),
            check_uppercase(pwd),
            check_special_char(pwd),
            not check_white_space(pwd),
            check_length(pwd)]):
        print("Your password is strong. You are good to go -->")
        break
    else:
        print("Your password is not strong. Fill it up with these requirements:")
        if not check_digit(pwd):
            print("- Password must contain at least a number from 0-9")
        if not check_uppercase(pwd):
            print("- Password must have at least an uppercase from A-Z")
        if not check_lowercase(pwd):
            print("- Password must have at least a lowercase from a-z")
        if not check_special_char(pwd):
            print("- Password must have at least a special character [~!@#$%^&*?]")
        if check_white_space(pwd):
            print("- Password should not contain any white or blank space")
        if check_length(pwd):
            print("- Password must be of 6 to 8 characters length.")
