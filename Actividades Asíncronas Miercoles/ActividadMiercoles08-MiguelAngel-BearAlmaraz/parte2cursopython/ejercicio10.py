with open("Usernames and Passwords.txt",'w') as fi:
    username=input("Enter your username: ")
    fi.write(username)
    password=input("Enter your password: ")
    print("\n")
    fi.write(password)
    