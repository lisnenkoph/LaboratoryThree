value_of_items = {'в': (3, 25), 'п': (2, 15), "б": (2, 15), "а": (2, 20), "и": (1, 5),
                  "н": (1, 15), "т": (3, 20), "о": (1, 25), "ф": (1, 15), "д": (1, 10), "к": (2, 20), "р": (2, 20)}

start_value = 15
result_value = 0


def get_area_and_value(value_of_items):
    area = [value_of_items[item][0] for item in value_of_items]
    value = [value_of_items[item][1] for item in value_of_items]
    summ = sum(value)
    return area, value, summ


def get_memtable(value_of_items, A=8):
    area, value, summ = get_area_and_value(value_of_items)
    n = len(value)
    K = [[0 for a in range(A + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for a in range(A + 1):
            if i == 0 or a == 0:
                K[i][a] = -summ
            elif area[i - 1] <= a:
                after = value[i - 1] + K[i - 1][a - area[i - 1]]
                K[i][a] = max(after, K[i - 1][a])
            # если площадь предмета больше площади столбца, забираем значение ячейки из предыдущей строки
            else:
                K[i][a] = K[i - 1][a]

    return K, area, value


def get_selected_items_list(value_of_items, A):
    K, area, value = get_memtable(value_of_items)
    n = len(value)
    res = K[n][A]  # начинаем с последнего элемента
    a = A  # площадь с начала - макс.
    items_list = []  # список занимаемых ячеек и ценностей

    for i in range(n, 0, -1):  # идём в обратном порядке
        if a <= 0:  # условие прерывания
            break
        if res == K[i - 1][a]:
            continue
        else:
            items_list.append((area[i - 1], value[i - 1]))
            res -= value[i - 1]  # отнимаем значение ценности от общей
            a -= area[i - 1]

    selected_stuff = []
    mas = []
    for search in items_list:
        for key, value in value_of_items.items():
            if value == search and (key not in selected_stuff):
                selected_stuff.append(key)
                k = value[0]
                mas.extend([[key]] * k)
                break
    return selected_stuff, mas


stuff, mas = get_selected_items_list(value_of_items, 8)
K, area, value, = get_memtable(value_of_items)
summ1 = sum(value) - abs(K[-1][-1])  # сумма взятых предметов
result_value = summ1 - abs(K[-1][-1]) + start_value
print(mas[0:4])
print(mas[4:])
print('\nИтоговые очки выживания:', result_value)

#Допзадание
''' 
    В 7 ячеек невозможно сложить предметы, получив положительный счет, докажем это
    Ингалятор и антидот не нужен
    Берём максимально выгодные предметы с наибольшей ценностью и наименьшим местом:
    ("о": (1, 25), "н": (1, 15), "ф": (1, 15), остается 4 места, можем взять 'а': (2, 20) и "к": (2, 20) 
    7 ячеек занято, итоговый счет очков: 95
    Всего: 205
    Взяв максимально выгодные предметы, получили отрицательное количество очков. 
    Получается, что в 7 ячеек сложить предметы не получится 
'''