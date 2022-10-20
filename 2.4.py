# 2.4
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

the_words = input("Введите несколько слов, разеделённых пробелами: ").split(" ")

numbering = 1

for n in range(0, len(the_words), 1):
    if len(the_words[n]) > 10:
        print(f"{numbering}. {the_words[n][0:10]}")
        numbering += 1
    else:
        print(f"{numbering}. {the_words[n]}")
        numbering += 1