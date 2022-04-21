# Asks for a new password
locked = False
password = input("enter your new password: ")

# Checks if a legal password was entered
while "#" not in password or len(password) < 8:
    if len(password) < 8:
        password = input("Your password must be at least 8 characters: ")
    else:
        password = input("Your password must have at least 1 '#' : ")

# Confirms password
while not locked:
    confirmPassword = input("confirm your password: ")
    if password == confirmPassword:
        print("password updated successfully")
        locked = True
    else:
        print("Your password does not match")
