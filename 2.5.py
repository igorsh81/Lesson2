# 2.5
# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
while True:
    n = int(input("Введите число: ").strip())
    my_list.append(n)
    my_list.sort(reverse=True)
    print(my_list)
