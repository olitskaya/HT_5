# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
# P.S. Повинен вертатись генератор.
# P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range

def range_test(start, stop = 0, step = 1):
    if stop == 0:
        stop = start
        start = 0
    while start < stop:
        yield start 
        start = start + step
