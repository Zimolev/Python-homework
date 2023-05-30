def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input("Введите фио: ")
    phone_num = input("Введите номер телефона: ")
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f"\n{fio} | {phone_num}")


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
    contakt_to_find = input('Введите ФИО или номер телефона: ')
    result = search(book, contakt_to_find)
    print(result)


def search(book: list[str], info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    result = [contact for contact in book if info in contact]
    if not result:
        return "Совпадений нет"
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('________________')
        print('\n'.join(result))
        new_info = input('Введите уточнения поиска: ')
        return search(result, new_info)
    
def change():
    with open('book.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
    print('\n'.join(book))
    contakt_to_find = input('Введите ФИО или номер телефона: ')
    contakt_to_find = search(book, contakt_to_find)
    print(f'Найденный контакт для изменения или удаления: {contakt_to_find}')
    index_2 = int(input("Хотите изменить, нажмите 1, удалить - нажмите 2: "))
    if index_2 == 1:
        book[book.index(contakt_to_find)] = new_contact()
    else:
        book.remove(contakt_to_find)
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(book))


def new_contact():
    fio = input("Введите фио: ")
    phone_num = input("Введите номер телефона: ")
    return f'{fio} | {phone_num}'


