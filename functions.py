def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('template_for_homework8\\book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    with open('template_for_homework8\\book.txt', 'r', encoding='utf-8') as book:
        book_file = book.read()
    num = len(book_file.split("\n"))
    with open('template_for_homework8\\book.txt', 'a', encoding='utf-8') as book:
        fio = input('Введите ФИО: ')
        phone_num = input('Введите номер телефона: ')
        book.write(f"{num} | {fio} | {phone_num}\n")
        print(f"Добавлена запись : {num} | {fio} | {phone_num}\n")


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))


def edit_data() -> None:
    """Выводит список контактов и изменяет выбранную строку"""
    print("\nПП | ФИО | Телефон")
    with open('template_for_homework8\\book.txt', "r", encoding='utf-8') as book:
        tel_book = book.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки\n"
                                  " для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} | {fio} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open('template_for_homework8\\book.txt', "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))


def delete_data() -> None:
    """Выводит список контактов и удаляет выбранную строку"""
    print("\nПП | ФИО | Телефон")
    with open('template_for_homework8\\book.txt', "r", encoding="utf-8") as book:
        tel_book = book.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open('template_for_homework8\\book.txt', "w", encoding='utf-8') as book:
        book.write("\n".join(tel_book_lines))
