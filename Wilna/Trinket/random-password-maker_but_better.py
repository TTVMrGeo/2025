from string import digits, ascii_lowercase, ascii_uppercase
from random import randint

def section_maker():
    password = ""
    for j in range(4):
        character = ("" + ascii_lowercase[randint(0, 25)] + ascii_uppercase[randint(0, 25)] + digits[randint(0, 9)])
        if character not in password:
            password = password + character[randint(0, 2)]
    return password

def password_maker():
    final = f"{section_maker()}-{section_maker()}-{section_maker()}"
    return final

print(password_maker())