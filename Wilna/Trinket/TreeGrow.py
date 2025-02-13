def calculate_speed(name):
    score, name = 0, name.lower()
    for j in range(len([*name])): score += 5 if [*name][j] in [*"aeiou"] else 5 if [*name][j] in [*"bcdfg"] else 2
    return("Slow" if score < 25 else "Medium" if score >= 25 and score <= 35 else "Fast")
print(calculate_speed(input("Tree name\n> "))); score = 0