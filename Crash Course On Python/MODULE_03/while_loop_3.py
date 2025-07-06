username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()
#This code will give an error because get_username is not defined