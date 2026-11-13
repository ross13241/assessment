"""Ross Gallagher
banner ID:B01886848
date: 2/6/2024"""


import random
import string


def validate_password(password):

    if len(password) < 8:
        return False

    has_character = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if has_character and has_number and has_special:
        return True
    else:
        return False


def validate_ip(ip):

    if ip.count(".") != 3:
        return False

    octets = ip.split(".")

    if len(octets) != 4:
        return False

    for number in octets:

        if not number.isdigit():
            return False

        if int(number) < 0 or int(number) > 255:
            return False

    return True


def generate_password():

    length = random.randint(10, 16)

    characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    for i in range(length - 4):
        password.append(random.choice(characters))

    random.shuffle(password)

    return ''.join(password)
