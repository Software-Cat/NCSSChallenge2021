from enum import Enum
from typing import List
import sys

# Constant definitions
MAZE_PATH = "./week_four/pac_man/maze.txt"
sys.setrecursionlimit(10000)

class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Vector):
            if o.x == self.x and o.y == self.y:
                return True
        return False

    def copy(self):
        return Vector(self.x, self.y)

    def add(self, other: "Vector"):
        newVector: Vector = self.copy()
        newVector.x += other.x
        newVector.y += other.y
        return newVector


class MazeCell(Enum):
    PAC_MAN = "P"
    GHOST = "G"
    WALL = "#"
    PELLET = "."
    SPACE = " "


class Maze:
    def __init__(self, mazeStr: str) -> None:
        # Split input into lines
        mazeLines: List[str] = mazeStr.splitlines()

        # Make empty grid
        self.size: Vector = Vector(len(mazeLines[0]), len(mazeLines))
        self.__grid: List[List[MazeCell]] = [
            [MazeCell.SPACE]*self.size.x for i in range(self.size.y)]

        # Fill grid with correct cells
        for y, line in enumerate(mazeLines):
            for x, char in enumerate(line):
                self.set_cell(Vector(x, y), MazeCell(char))

    def __str__(self) -> str:
        string: str = ""
        for row in self.__grid:
            for cell in row:
                string = string + cell.value
            string = string + "\n"
        return string.rstrip("\n")

    def __repr__(self) -> str:
        return self.__str__()

    def get_cell(self, position: Vector) -> MazeCell:
        return self.__grid[position.y][position.x]

    def set_cell(self, position: Vector, newCell: MazeCell) -> None:
        self.__grid[position.y][position.x] = newCell

    def find_cells_of_type(self, cellType: MazeCell) -> List[Vector]:
        positions: List[Vector] = list()

        for x in range(self.size.x):
            for y in range(self.size.y):
                if self.get_cell(Vector(x, y)) is cellType:
                    positions.append(Vector(x, y))

        return positions

    def tick(self):
        # Get pac man's position
        pacManPos: Vector = maze.find_cells_of_type(MazeCell.PAC_MAN)[0]

        # Move each ghost once
        for ghostPos in maze.find_cells_of_type(MazeCell.GHOST):
            # Set up pathfinder for current ghost
            pathfinder: Pathfinder = Pathfinder(
                maze,
                ghostPos,
                pacManPos
            )

            # Find the path to pac man
            pathfinder.find_path()

            # Update maze
            self.set_cell(ghostPos, MazeCell.SPACE)
            self.set_cell(pathfinder.path[1], MazeCell.GHOST)


class Pathfinder:
    def __init__(self, maze: Maze, initialPosition: Vector, targetPosition: Vector) -> None:
        # Initialize criteria variables
        self.maze = maze
        self.initialPosition = initialPosition
        self.targetPosition = targetPosition

        # Initialize pathfinding variables
        self.path: List[Vector] = None
        self.pathsToSearch: List[List[Vector]] = list()
        self.pathsToSearch.append([self.initialPosition])
        self.seenCells: List[Vector] = list()

    def reset(self):
        self.path = None
        self.pathsToSearch = list()
        self.pathsToSearch.append(list(self.initialPosition))
        self.seenCells = list()

    def find_path(self):
        # Start processing the current path
        currentPath: List[Vector] = self.pathsToSearch[0]
        self.pathsToSearch.remove(currentPath)

        # If the current path reaches the goal, return this path
        if currentPath[len(currentPath)-1] == self.targetPosition:
            self.path = currentPath
            return
        # If the current path leads to a seen cell, ditch this path
        if currentPath[len(currentPath)-1] in self.seenCells:
            self.find_path()
            return

        # Add the last cell to the seen cells
        self.seenCells.append(currentPath[len(currentPath)-1])

        # Check each possible direction
        for direction in [Vector(0, -1), Vector(-1, 0), Vector(0, 1), Vector(1, 0)]:
            # Generate possible next position for each direction
            possibleNextCell: Vector = currentPath[len(
                currentPath)-1].copy().add(direction)

            # Do not add invalid cells
            if self.maze.get_cell(possibleNextCell) == MazeCell.WALL:
                continue
            elif possibleNextCell in self.seenCells:
                continue

            # Add the valid next cell to path
            newPath: List[Vector] = currentPath.copy()
            newPath.append(possibleNextCell)
            self.pathsToSearch.append(newPath)

        self.find_path()


# Load in the maze
maze: Maze
with open(MAZE_PATH) as file:
    maze = Maze(file.read())

# Tick the maze once
maze.tick()

# Print the maze
print(maze)
