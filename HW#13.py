# Користувач вводить через дефіс дві літери,
# Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
# Приклад:
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA
import string
my_string = input('Ent:''')
start, end = my_string.split('-')
#print(start, end)
start_i = string.ascii_letters.index(start)
end_i = string.ascii_letters.index(end)
#print(start_i, end_i)
print(string.ascii_letters[start_i:end_i+1])

