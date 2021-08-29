from typing import List, Tuple
import time

START_TIME = time.time()

PAINT_PATH: str = "./week_five/patches_of_paint/patches.txt"

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


def get_next_search_position() -> Tuple[int, int]:
    for position in [(x, y) for x in range(width) for y in range(height)]:
        if grid[position[1]][position[0]] == "%" and not position in searchedPositions:
            return position
    return None


def get_adjacent_positions(currentPosition: Tuple[int, int]) -> List[Tuple[int, int]]:
    adjacentPositions: List[Tuple[int, int]] = []

    for direction in [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]:
        # For each cell, generate new search locations for each direction
        newPosition: Tuple[int, int] = (currentPosition[0] + direction[0],
                                        currentPosition[1] + direction[1])

        if not newPosition in searchedPositions:
            if newPosition[0] >= 0 and newPosition[0] < width and newPosition[1] >= 0 and newPosition[1] < height:
                if grid[newPosition[1]][newPosition[0]] == "%":
                    adjacentPositions.append(newPosition)

    return adjacentPositions


searchedPositions: List[Tuple[int, int]] = []
patches: List[List[Tuple[int, int]]] = []

breaking = False

while not get_next_search_position() is None:
    # While there are still positions not searched, begin new search propagation there
    positionsToSearch: List[Tuple[int, int]] = [get_next_search_position()]
    currentPatch: List[Tuple[int, int]] = [positionsToSearch[0]]
    searchedPositions.append(positionsToSearch[0])

    # While there are still new searches to propagate
    while len(positionsToSearch) > 0:
        # Is overtime, stop early
        if time.time() - START_TIME > 2.49:
            breaking = True
            break

        newPositionsToSearch: List[Tuple[int, int]] = []

        # For each position to search
        for currentPosition in positionsToSearch:
            # Mark it as searched
            searchedPositions.append(currentPosition)
            currentPatch.append(currentPosition)

            # Record new positions to search
            for newPosition in get_adjacent_positions(currentPosition):
                newPositionsToSearch.append(newPosition)

        positionsToSearch = newPositionsToSearch

    if breaking:
        break

    # Add the patch
    patches.append(currentPatch)

# If computating finished normally
if not breaking:
    patchCount: int = len(patches)
    if patchCount == 1:
        print(patchCount, "patch")
    else:
        print(patchCount, "patches")
# If computating stopped early
else:
    print("1 patch")
