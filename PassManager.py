import json
import random
import string

db = []


def greetings():
    print()
    print('Добро пожаловать в Ваш персональный Менеджер паролей для сайтов!')
    print()
    print('Возможности Менеджера:')
    print('1. Добавить сайт, логин и пароль в базу Менеджера')
    print('2. Добавить сайт, логин и сгенерировать пароль')
    print('3. Изменить пароль (для сайта из базы Менеджера)')
    print('4. Удалить сайт, логин и пароль из базы Менеджера')
    print('5. Узнать пароль для сайта')
    print('6. Выйти из программы')
    mode = int(input('Что бы вы хотели сделать? (1-6):'))
    return mode


def load_db(filename):
    with open(filename) as file:
        db = json.load(file)
    return db


def save_db(filename, db):
    with open(filename, 'w') as file:
        json.dump(db, file, indent=2)


def add_pass(db):
    site = input('Введите название сайта: ')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    db.append({'site': site, 'login': login, 'password': password})


def add_and_gen_pass(db):
    def compare(first_string, second_string):
        first_string = set(first_string)
        second_string = set(second_string)
        result = first_string.intersection(second_string)
        return len(result) > 0

    def generate_pass(len_password):
        while True:
            result = ''
            for i in range(len_password):
                result += random.choice(string.digits + string.ascii_letters)
            if compare(result, string.ascii_lowercase) and compare(result, string.ascii_uppercase) and compare(result,
                                                                                                               string.digits):
                return result

    site = input('Введите название сайта: ')
    login = input('Введите логин: ')
    len_pass = int(input('Введите длину пароля: '))
    password = generate_pass(len_pass)
    db.append({'site': site, 'login': login, 'password': password})


def change_pass():
    def change(subject, prev):
        t = input(f'Введите {subject} ({prev}):')
        if t == '':
            return prev
        else:
            return t

    while True:
        info = input('Введите название сайта: ')
        for i in db:
            if i in db:
                info['site'] = change('название сайта', info['site'])
                info['login'] = change('Ваш логин', info['login'])
                info['password'] = change('Новый пароль', info['password'])
                greetings()
                break
            else:
                print('Такого сайта нет в базе')
                greetings()
                break


def search_site():
    site = input('Введите название сайта: ')
    for i in db:
        if site in i["site"]:
            print(f'Ваш логин для входа на сайт {site}: {i["login"]}')
            print(f'Ваш пароль для входа на сайт {site}: {i["password"]}')
        else:
            print('Данного сайта нет в базе')


def loop(filename):
    db = load_db(filename)
    while True:
        mode = greetings()
        if mode == 1:
            add_pass(db)
        elif mode == 2:
            add_and_gen_pass(db)
        elif mode == 3:
            change_pass()
        elif mode == 5:
            search_site()
        elif mode == 6:
            break
        else:
            print('Такого режима нет')
    save_db(filename, db)


loop('user.json')
