# Задача №31 ========================================================================
# Последовательностью Фибоначчи называется последовательность чисел 
# a(0), a1, ..., a(n), где a(0) = 0, a(1)  = 1, a(k) = a(k-1) + a(k-2) (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

'''
def FibonacciNextElem(previous, next, lastNumber):
    if lastNumber == 0:
        return
    print(previous, end=' ')
    FibonacciNextElem(next, next + previous, lastNumber - 1)

previous = 0
next = 1
# lastNumber = int(input("Введите длину ряда Фибоначчи для его вывода... "))
lastNumber = 20

FibonacciNextElem(previous, next, lastNumber)
'''

# Введите длину ряда Фибоначчи для его вывода... 20
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 

# Задача №33 ========================================================================
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, которая заменяет оценки 
# Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

'''
import random as rnd

def replaceScore(scoreList):
    return list(map(lambda item: (1 if item > 3 else item), scoreList))

scoreList = [rnd.randint(1,5) for i in range(0,20)]
print(scoreList)
print(replaceScore(scoreList))
'''

# [2, 4, 4, 3, 2, 5, 1, 3, 4, 3, 4, 2, 4, 3, 5, 2, 5, 2, 4, 1]
# [2, 1, 1, 3, 2, 1, 1, 3, 1, 3, 1, 2, 1, 3, 1, 2, 1, 2, 1, 1]

# Задача №35 ========================================================================
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 
'''
def isSimple (num):
    for i in range(2, num-1):
        if num % i == 0:
            return "Число НЕ простое."
    return "Число ПРОСТОЕ."

userNumber = int(input("Введите число для проверки на простоту... "))
print(isSimple(userNumber))
'''

# Задача №37 ========================================================================
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

'''
import random as rnd

def reverseList (userList):
    print("[", end='')
    printReversedList(userList, 0)


def printReversedList (userList, index):
    if index > len(userList) - 1:
        return
    printReversedList(userList, index + 1)
    if index == 0:
        pointer = "]"
    else:
        pointer = ", "
    print (userList[index], end = pointer)


list = [rnd.randint(0,10) for i in range(0,10)]
print(list)
reverseList(list)
'''