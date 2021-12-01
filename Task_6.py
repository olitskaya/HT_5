# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
# P.S. Повинен вертатись генератор.
# P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range

def range_test(start, stop, step = 1):
	list_test = []
	list_test.append(start)
	i = start
	while i < stop :
		i += step
		list_test.append(i)
	yield i
