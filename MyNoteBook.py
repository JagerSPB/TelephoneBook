import easygui as eg
import json

try:
    with open('phone_book.json', 'r') as file:
        phone_book = json.load(file)
except FileNotFoundError:
    phone_book = {}

def generate_id():
    if not phone_book:
        return 1
    else:
        return max([int(key) for key in phone_book.keys()]) + 1


while True:
    choice = eg.buttonbox("Выберите действие:", "Телефонная книга",
                          choices=["Добавить контакт", "Найти контакт", "Показать все контакты", "Удалить контакт",
                                   "Выход"])

    if choice == "Добавить контакт":
        name = eg.enterbox("Введите имя контакта:")
        number = eg.enterbox("Введите номер контакта:")
        email = eg.enterbox("Введите email контакта (по желанию):")

        contact = {"name": name, "number": number}
        if email:
            contact["email"] = email

        contact_id = generate_id()
        phone_book[str(contact_id)] = contact

        with open('phone_book.json', 'w') as file:
            json.dump(phone_book, file)

        eg.msgbox(f"Контакт {name} успешно добавлен с id: {contact_id}")

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
