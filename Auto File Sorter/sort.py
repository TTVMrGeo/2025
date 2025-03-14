import os

files_to_sort = os.listdir("Sort")
files = []

for j in os.listdir():
    if j[0] == "A":
        files.append(j)
    elif j == "Sort" or j == "File Sorter.exe" or j == "sort.py":
        pass
    else:
        os.system(f"msg * Folder {j} not named right. Family code has to start with A! (E.g. A001{j[4:]})")

for j in range(len(files_to_sort)):
    for i in range(len(files)):
        if files[i][0:4] == files_to_sort[j][0:4]:
            os.rename(f"Sort/{files_to_sort[j]}", f"{files[i]}/{files_to_sort[j]}")

for j in os.listdir("Sort"):
    os.system(f"msg * No Folder with the family code {j[0:4]}")