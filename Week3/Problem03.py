password = input("Enter a new password: ")
if 8<len(password)<12:
    confirm_password = input("Confirm new password: ")
    if password == confirm_password:
        print("Password Set")
    else:
        print("Both password didn't match. Try again!")
else:
    print("Password must be between 8-12 characters.")
