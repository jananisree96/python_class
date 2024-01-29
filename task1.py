username = input("Enter username: ")

if not username:
    print("Enter a username.")
else:
    password = input("Enter password: ")

    if len(password) < 8:
        print("Password should be at least 8 characters.")
    else:
        confirm_password = input("Confirm password: ")

        if password != confirm_password:
            print("Passwords do not match. Please provide matching passwords.")
        elif username == password:
            print("Username and password cannot be the same. Please choose another password.")
        else:
            print("Registration successful!")
                           
