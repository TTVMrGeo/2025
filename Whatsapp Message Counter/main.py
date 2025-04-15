from glob import glob

txt_files = glob('Chats/*.txt')

if not txt_files:
    print("No .txt files found in current directory.")
    exit(1)

print("Select a chat to get the message count for:")
for i, file in enumerate(txt_files, 1):
    print(f"{i}. {file[6:]}")

while True:
    try:
        choice = int(input("Enter number: "))
        if 1 <= choice <= len(txt_files):
            file_path = txt_files[choice-1]
            print("")
            break
        else:
            print("Invalid selection. Please try again.")
    except ValueError:
        print("Please enter a number.")

count1 = 0
count2 = 0
users = []
j = 0

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        for j in range(len(line)):
            if line[j] == ":" and line[20:j] not in users and line[20:j] != '':
                users.append(line[20:j])
            if len(users) == 2:
                break

try:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            count1 += line.count(f"{users[0]}:")
            count2 += line.count(f"{users[1]}:")
except FileNotFoundError:
    print(f"The file {file_path} was not found.")

print(f"""Stats for {users[0]} and {users[1]}:\n  {users[0]} {count1}.\n  {users[1]} {count2}.\n\nThe total message count is {count1 + count2}""")