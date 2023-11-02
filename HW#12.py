# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
#  ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
#      підсумкова довжина hashtag має бути не більше 140 символів.
#      кожне слово починається з великої літери.
#     якщо довжина хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
# Приклади:
# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
import string
#my_string = 'Should, I. subscribe? Yes!'
my_string = str(input('Enter:'' '))
my_string = my_string.title()
for i in string.punctuation:
    if i in my_string:
        my_string = my_string.replace(i, '')
#print(my_string)
my_string = my_string.replace(' ', '')
c = len(my_string)
my_string = my_string.rjust(c+1, '#')
my_string = my_string[:140]
print(my_string)


# lst2 = list(my_string)
#lst = my_string1.split()
#my_string1 = "".join(lst)
#print(my_string1)





