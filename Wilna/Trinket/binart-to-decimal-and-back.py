def b_to_d(binary_o):
    binary = list(binary_o[::-1])
    a = 0
    b = 1
    ans = 0

    for binar in binary:
        if binary[a] == "1":
            ans += b
            a += 1
            b *= 2
            
        elif binary[a] == "0":
            ans += 0
            a += 1
            b *= 2
            
    print(f"{binary_o} in decimal is: {ans}")

def d_to_b(n):
    n = int(n)
    a = 128
    ans = []
    while a > 0:
        if n >= a:
            ans.append(1)
            n -= a
        else:
            ans.append(0)
        a = a // 2
    print(str(ans).replace('[','').replace(']','').replace(',','').replace(' ',''))
            

choice = input("Do you want to\n1. Convert from binary to decimal\n2. Convert from decimal to binary (max 255)\n> ")

if int(choice) == 1:
    b_to_d(input("Binary number\n> "))
elif int(choice) == 2:
    d_to_b(input("Decimal number\n> "))
else:
    print("Invalid input!")