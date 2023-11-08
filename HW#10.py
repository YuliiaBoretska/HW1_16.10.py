import keyword
import string
  # починатися з цифри,
  # складатися тільки з цифр,
  # містити великі літери,
  # пропуск
# і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної може складатися тільки з одного нижнього підкреслення "_".
# _ => True
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
#my_string = 'm3'
my_string = str(input('Bitte erstellen Sie ein Passwort:'' '))
check = True
Space = my_string.find(" ")
if Space >= 0:
    #print('space error')
    check = False

if (my_string[0].isdigit()):
    #print('digit error')
    check = False

for char in my_string:
    if char.isupper():
        # print('uppercase error')
        check = False

if my_string in keyword.kwlist:
    #print('keylist error')
    check = False

for char in my_string:
  if char == '_':
        continue
  elif char in string.punctuation:
        check = False
        break

if check:
    print("True")
else:
    print("False")

