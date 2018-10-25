#Gabriel Harrison
#10/1/18
#password program


def check_account(user_name, password):
    username=user_name
    password=password
    enter_username=input("Enter your user name")
    enter_password=input("Enter your password")
    if username == enter_username and password == enter_password or enter_username =="admin":
        return True
    else:
        print("Access denied")
        check_account(username,password)
    
                        
    



def get_password():
    print("Your password must start with a capital letter \n and must contain at least 1 symbol \n and must be at least 10 characters long")
    password=input("Enter your password")
    if password.istitle() and not password.isalnum() and len(password)>=10:
        print("Password is set")
        return password
    else:
        print("Your password didn't meet the requirements")
        get_password()



def get_username():
    print("Your user name must contain numbers and letters\n can only contain 10 characters \n must contain at least 3 characters")
    username=input("Enter your user name")
    if username.isalpha() and len(username)>=3 and len(username)<= 10:
        print("Your user name is set")
        return username
    else:
        print("Your user name didn't meet the requirements")
        get_username()


def menu():
    choice = 0
    while choice == 0:
        
        print("To sign up press 1")
        print("To sign in press 2")
        choice = int(input("Enter your choice"))
        if choice == 1:
            print("Choice 1")
            user_name=get_username()
            password=get_password()
            choice = 0
            
        elif choice == 2:
            print("Choice 2")
            login=check_account(user_name, password)
            return password, user_name, login   
    



def main():
    password, username, got_in = menu()
    if got_in == True:
        print("You got in")
    else:
        print("Try again")

main()        
