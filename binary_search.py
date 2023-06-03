# arr - отсоритровнная последовательность. k - число.
# Нужно найти индекс k. Если к нет, то вывести -1
# import os
# os.system('cls')

def BinarySearch(array, findNumber):
    if findNumber < array[0] or findNumber > array[-1]:
        return f"    Число {findNumber} находится вне диапазона поиска"
    # return f"    Бинарный поиск (рекурсия): {BinarySearchRecursion(array, findNumber, 0, len(array) - 1)}"
    return f"    Бинарный поиск (цикл): {BinarySearchCycle(array, findNumber)}"


def BinarySearchRecursion(array, findNumber, start, finish):
    # if finish - start <= 1:
    #     if array[start] == findNumber:            
    #         return f"индекс числа {findNumber} = {start}"
    #     elif array[finish] == findNumber:
    #         return f"индекс числа {findNumber} = {finish}"
    #     else:
    #         return "такого числа нет в массиве, -1"
    middleIndex = (start + finish) // 2
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
            return(BinarySearchRecursion(array, findNumber, middleIndex + 1, finish))
        else:
            return(BinarySearchRecursion(array, findNumber, start, middleIndex - 1))


def BinarySearchCycle (array, target):
    begin = 0
    end = len(array) - 1

    while (begin != end):
        middle = (begin + end) // 2
        print(f"    {begin}...{middle}...{end}: числа {array[begin]} ... {array[middle]} ... {array[end]}")
        
        if array[middle] == target:
            return f"индекс числа {target} = {middle}"
        else:
            if array[middle] > target:
                end = middle - 1
            else:
                begin = middle + 1

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

delIndex = 29
delNumber = array.pop(delIndex)
print(f"Удаляем индекс {delIndex} (число {delNumber})")

# number = int(input("Введите число для поиска... "))
# print(LineSearch(array, number))

number = array[delIndex - 1]
print("ищем число " + str(number))
print(BinarySearch(array, number))
number = delNumber
print("ищем число " + str(number))
print(BinarySearch(array, number))
number = array[delIndex]
print("ищем число " + str(number))
print(BinarySearch(array, number))
number = min
print("ищем число " + str(number))
print(BinarySearch(array, number))
number = max
print("ищем число " + str(number))
print(BinarySearch(array, number))
number = min - 1
print("ищем число " + str(number))
print(BinarySearch(array, number))
number = max + 1
print("ищем число " + str(number))
print(BinarySearch(array, number))