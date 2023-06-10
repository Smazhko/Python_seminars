# Задача №25. 
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# text = input("Введите любую строку: ")

# dict_text = {item: -1 for item in set(text)} # ГЕНЕРАТОР СЛОВАРЯ - ШИКАРНО !

# for i in list(text):
#     dict_text[i] = dict_text[i] + 1
#     if dict_text[i] == 0:
#         print(f'{i}', end=' ')
#     else:
#         print(f'{i}_{dict_text[i]}', end=' ')

# ============== со срезами ========== НЕ РАБОТАЕТ если вводить строку без пробелов между буквами
# s = input()
# s = s.split()
# print(s)
# final_string = ''
# for i in range(len(s)):
#     if s[0:i].count(s[i]) == 0:
#         final_string += f' {s[i]}'
#     else:
#         final_string += f' {s[i]}_{s[0:i].count(s[i])}'
# print(final_string)

# ====== РЕШЕНИЕ С GET =====================
# st = list(input("Введите строку: "))
# print(st)
# d = {}
# p = ""
# for i in range(len(st)):
#     if d.get(st[i]) != None:
#         d[st[i]] = int(d[st[i]])+1
#     else:
#         d[st[i]] = 1
#     p = p + f"{st[i]}_{d[st[i]]}"
# print(p)

# =================================================================================================
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13
# print('aBcdEfg.?,!'.strip('.?,!\n').lower())

# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

# list_text = list(text.split())

# for i in range(len(list_text) - 1):
#     list_text[i] = list_text[i].strip('.?,!\n').lower()

# print(f"В тексте встречается {len(set(list_text))} различных слов.")


# Задача №29. ==========================================================================
# Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность)




