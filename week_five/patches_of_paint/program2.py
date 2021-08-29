from typing import List, Set, Tuple


PAINT_PATH: str = "./week_five/patches_of_paint/patches.txt"
PROPAGATION_LIMIT = 100

width: int = 0
height: int = 0
grid: List[List[str]] = []

with open(PAINT_PATH, "r") as file:
    # Calculate width and height of grid
    for line in file.read().rstrip("\n").splitlines():
        width = max(width, len(line))
        height += 1

    # Initialize grid with all ground
    grid = [["%" for x in range(width)] for y in range(height)]


with open(PAINT_PATH, "r") as file:
    # Fill grid according to paint file
    for y, line in enumerate(file.read().rstrip("\n").splitlines()):
        for x, char in enumerate(line):
            grid[y][x] = char

patches: List[Set[Tuple[int, int]]] = []

# Initialize position seeds
for position in [(x, y) for x in range(width) for y in range(height)]:
    if grid[position[1]][position[0]] == "%":
        patches.append(set([position]))

# Grow the position seeds
for i in range(PROPAGATION_LIMIT):
    for patch in patches:
        itemsToAdd: List[Tuple[int, int]] = []

        for position in patch:
            for direction in [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]:
                # For each cell, generate new search locations for each direction
                newPos: Tuple[int, int] = (
                    position[0] + direction[0], position[1] + direction[1])

                # If the cell is a new paint cell, add it
                if not newPos in patch:
                    if newPos[0] >= 0 and newPos[0] < width and newPos[1] >= 0 and newPos[1] < height:
                        if grid[newPos[1]][newPos[0]] == "%":
                            itemsToAdd.append(newPos)

        for item in itemsToAdd:
            patch.add(item)

# Remvoe duplicates
uniquePatches: List[Set[Tuple[int, int]]] = []
for patch in patches:
    if not patch in uniquePatches:
        uniquePatches.append(patch)

patchCount = len(uniquePatches)
if patchCount == 1:
    print(patchCount, "patch")
else:
    print(patchCount, "patches")
