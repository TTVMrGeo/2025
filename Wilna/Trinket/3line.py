# def LastLines(file):
#     LineX, LineY, LineZ = "", "", ""
#     for j in range(len(f := (open(file, "r")).readlines())):
#         LineZ, LineY, LineX = LineY, LineX, f[j].removesuffix("\n")
#     return(f"{LineZ}\n{LineY}\n{LineX}")
# print(LastLines("results.txt"))

# def LastLines(file):
#     for j in range(len(f := (open(file, "r")).readlines())): f[j] = f[j].removesuffix("\n")
#     return str(f[len(f)-3:len(f)]).replace("[", "").replace("'", "").replace(",", "").replace("]", "").replace(" ", "\n")
# print(LastLines("results.txt"))

# for j in range(len(f := (open("results.txt", "r")).readlines())): f[j] = f[j].removesuffix("\n")
# print(str(f[len(f)-3:len(f)]).replace("[", "").replace("'", "").replace(",", "").replace("]", "").replace(" ", "\n"))

f = (open("results.txt", "r")).readlines()
print((LineX := f[len(f)-3:len(f)][0]) + (LineY := f[len(f)-3:len(f)][1]) + (LineZ := f[len(f)-3:len(f)][2]))