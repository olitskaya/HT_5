# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
# - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
# - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
# - щось своє :)
# Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.

class LoginException(Exception):
    pass

def user(username, password):
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
