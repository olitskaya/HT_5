# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
# - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
# - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
# - щось своє :)
# Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.

class LoginException(Exception):
    pass

def user(username, password):
    if len(username) >= 3 and len(username) <= 50 and len(password) >= 8 and password.isalpha() == False and password.isalnum() == True:
        return True 
    else:
        raise LoginException("Wrong login or password!")
    
test_username = str(input("Enter username: "))
test_password = str(input("Enter password: "))
print(user(test_username, test_password))
