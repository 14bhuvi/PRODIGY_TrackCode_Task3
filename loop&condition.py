while True:                          #using this we can have a loop and can use this if the contion gets false
    pwd = input("Write your password for your account: ")

    if all([check_digit(pwd),       #this condition is true hence,
            check_lowercase(pwd),
            check_uppercase(pwd),
            check_special_char(pwd),
            not check_white_space(pwd),
            check_length(pwd)]):
        print("Your password is strong. You are good to go -->")
        break                      #break statement is used to stop the loop is condition gets under true
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
            print("- Password must be of 6 to 8 characters length.")           #the loop continues after this condition 
