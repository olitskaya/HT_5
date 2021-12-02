# На основі попередньої функції створити наступний кусок кода:
# а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
# б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
# Name: vasya
# Password: wasd
# Status: password must have at least one digit
# -----
# Name: vasya
# Password: vasyapupkin2000
# Status: OK
# P.S. Не забудьте використати блок try/except ;

class UsernameException(Exception):
	pass
	
class PasswordException(Exception):
	pass	

def user(username, password):
    print(f"\n\nusername: {username}\npassword: {password}\nStatus:")
    if len(username) >= 3 and len(username) <= 50:
        if len(password) >= 8 and password.isalpha() == False and password.isalnum():
            print(f"Ok.")
    try:
        if len(username) < 3 or len(username) > 50:
            raise UsernameException("Username must be at least 3 characters and no more than 50 characters.")
    except UsernameException as e:
        print(f"{e}")        
    try:    
        if len(password) < 8 or password.isalpha() or password.isalnum() == False:
            raise PasswordException("Password must be at least 8 characters and contain only letters and at least 1 number.")
    except PasswordException as e:
        print(f"{e}")    

users = {'username1': 'password1', 'us': 'password2', 'username3': 'passwo', 'u': 'password_4'}
for key, value in users.items():
    user(key, value)
