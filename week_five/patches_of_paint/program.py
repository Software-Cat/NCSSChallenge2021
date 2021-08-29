from enum import Enum
from typing import List, Set

PAINT_PATH: str = "./week_five/patches_of_paint/patches.txt"


class CellType(Enum):
    PAINT = "%"
    GROUND = "."


class Vector(tuple):
    def __new__(cls, x, y):
        return super(Vector, cls).__new__(cls, tuple((x, y)))

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y


class Direction(Enum):
    UP = Vector(0, -1)
    UP_RIGHT = Vector(1, -1)
    RIGHT = Vector(1, 0)
    DOWN_RIGHT = Vector(1, 1)
    DOWN = Vector(0, 1)
    DOWN_LEFT = Vector(-1, 1)
    LEFT = Vector(-1, 0)
    UP_LEFT = Vector(-1, -1)


class PaintGrid:

    def __init__(self, paintFile: str) -> None:
        self.width: int = 0
        self.height: int = 0

        # Calculate width and height of grid
        for line in paintFile.rstrip("\n").splitlines():
            self.width = max(self.width, len(line))
            self.height += 1

        # Initialize grid with all ground
        self.__grid: List[List[CellType]] = \
            [[CellType.GROUND for x in range(self.width)]
             for y in range(self.height)]

        # Fill grid according to paint file
        for y, line in enumerate(paintFile.splitlines()):
            for x, char in enumerate(line):
                self.__grid[y][x] = CellType(char)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        string: str = ""

        for row in self.__grid:
            for cell in row:
                string += cell.value
            string += "\n"

        return string.rstrip("\n")

    def get_cell(self, position: Vector) -> CellType:
        """Gets the cell at a certain position

        Args:
            position (Vector): x axis increases to the right,
            y axis increases to the bottom,
            origin at top left corner

        Returns:
            CellType: The type of the cell
        """
        return self.__grid[position.y][position.x]

    def is_valid(self, position: Vector) -> bool:
        if position.x < 0 or position.y < 0:
            return False
        if position.x >= self.width or position.y >= self.height:
            return False
        return True

    def is_of_type(self, position: Vector, cellType: CellType) -> bool:
        return self.get_cell(position) == cellType

    def count_patches(self, propagationLimit: int) -> int:
        patches: List[Set[Vector]] = []

        # Initialize position seeds
        for position in [Vector(x, y) for x in range(self.width) for y in range(self.height)]:
            if self.is_of_type(position, CellType.PAINT):
                patches.append(set([position]))

        # Grow the position seeds
        for i in range(propagationLimit):
            for patch in patches:
                itemsToAdd: List[Vector] = []

                for position in patch:
                    for direction in Direction:
                        # For each cell, generate new search locations for each direction
                        newPos: Vector = position + direction.value

                        # If the cell is a new paint cell, add it
                        if (self.is_valid(newPos)) and (not newPos in patch) and (self.is_of_type(newPos, CellType.PAINT)):
                            itemsToAdd.append(newPos)

                for item in itemsToAdd:
                    patch.add(item)

        # Remvoe duplicates
        uniquePatches: List[Set[Vector]] = []
        for patch in patches:
            if not patch in uniquePatches:
                uniquePatches.append(patch)

        return len(uniquePatches)


# Generate the paint grid
with open(PAINT_PATH, "r") as file:
    myGrid = PaintGrid(file.read())

patchCount = myGrid.count_patches(100)
if patchCount == 1:
    print(patchCount, "patch")
else:
    print(patchCount, "patches")
