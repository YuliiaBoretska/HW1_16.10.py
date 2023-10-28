# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.
# Приклад:
# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]
#Заповнити список випадковою кількістю елементів від 6 до 15 та випадковим значенням від 1 до 100,
# і порахувати їхню суму.
# my_list = []
# Не найоптимальніший варіант рішення
# for i in range(random.randint(3, 10)):
#     my_list.append(random.randint(1, 10))
# print(my_list)
# summa = 0
# for element in my_list:
#     summa += element
# print(summa)
import random
my_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]
my_list2 = []
i = 0
for a in my_list:
    my_list2 = [my_list[i], my_list[i + 2], my_list[-2]]
print(my_list)
print(my_list2)

