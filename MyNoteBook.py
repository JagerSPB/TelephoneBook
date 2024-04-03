import easygui as eg
import json


def load_phone_book(filename='phone_book.json'):
    try:
        with open(filename, 'r') as file:
            phone_book = json.load(file)
    except FileNotFoundError:
        phone_book = {}
    return phone_book


def save_phone_book(phone_book, filename='phone_book.json'):
    with open(filename, 'w') as file:
        json.dump(phone_book, file, indent=4)


def add_contact(phone_book):
    name = eg.enterbox(msg='Введите имя контакта:')
    number = eg.enterbox(msg='Введите номер телефона контакта:')
    email = eg.enterbox(msg='Введите email контакта (если есть):')
    contact_id = str(max([int(x) for x in phone_book.keys()] + [0]) + 1)
    phone_book[contact_id] = {'name': name, 'number': number, 'email': email}


def list_contacts(phone_book):
    message = '\n'.join([
        f'ID: {contact_id}, Имя: {details["name"]}, Телефон: {details["number"]}, Email: {details.get("email", "Не указан")}'
        for contact_id, details in phone_book.items()])
    eg.msgbox(msg=message, title='Список контактов')


def main_menu():
    phone_book = load_phone_book()
    while True:
        choice = eg.choicebox(msg='Выберите действие:',
                              choices=['Добавить контакт', 'Показать контакты', 'Сохранить и выйти'])
        if choice == 'Добавить контакт':
            add_contact(phone_book)
        elif choice == 'Показать контакты':
            list_contacts(phone_book)
        elif choice == 'Сохранить и выйти':
            save_phone_book(phone_book)
            break


if __name__ == '__main__':
    main_menu()
