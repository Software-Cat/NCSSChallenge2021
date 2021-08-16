GRID_SIZE = int(input("Size: "))
MAX_RECUR_DEPTH = int(input("Moves: "))
INITIAL_POS = tuple([int(n) for n in input("Knight: ").split(",")])

grid = [["." for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]


def propagate_move(pos, depth):
    if depth > MAX_RECUR_DEPTH:
        return

    for deltaPos in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
        if (pos[0] + deltaPos[0] >= 0 and pos[0] + deltaPos[0] < GRID_SIZE and pos[1] + deltaPos[1] >= 0 and pos[1] + deltaPos[1] < GRID_SIZE):
            if grid[pos[0] + deltaPos[0]][pos[1] + deltaPos[1]] == "." or int(grid[pos[0] + deltaPos[0]][pos[1] + deltaPos[1]]) > depth:
                grid[pos[0] + deltaPos[0]][pos[1] + deltaPos[1]] = str(depth)
                propagate_move(
                    (pos[0] + deltaPos[0], pos[1] + deltaPos[1]), depth + 1)


grid[INITIAL_POS[0]][INITIAL_POS[1]] = "0"
propagate_move(INITIAL_POS, 1)

for row in grid:
    print(" ".join(row))
