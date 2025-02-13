from random import randint
grid = [[" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "]]

place1, place2 = randint(0,4), randint(0,4)
while place1 == 0 or place2 == 0:
    place1, place2 = randint(0,4), randint(0,4)

def show_grid():
    print(grid[0])
    print(grid[1])
    print(grid[2])
    print(grid[3])
    print(grid[4])
    quit()

move_count, player_pos1, player_pos2, grid[place1][place2] = 0, 0, 0, "X"

while move_count != 10:
    move = (input("W, A, S, D\n> ")).lower()
    if move == "w":
        if player_pos1 - 1 > -1 and player_pos1 - 1 < 5:
            player_pos1 -= 1
            move_count += 1
        else: print("Invalid move!")
    elif move == "a":
        if player_pos2 - 1 > -1 and player_pos2 - 1 < 5:
            player_pos2 -= 1
            move_count += 1
        else: print("Invalid move!")
    elif move == "s":
        if player_pos1 + 1 > -1 and player_pos1 + 1 < 5:
            player_pos1 += 1
            move_count += 1
        else: print("Invalid move!")
    elif move == "d":
        if player_pos2 + 1 > -1 and player_pos2 + 1 < 5:
            player_pos2 += 1
            move_count += 1
        else: print("Invalid move!")

    if player_pos1 == place1 and player_pos2 == place2:
        print(f"You WON!\nMove count: {move_count}")
        move_count = 10
        show_grid()

print("You lost! (Ran out of moves D:)")
show_grid()