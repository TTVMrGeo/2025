from string import ascii_lowercase
max_count, split_string, letters, count, maxes, index = 0, [*(str(input(""))).lower()], [*ascii_lowercase], 0, [], 0

for j in range(len(letters)):
    for i in range(len(split_string)):
        if split_string[i] in letters[j]: count = count + 1
    if count >= max_count:
        maxes.append([])
        max_count = count
        maxes[index].append(split_string[index])
        maxes[index].append(count)
        index += 1
    count = 0

print("Character(s) that appeared the most:")
for j in range(len(maxes)):
    if maxes[j][1] == max_count: print(f"{maxes[j][0]} : {max_count}")