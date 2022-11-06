while(True):
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Password must be between 8-12 characters.")
    else:
        print("Save Password")