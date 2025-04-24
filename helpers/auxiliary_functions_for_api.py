import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_email_password_name():
    email = f'{generate_random_string(6)}@yandex.ru'
    password = generate_random_string(8)
    name = generate_random_string(8)
    return [email, password, name]

def choice_random_sauce():
    sauce = ['Соус Spicy-X',
    'Соус фирменный Space Sauce',
    'Соус традиционный галактический',
    'Соус с шипами Антарианского плоскоходца'
]
    return random.choice(sauce)
