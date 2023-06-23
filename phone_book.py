phonebook = dict()
path = 'phones.txt'

def print_message(message): #┌─┐└─┘│
    print("┌" + "─" * (len(message) + 2) + "┐")
    print("│ " +        message         + " │")
    print("└" + "─" * (len(message) + 2) + "┘")

def menu() -> int:
    main_menu = '''Работа с телефонным справочиником:
    (1) открыть файл                (5) найти контакт  
    (2) сохранить файл              (6) изменить контакт
    (3) показать все контакты       (7) удалить контакт
    (4) добавить новый контакт      (8) выход из программы'''
    print(main_menu)
    while True:
        select = input("\nВыберите пункт меню... > ")
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print_message("Ошибка ввода (необходимо ввести цифры от 1 до 8). Попробуйте ещё раз.")


def open_file(path = 'phones.txt'):
    phonebook_file = open(path, 'r', encoding="UTF-8")
    data = phonebook_file.readlines() # .readlines() преобразует файл в список, где элементы - строки
    phonebook_file.close
    phonebook.clear
    for line in data:
        contact = line.split(':')
        phonebook[int(contact[0])] = {'name': contact[1].strip(), 'phone': contact[2].strip(), 'comment': contact[3].strip()}
        # телефонная книга - словарь, где ключ = ИНТ, значение ключа (это тоже словарь) - строка из файла
    print_message('(+) Телефонная книга успешно загружена')


def save_file():
    data = []
    for i, contact in phonebook.items():
        line = ":".join([str(i), contact['name'], contact['phone'], contact['comment']])
        data.append(line)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as phonebook_file:
        phonebook_file.write(data)
    print_message(f"Телефонная книга успешно сохранена в файл {path}.")
    

def print_contacts (data: dict[int, dict]):#┌─┬─┐└─┴─┘│├─┼─┤
    if len(data) != 0:
        idField = 4
        nameField    = max([len(item['name']) for item in data.values()]) #максимальная из списка длин полей NAME
        commentField = max([len(item['comment']) for item in data.values()])
        phoneField   = max([len(item['phone']) for item in data.values()])
        print("┌" + "─" * idField + "┬" + "─" * nameField + "┬" +"─" * commentField + "┬" + "─" * phoneField + "┐")
        print("│" + "ID".center(idField) + "│" + "ИМЯ".center(nameField) + "│" + "КОММЕНТ".center(commentField) + "│" + "ТЕЛЕФОН".center(phoneField) + "│")
        print("├" + "─" * idField + "┼" + "─" * nameField + "┼" +"─" * commentField + "┼" + "─" * phoneField + "┤")


        for i, contact in data.items():
            print(f"│{i:^{idField}}│{contact['name']:<{nameField}}│{contact['comment']:<{commentField}}│{contact['phone']:<{phoneField}}│")
        print("└" + "─" * idField + "┴" + "─" * nameField + "┴" +"─" * commentField + "┴" + "─" * phoneField + "┘")
    else:
        print("Список пуст. Выводить нечего.")


def add_contact():
    print_message("Введите данные нового контакта")
    newID = max(list(phonebook.keys())) + 1
    newName    = input("Имя контакта >> ").strip()
    newPhone   = input("Телефон      >> ").strip()
    newComment = input("Комментарий  >> ").strip()
    phonebook[newID] = {'name': newName, 'phone': newPhone, 'comment': newComment}
    print_message(f"Контакт \"{newName}\" успешно добавлен.")


def search_contact(target = ''):
    result = {}
    print_message(f" ПОИСК {target.upper()}... ")
    requestWord = input("Введите поисковый запрос >> ").lower()
    for i, contact in phonebook.items():
        if requestWord in ' '.join(list(contact.values())).lower():
            result[i] = contact
    return result

def remove_contact():
    print_contacts(search_contact("для удаления"))
    indexToRemove = int(input("Введите ID контакта для удаления >> "))
    contactToRemove = phonebook.pop(indexToRemove)
    print_message(f" Контакт \"{contactToRemove['name']}\" успешно удалён ! ")


def edit_contact():
    editDict = search_contact("для редактирования")
    if len(editDict) == 0:
        print("Ничего не найдено...")
    else:
        print_contacts(editDict)
        indexToRemove = int(input("Введите ID контакта для ИЗМЕНЕНИЯ >> "))
        if  indexToRemove in editDict.keys():
            print("Введите новые данные контакта:")
            phonebook[indexToRemove]['name']    = input("Имя контакта >> ").strip()
            phonebook[indexToRemove]['phone']   = input("Телефон      >> ").strip()
            phonebook[indexToRemove]['comment'] = input("Комментарий  >> ").strip()
            print_message(f"Контакт \"{phonebook[indexToRemove]['name']}\" успешно добавлен.")
        else:
            print("Контакта с таким ID нет среди найденных")
            select = input("Повторить поиск ? (Введите \"+\", если ДА, и \"-\", если НЕТ) > ")
            if select == "+":
                edit_contact()


def exit_program():
    while True:
        print_message("Сохранить изменения адресной книги в файл?")
        select = input("Введите \"+\", если ДА, и \"-\", если НЕТ) > ")
        if select == "+":
            save_file()
            break
        if select == "-":
            print_message("ВОТ и ВСЁ !")
            break



    

open_file()
while True:
    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            print_contacts(phonebook)
        case 4:
            add_contact()
        case 5:
            print_contacts(search_contact())
        case 6:
            edit_contact()        
        case 7:
            remove_contact()
        case 8:
            exit_program()
            break
    print("░" * 100)

