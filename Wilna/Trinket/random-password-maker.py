from string import digits, ascii_lowercase, ascii_uppercase
from random import randint

def RandomChar():
    character = ("" + ascii_lowercase[randint(0, 25)] + ascii_uppercase[randint(0, 25)] + digits[randint(0, 9)])
    return character[randint(0, 2)]

def Exists(password, character):
    return True if character in password else False

def Generate():
    password = ""
    character = RandomChar()
    for j in range(2):
        for j in range(4):
            while Exists(password, character):
                character = RandomChar()
            password = password + character
        password = password + "-"
    for j in range(4):
        while Exists(password, character):
            character = RandomChar()
        password = password + character
    
    return password

print(Generate())