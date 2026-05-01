user_name = "KIIT"
password = "1234"
max_attempt = 3
for  attempt in range (1,max_attempt +1):
    username = input("enter username :")
    Password = input("enter your password :")
    if user_name == username and password == Password :
        print("Access granted!")
        break
    else :
        remaining = max_attempt - attempt
    if remaining>0 :
        print("Incorrect credentials {remaining}attempts left")
    else :
        print("Account locked! Too many wrong attempts.")
