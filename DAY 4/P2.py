username = ''
password = ''

while (username!="admin" and password!="hello"):
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    print("Incorrect! Try again.")
    
print("Correct! Login Successful.")
