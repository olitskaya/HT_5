class LoginException(Exception):
    pass

def user(username, password, silent=False):
    users = {'username1': 'password1', 'username2': 'password2', 'username3': 'password3',
            'username4': 'password4', 'username5': 'password5'}
    for key, value in users.items():
        if (username == key and password == value):
            return True 
        if (username != key and password != value and silent == True):
            return False 
        if (username != key and password != value and silent == False):
            raise LoginException("Wrong login and password!")
    
test_username = str(input("Enter username: "))
test_username = test_username.lower()
test_password = str(input("Enter password: "))
print(user(test_username, test_password))