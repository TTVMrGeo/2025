# from math import factorial
# def Factorial(number): return -1 if number < 0 else factorial(number)
# print(Factorial((int(input("Input number you wanna find factorial of\n> ")))))

def Factorial(number):
    answer = number
    for j in range(number):
        if j != 0:
            answer = answer * j
    return -1 if number < 0 else 1 if number == 0 else answer

print(Factorial(5))