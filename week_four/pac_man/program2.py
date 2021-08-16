from typing import List, Tuple
import sys

# Constant definitions
sys.setrecursionlimit(10000)
MAZE_PATH = "./week_four/pac_man/maze.txt"


def print_maze():
    for row in maze:
        for char in row:
            print(char, end="")
        print()


def find_ghosts(maze: List[List[str]]) -> List[Tuple[int, int]]:
    ghosts: List[Tuple[int, int]] = list()

    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == "G":
                ghosts.append((x, y))

    return ghosts


def find_man(maze: List[List[str]]) -> List[Tuple[int, int]]:
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == "P":
                return (x, y)


def find_path(
        maze: List[List[str]],
        start: Tuple[int, int],
        end: Tuple[int, int]) -> List[Tuple[int, int]]:

    # Initialize
    todo: List[List[Tuple[int, int]]] = list()
    todo.append([start])
    seen: List[Tuple[int, int]] = list()

    # Main loop
    while len(todo) > 0:
        currentPath: List[Tuple[int, int]] = todo.pop(0)

        # Base conditions
        if currentPath[-1] == end:
            return currentPath
        if currentPath[-1] in seen:
            continue

        seen.append(currentPath[-1])

        # Four directions
        for direction in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            possibleNextStep: Tuple[int, int] = (
                currentPath[-1][0] + direction[0],
                currentPath[-1][1] + direction[1],)

            if maze[possibleNextStep[1]][possibleNextStep[0]] == "#":
                continue
            elif possibleNextStep in seen:
                continue

            newPath = currentPath.copy()
            newPath.append(possibleNextStep)
            todo.append(newPath)


# Load maze
maze: List[List[str]] = list()
with open(MAZE_PATH) as file:
    for line in file.readlines():
        line = line.rstrip("\n")
        maze.append([char for char in line])


pacManPos = find_man(maze)
for ghostPos in find_ghosts(maze):
    path = find_path(maze, ghostPos, pacManPos)
    maze[ghostPos[1]][ghostPos[0]] = " "
    maze[path[1][1]][path[1][0]] = "G"

print_maze()
