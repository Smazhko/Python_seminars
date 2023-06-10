# arr - отсоритровнная последовательность. k - число.
# Нужно найти индекс k. Если к нет, то вывести -1
# import os
# os.system('cls')

def BinarySearch(array, findNumber, logFlag):
    if findNumber < array[0] or findNumber > array[-1]:
        return f"    Число {findNumber} находится вне диапазона поиска"
    return f"    Бинарный поиск (рекурсия): {BinarySearchRecursion(array, findNumber, 0, len(array) - 1, logFlag)}"
    # return f"    Бинарный поиск (цикл): {BinarySearchCycle(array, findNumber, logFlag)}"


def BinarySearchRecursion(array, findNumber, start, finish, logFlag):
    # if finish - start <= 1:
    #     if array[start] == findNumber:            
    #         return f"индекс числа {findNumber} = {start}"
    #     elif array[finish] == findNumber:
    #         return f"индекс числа {findNumber} = {finish}"
    #     else:
    #         return "такого числа нет в массиве, -1"
    middleIndex = (start + finish) // 2
    if logFlag:
        print(f"    {start}...{middleIndex}...{finish}: числа {array[start]} ... {array[middleIndex]} ... {array[finish]}")
    
    if finish == start:
        if array[start] == findNumber:            
            return f"индекс числа {findNumber} = {start}"
        else:
            return f"числа {findNumber} нет в массиве"
        

    if findNumber == array[middleIndex]:
        return f"индекс числа {findNumber} это {middleIndex}"
    else:
        if findNumber > array[middleIndex]:
            return(BinarySearchRecursion(array, findNumber, middleIndex + 1, finish, logFlag))
        else:
            return(BinarySearchRecursion(array, findNumber, start, middleIndex - 1, logFlag))


def BinarySearchCycle (array, target, logFlag):
    begin = 0
    end = len(array) - 1

    while (begin != end):
        middle = (begin + end) // 2
        if logFlag:
            print(f"    {begin}...{middle}...{end}: числа {array[begin]} ... {array[middle]} ... {array[end]}")
        
        if array[middle] == target:
            return f"индекс числа {target} = {middle}"
        else:
            if array[middle] > target:
                end = middle - 1
            else:
                begin = middle + 1

        if logFlag:
            print(f"          следующий диапазон: {begin}...{end}: числа {array[begin]} ... {array[end]}")
        if array[begin] == target:
            return f"индекс числа {target} = {begin}"
        if array[end] == target:
            return f"индекс числа {target} = {end}"
    return f"числа {target} нет в массиве"


def LineSearch(array, findNumber):
    if findNumber > array[-1] or findNumber < array[0]:
        return -1
    for i in range(len(array) - 1):
        if array[i] == findNumber:
            return f"Линейный поиск: индекс числа {findNumber}  = {i}"
    else:
        return "Линейный поиск: такого числа нет в массиве, -1"


array = list()
min, max = 100, 200
for i in range(min, max + 1):
    array.append(i)

logFlag = False

delIndex = 29
delNumber = array.pop(delIndex)
print(f"Из массива удалено число {delNumber} (индекс {delIndex})")

# number = int(input("Введите число для поиска... "))
# print(LineSearch(array, number))

number = array[delIndex - 1]
print("ищем число " + str(number))
print(BinarySearch(array, number, logFlag))
number = delNumber
print("ищем число " + str(number))
print(BinarySearch(array, number, logFlag))
number = array[delIndex]
print("ищем число " + str(number))
print(BinarySearch(array, number, logFlag))
number = min
print("ищем число " + str(number))
print(BinarySearch(array, number, logFlag))
number = max
print("ищем число " + str(number))
print(BinarySearch(array, number, logFlag))
number = min - 1
print("ищем число " + str(number))
print(BinarySearch(array, number, logFlag))
number = max + 1
print("ищем число " + str(number))
print(BinarySearch(array, number, logFlag))

