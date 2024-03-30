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
        number = eg.enterbox("Введите тел. номер контакта:")
        email = eg.enterbox("Введите email контакта (по желанию):")

        contact = {"name": name, "number": number}
        if email:
            contact["email"] = email

        contact_id = generate_id()
        phone_book[str(contact_id)] = contact

        with open('phone_book.json', 'w') as file:
            json.dump(phone_book, file)

        eg.msgbox(f"Контакт {name} успешно добавлен с id: {contact_id}")

    elif choice == "Показать все контакты":
        contacts_info = ""
        for contact_id, contact_info in phone_book.items():
            contacts_info += f"ID: {contact_id}\n"
            contacts_info += f"Имя: {contact_info['name']}\n"
            contacts_info += f"Телефон: {contact_info['number']}\n"
            if 'email' in contact_info:
                contacts_info += f"Email: {contact_info['email']}\n"
            contacts_info += "\n"

        eg.msgbox(contacts_info)

    elif choice == "Найти контакт":
        search_name = eg.enterbox("Введите уникальный идентификатор контакта для поиска:").strip()
        if search_name in phone_book:
            eg.msgbox(f"Номер телефона для контакта {search_name}: {phone_book[search_name]}")
        else:
            eg.msgbox("Контакт не найден.")

    elif choice == "Удалить контакт":
        delete_id = eg.enterbox("Введите уникальный идентификатор контакта для удаления:")
        if delete_id in phone_book:
            del phone_book[delete_id]
            eg.msgbox("Контакт успешно удален.")
        else:
            eg.msgbox("Контакт не найден.")

    elif choice == "Выход":
        with open('phone_book.json', 'w') as file:
            json.dump(phone_book, file)

        break

eg.msgbox("Спасибо за использование телефонной книги!")
