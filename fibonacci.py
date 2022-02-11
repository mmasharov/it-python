# Создаем функцию, которая вычисляет элементы последовательности Фибоначчи длинной в i элементов
def nfib(i):
    # Задаем исходные элементы для вычисления последовательности
    x1, x2 = 0, 1
    # Запускаем цикл, который вычисляет нужное количество элементов последовательности
    for iter in range(i):
        # Вычисляется элемент i
        fibnumber = x1 + x2
        # Функция возвращает вычисленное значение и продолжает выполнение
        yield fibnumber
        # С помощью метода присваивания кортежа меняем исходные элементы вычисления, после чего завершается текущая итерация цикла
        x1, x2 = x2, fibnumber

# Так как результат выполнения функцтт nfib - набор итерируемых объектов, то создаем из него список функцией list и выводим его на печать
print('Список 20 чисел Фибоначчи через функцию list:')
data1 = list(nfib(20))
print(data1)

# Тот же список создаем с помощью генератора списков
print('Список 20 чисел Фибоначчи через генератор списков:')
data2 = [x for x in nfib(20)]
print(data2)

# Выводим элементы списка перебором через цикл
print('Список 20 чисел Фибоначчи через перебор циклом for:')
for x in nfib(20):
    print(x, end=',')
print('')

# Выводим элементы через генератор множеств, в отличие от списка тут получается неупорядоченная структура
print('Неупорядоченный список 20 чисел Фибоначчи через генератор множеств:')
data3 = {x for x in nfib(20)}
print(data3)