# Удаляем индекс 29 (число 129)
# ищем число 128
#     0...49...99: числа 100 ... 150 ... 200
#           следующий диапазон: 0...48: числа 100 ... 149
#     0...24...48: числа 100 ... 124 ... 149
#           следующий диапазон: 25...48: числа 125 ... 149
#     25...36...48: числа 125 ... 137 ... 149
#           следующий диапазон: 25...35: числа 125 ... 136
#     25...30...35: числа 125 ... 131 ... 136
#           следующий диапазон: 25...29: числа 125 ... 130
#     25...27...29: числа 125 ... 127 ... 130
#           следующий диапазон: 28...29: числа 128 ... 130
#     Бинарный поиск (цикл): индекс числа 128 = 28
# ищем число 129
#     0...49...99: числа 100 ... 150 ... 200
#           следующий диапазон: 0...48: числа 100 ... 149
#     0...24...48: числа 100 ... 124 ... 149
#           следующий диапазон: 25...48: числа 125 ... 149
#     25...36...48: числа 125 ... 137 ... 149
#           следующий диапазон: 25...35: числа 125 ... 136
#     25...30...35: числа 125 ... 131 ... 136
#           следующий диапазон: 25...29: числа 125 ... 130
#     25...27...29: числа 125 ... 127 ... 130
#           следующий диапазон: 28...29: числа 128 ... 130
#     28...28...29: числа 128 ... 128 ... 130
#           следующий диапазон: 29...29: числа 130 ... 130
#     Бинарный поиск (цикл): числа 129 нет в массиве
# ищем число 130
#     0...49...99: числа 100 ... 150 ... 200
#     0...24...48: числа 100 ... 124 ... 149
#     25...36...48: числа 125 ... 137 ... 149
#           следующий диапазон: 25...29: числа 125 ... 130
#     Бинарный поиск (цикл): индекс числа 130 = 29
# ищем число 100
#     0...49...99: числа 100 ... 150 ... 200
#           следующий диапазон: 0...48: числа 100 ... 149
#     Бинарный поиск (цикл): индекс числа 100 = 0
#           следующий диапазон: 50...99: числа 151 ... 200
#     Бинарный поиск (цикл): индекс числа 200 = 99
# ищем число 99
#     Число 99 находится вне диапазона поиска

# ==============================================================
# Удаляем индекс 29 (число 129)
# ищем число 128
#     0...49...99: числа 100 ... 150 ... 200
#     0...24...48: числа 100 ... 124 ... 149
#     25...36...48: числа 125 ... 137 ... 149
#     25...30...35: числа 125 ... 131 ... 136
#     25...27...29: числа 125 ... 127 ... 130
#     28...28...29: числа 128 ... 128 ... 130
#     Бинарный поиск (рекурсия): индекс числа 128 это 28
# ищем число 129
#     0...49...99: числа 100 ... 150 ... 200
#     0...24...48: числа 100 ... 124 ... 149
#     25...36...48: числа 125 ... 137 ... 149
#     25...30...35: числа 125 ... 131 ... 136
#     25...27...29: числа 125 ... 127 ... 130
#     28...28...29: числа 128 ... 128 ... 130
#     29...29...29: числа 130 ... 130 ... 130
#     Бинарный поиск (рекурсия): числа 129 нет в массиве
# ищем число 130
#     0...49...99: числа 100 ... 150 ... 200
#     0...24...48: числа 100 ... 124 ... 149
#     25...36...48: числа 125 ... 137 ... 149
#     25...30...35: числа 125 ... 131 ... 136
#     25...27...29: числа 125 ... 127 ... 130
#     28...28...29: числа 128 ... 128 ... 130
#     29...29...29: числа 130 ... 130 ... 130
#     Бинарный поиск (рекурсия): индекс числа 130 = 29
# ищем число 100
#     0...49...99: числа 100 ... 150 ... 200
#     0...24...48: числа 100 ... 124 ... 149
#     0...11...23: числа 100 ... 111 ... 123
#     0...5...10: числа 100 ... 105 ... 110
#     0...2...4: числа 100 ... 102 ... 104
#     0...0...1: числа 100 ... 100 ... 101
#     Бинарный поиск (рекурсия): индекс числа 100 это 0
# ищем число 200
#     0...49...99: числа 100 ... 150 ... 200
#     50...74...99: числа 151 ... 175 ... 200
#     75...87...99: числа 176 ... 188 ... 200
#     88...93...99: числа 189 ... 194 ... 200
#     94...96...99: числа 195 ... 197 ... 200
#     97...98...99: числа 198 ... 199 ... 200
#     99...99...99: числа 200 ... 200 ... 200
#     Бинарный поиск (рекурсия): индекс числа 200 = 99
# ищем число 99
#     Число 99 находится вне диапазона поиска
# ищем число 201
#     Число 201 находится вне диапазона поиска