# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій
# - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
# якщо введено коректну пару ім'я/пароль - вертається <True>;
# якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,
# інакше (<silent> == <False>) - породжується виключення LoginException

class LoginException(Exception):
    pass

def user(username, password, silent = False):
    users = [('username1', 'password1'), ('username2', 'password2'), ('username3', 'password3'), ('username4', 'password4'), ('username5', 'password5')]
    user_test = (username, password)
    for pair in users:
        a = False
        if pair == user_test:
            a = True
            return a
    if silent:
        return a
    else:
        raise LoginException("Wrong login and password!")
    
test_username = str(input("Enter username: "))
test_username = test_username.lower()
test_password = str(input("Enter password: "))
print(user(test_username, test_password))
