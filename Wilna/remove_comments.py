def deleteComment(line):
    for j in range(len(line)):
        if line[j] == "/" and line[j + 1] == "/":
            return line[:j]
    return line

#! MAIN

file = 'BobBrown_src.txt'
with open(file, 'r', encoding='utf-8') as file:
    for line in file:
        print(deleteComment(line).strip())