import json
import random
import string

db = []


def greetings():
    print('==================')
    print('Доступные команды:')
    print('1. Добавить сайт, логин и пароль в базу Менеджера')
    print('2. Добавить сайт, логин и сгенерировать пароль')
    print('3. Изменить пароль (для сайта из базы Менеджера)')
    print('4. Удалить сайт из базы Менеджера')
    print('5. Узнать пароль для сайта')
    print('6. Выйти из программы')
    mode = int(input('Введите номер команды:'))
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
    print(f'{site} успешно добавлен в базу!')


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
    print(f'Ваш новый пароль для сайта {site}: {password}')
    db.append({'site': site, 'login': login, 'password': password})


def change_pass():
    def change(message, prev):
        t = input(f'Введите новый {message}:')
        if t == '':
            return prev
        else:
            return t

    info = input('Введите название сайта: ')
    count = 0
    for i in db:
        if info == i['site']:
            i['login'] = change('логин', i['login'])
            i['password'] = change('пароль', i['password'])
            print(f'Сайт: {i["site"]}')
            print(f'Логин: {i["login"]}')
            print(f'Пароль: {i["password"]}')
            break
        count += 1
    if count == len(db):
        print('Такого сайта нет в базе')


def remove_site():
    info = input('Введите название сайта: ')
    count = 0
    for i in db:
        if info == i['site']:
            db.remove(i)
            print(f'Сайт {info} успешно удален!')
            break
        count += 1
    if count == len(db):
        print('Такого сайта нет в базе')

def search_site():
    info = input('Введите название сайта: ')
    count = 0
    for i in db:
        if info in i["site"]:
            print(f'Ваш логин для входа на сайт {info}: {i["login"]}')
            print(f'Ваш пароль для входа на сайт {info}: {i["password"]}')
            break
        count += 1
    if count == len(db):
        print('Такого сайта нет в базе Менеджера')


db = load_db('user.json')
print('========================================================================')
print('=== Добро пожаловать в Ваш персональный Менеджер паролей для сайтов! ===')
print('========================================================================')
while True:
    mode = greetings()
    if mode == 1:
        add_pass(db)
    elif mode == 2:
        add_and_gen_pass(db)
    elif mode == 3:
        change_pass()
    elif mode == 4:
        remove_site()
    elif mode == 5:
        search_site()
    elif mode == 6:
        break
    else:
        print('Такого режима нет')
    input("Нажмите любую клавишу для продолжения...")

save_db('user.json', db)
