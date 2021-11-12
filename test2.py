# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

list_number = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = []
for el in range(len(list_number)):
    if list_number[el - 1] < list_number[el]:
        new_list.append(list_number[el])

print(f"Исходный список " + str(list_number))
print(f"Элементы исходного списка, значения которых больше предыдущего элемента" + str(new_list))