def login():
    username= input("Enter username: ")
    password= input("Enter password: ")

    if username==password:
        print("Login successful!")
    else:
        print("Invalid Credentials.")
        login()

login()