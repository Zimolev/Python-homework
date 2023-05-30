def search() -> str:
    """Находит в списке записи по определенному критерию поиска"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    # book_list = book.split('\n')
    # book_list = list(enumerate(book_list)) 
    return book
    #return [contact for contact in book if info in contact]
    
def delete(book: list) -> list:
    
    index = int(input("Введите номер строки которую хотите удалить: "))
    book.pop(index)

def change(book: list) -> list:
    book = book.split('\n')
    
    index = int(input("Введите номер строки которую хотите изменить: "))
    book_str = list(book[index].split('|'))
    print(book_str)
    index_2 = int(input("Что хотите изменить ФИО нажмите 1, телефон нажмите 2: "))
    if index_2 == 1:
        fio = input("Введите фио: ")
        book_str[0] = fio
    else:
        phone_num = input("Введите номер телефона: ")
        book_str[1] = phone_num
    print(book_str[0], book_str[1])
    book.pop(index)
    book[index] = f'{book_str[0]} | {book_str}'
    print(book)
    
        
    
    # phone_num = input("Введите номер телефона: ")
    # with open('book.txt', 'a', encoding='utf-8') as book:
    #     book.write(f"\n{fio} | {phone_num}")

data = 'фио                     |   номер телефона\n\
        Исаев Владислав Иванович | +814881481848\n\
        Зимник Олег Викторович | +79127557557\n\
        Зимник Ольга Викторовона | +79127557558'
#contakt_to_find = input('Введите ФИО или номер телефона: ')
#print(search(data, contakt_to_find))
#search()
change(data)