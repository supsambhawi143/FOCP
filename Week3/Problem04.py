BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password= input("Enter a New Password: ")
    confirm= input("Confirm Password: ")

    if (password or confirm) in BAD_PASSWORDS :
        print("BAD PASSWORD.")

    elif (password== confirm) and (len(password)>= 8 and len(password)<= 12) :
        print("Password Set.")
        break
    else:
        print("Password  must of length of 8 to 12 character.")