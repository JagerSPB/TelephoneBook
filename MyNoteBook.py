import easygui as eg
import json


try:
    with open('phone_book.json', 'r') as file:
        phone_book = json.load(file)
except FileNotFoundError:
    phone_book = {}

while True:
    choice = eg.buttonbox("Выберите действие:", "Телефонная книга",
                          choices=["Добавить контакт", "Найти контакт", "Показать все контакты", "Выход"])

    if choice == "Добавить контакт":
        name = eg.enterbox("Введите имя контакта:")
        number = eg.enterbox("Введите номер телефона контакта:")
        phone_book[name] = number

    elif choice == "Найти контакт":
        search_name = eg.enterbox("Введите имя контакта для поиска:")
        if search_name in phone_book:
            eg.msgbox(f"Номер телефона для контакта {search_name}: {phone_book[search_name]}")
        else:
            eg.msgbox("Контакт не найден.")

    elif choice == "Показать все контакты":
        if phone_book:
            contacts_info = "\n".join([f"{name}: {phone_book[name]}" for name in phone_book])
            eg.msgbox(contacts_info)
        else:
            eg.msgbox("Телефонная книга пуста.")

    elif choice == "Выход":
        with open('phone_book.json', 'w') as file:
            json.dump(phone_book, file)

        break

eg.msgbox("Спасибо за использование телефонной книги!")