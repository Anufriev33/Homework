# Задача №5

# Требуется найти в массиве list_1 
# самый близкий по величине элемент к заданному числу k и вывести его.

# list_1 = [1, 2, 3, 4, 5]
# k = 6

# closest_element = list_1[0]  # предполагаем, что первый элемент ближайший
# min_diff = abs(k - closest_element)  # предполагаем, что разница с первым элементом наименьшая

# for num in list_1:
#     diff = abs(k - num)  # находим разницу между числом k и текущим элементом
#     if diff < min_diff:  # если разница меньше минимальной
#         min_diff = diff  # обновляем минимальную разницу
#         closest_element = num  # обновляем ближайший элемент

# print(closest_element)  # выводим ближайший элемент


               
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)