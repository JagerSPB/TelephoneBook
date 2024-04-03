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




def main_menu():
    phone_book = load_phone_book()
    while True:
        choice = eg.choicebox(msg='Выберите действие:',
                              choices=['Добавить контакт', 'Сохранить и выйти'])
        if choice == 'Добавить контакт':
            add_contact(phone_book)
        elif choice == 'Сохранить и выйти':
            save_phone_book(phone_book)
            break


if __name__ == '__main__':
    main_menu()
