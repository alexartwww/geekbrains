task = '''
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
'''


def print_user_info(name, last_name, year_of_birth, city_of_living, email, phone):
    print(f"Name: {name}\nLast name: {last_name}\nYear of birth: {year_of_birth}\nCity of living: {city_of_living}\nEmail: {email}\nPhone: {phone}")


if __name__ == '__main__':
    print(task)
    print_user_info(name='Artem',
                    last_name='Alekashkin',
                    year_of_birth=1986,
                    city_of_living='Moscow',
                    email='artem@aleksashkin.com',
                    phone='+79991234567')
