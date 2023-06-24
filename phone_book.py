phonebook = dict()
path = 'phones.txt'

def print_message(message): #┌─┐└─┘│
    print("┌" + "─" * (len(message) + 2) + "┐")
    print("│ " +        message         + " │")
    print("└" + "─" * (len(message) + 2) + "┘")

def menu() -> int:
    main_menu = '''Работа с телефонным справочиником:
    (1) открыть файл                (6) изменить контакт
    (2) сохранить файл              (7) удалить контакт
    (3) показать все контакты       (8) выйти без сохранения
    (4) добавить новый контакт      (9) сохранить изменения и выйти
    (5) найти контакт'''
    print(main_menu)
    while True:
        select = input("\nВыберите пункт меню... > ")
        if select.isdigit() and 0 < int(select) < 10:
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
        if nameField < 3:
            nameField = 3
        if commentField < 7:
            commentField = 7
        if phoneField < 7:
            phoneField = 7
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
    newName    = input("Имя контакта >> ").strip().replace(":", "-")
    newPhone   = input("Телефон      >> ").strip().replace(":", "-")
    newComment = input("Комментарий  >> ").strip().replace(":", "-")
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
    removeDict = search_contact("для удаления")
    if len(removeDict) == 0:
        print("Ничего не найдено...")
    else:
        print_contacts(removeDict)
        indexToRemove = inputID("Введите ID контакта для УДАЛЕНИЯ")
        if  indexToRemove in removeDict.keys():
            contactToRemove = phonebook.pop(indexToRemove)
            print_message(f" Контакт \"{contactToRemove['name']}\" успешно удалён ! ")
        else:
            print("Контакта с таким ID нет среди найденных")
            select = input("Повторить поиск ? (Введите \"+\", если ДА, и \"-\", если НЕТ) > ")
            if select == "+":
                remove_contact()


def edit_contact():
    editDict = search_contact("для редактирования")
    if len(editDict) == 0:
        print("Ничего не найдено...")
        select = input("Повторить поиск ? (Введите \"+\", если ДА, и \"-\", если НЕТ) > ")
        if select == "+":
            edit_contact()
    else:
        print_contacts(editDict)
        while True:
            indexToEdit = inputID("Введите ID контакта для ИЗМЕНЕНИЯ")
            if  indexToEdit in editDict.keys():
                print("Введите новые данные контакта:")
                phonebook[indexToEdit]['name']    = input("Имя контакта >> ").strip()
                phonebook[indexToEdit]['phone']   = input("Телефон      >> ").strip()
                phonebook[indexToEdit]['comment'] = input("Комментарий  >> ").strip()
                print_message(f"Контакт \"{phonebook[indexToEdit]['name']}\" успешно изменён.")
                break
            else:
                print("Контакта с таким ID нет среди найденных")


def exit_program(saveFlag):
    if saveFlag:
        save_file()
    print_message("ВОТ и ВСЁ! Приходите ещё ^_^")

def inputID(message):
    userInput = input(message + " >> ")
    if len(userInput) != 0 and userInput.isdigit():
        return int(userInput)
    else:
        inputID("Неверный ввод. " + message)
    

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
            exit_program(False)
            break
        case 9:
            exit_program(True)
            break
    print("░" * 100)

