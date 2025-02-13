import string
stringg = (str(input(""))).lower()
split_string, letters, count = [*stringg], [*string.ascii_lowercase], 0

for j in range(len(letters)):
    for i in range(len(split_string)):
        if split_string[i] in letters[j]: count = count + 1
    if count > 0:
        print(f"{letters[j]}: ", "*"*count)
    count = 0