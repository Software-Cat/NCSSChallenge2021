class Tile:
    def __init__(self, parent):
        self.parent = parent

    def __str__(self):
        """ Interface for converting to string """
        return ""

    def get_pos(self):
        return self.parent.get_pos(self)

    def get_state(self):
        """ Interface for getting state of tile

        Can be in 3 states: [
            UNHAPPY: Broken a rule
            HAPPY: No rules broken but clear condition not satisfied
            SOLVED: All conditions satisfied
        ]

        """
        return "SOLVED"


class Light(Tile):
    def __init__(self, parent):
        Tile.__init__(self, parent)

    def __str__(self):
        return "L"

    def get_state(self):
        for tile in self.parent.get_wasd(self):
            if isinstance(tile, Light):
                return "UNHAPPY"
        return "SOLVED"


class Block(Tile):
    def __str__(self):
        return "X"


class NumberBlock(Tile):
    def __init__(self, parent, number):
        Tile.__init__(self, parent)
        self.number = number

    def __str__(self):
        return str(self.number)

    def get_state(self):
        lightCount = 0

        for tile in self.parent.get_adjacent(self):
            if isinstance(tile, Light):
                lightCount += 1

        if lightCount > self.number:
            return "UNHAPPY"
        elif lightCount < self.number:
            return "HAPPY"
        else:
            return "SOLVED"


class Space(Tile):
    def __init__(self, parent, lit):
        Tile.__init__(self, parent)
        self.lit = lit

    def __str__(self):
        if self.lit:
            return "o"
        return "."

    def get_state(self):
        if self.lit:
            return "SOLVED"
        return "HAPPY"


class Board:
    def __init__(self, board):
        self.n = len(board[0])
        self.grid = [[None for j in range(self.n)] for i in range(self.n)]

        for y, row in enumerate(board):
            for x, tile in enumerate(row):
                if tile == ".":
                    self.grid[y][x] = Space(self, False)
                elif tile == "L":
                    self.grid[y][x] = Light(self)
                elif tile == "X":
                    self.grid[y][x] = Block(self)
                else:
                    self.grid[y][x] = NumberBlock(self, int(tile))

    def __str__(self):
        return "\n".join(["".join([str(tile) for tile in self.grid[y]]) for y in range(len(self.grid))])

    def get_pos(self, tile):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == tile:
                    return (x, y)
        raise IndexError("Could not find tile " + str(tile))

    def get_tile(self, pos):
        return self.grid[pos[1]][pos[0]]

    def get_wasd(self, tile):
        tiles = []

        currentPos = list(tile.get_pos())
        currentTile = None
        while currentPos[0] > 0:
            currentPos[0] -= 1
            currentTile = self.get_tile(currentPos)
            if isinstance(currentTile, Block) or isinstance(currentTile, NumberBlock):
                break
            tiles.append(currentTile)

        currentPos = list(tile.get_pos())
        currentTile = None
        while currentPos[0] < self.n - 1:
            currentPos[0] += 1
            currentTile = self.get_tile(currentPos)
            if isinstance(currentTile, Block) or isinstance(currentTile, NumberBlock):
                break
            tiles.append(currentTile)

        currentPos = list(tile.get_pos())
        currentTile = None
        while currentPos[1] > 0:
            currentPos[1] -= 1
            currentTile = self.get_tile(currentPos)
            if isinstance(currentTile, Block) or isinstance(currentTile, NumberBlock):
                break
            tiles.append(currentTile)

        currentPos = list(tile.get_pos())
        currentTile = None
        while currentPos[1] < self.n - 1:
            currentPos[1] += 1
            currentTile = self.get_tile(currentPos)
            if isinstance(currentTile, Block) or isinstance(currentTile, NumberBlock):
                break
            tiles.append(currentTile)

        return tiles

    def get_adjacent(self, tile):
        tiles = []

        tilePos = tile.get_pos()

        if tilePos[0] - 1 >= 0:
            tiles.append(self.get_tile((tilePos[0] - 1, tilePos[1])))
        if tilePos[0] + 1 < self.n:
            tiles.append(self.get_tile((tilePos[0] + 1, tilePos[1])))
        if tilePos[1] - 1 >= 0:
            tiles.append(self.get_tile((tilePos[0], tilePos[1] - 1)))
        if tilePos[1] + 1 < self.n:
            tiles.append(self.get_tile((tilePos[0], tilePos[1] + 1)))

        return tiles

    def update(self):
        for row in self.grid:
            for tile in row:
                if isinstance(tile, Light):
                    for space in self.get_wasd(tile):
                        if isinstance(space, Space):
                            space.lit = True

    def is_happy(self):
        tileStates = []
        for row in self.grid:
            for tile in row:
                tileStates.append(tile.get_state())

        return not "UNHAPPY" in tileStates

    def is_solved(self):
        tileStates = []
        for row in self.grid:
            for tile in row:
                tileStates.append(tile.get_state())

        return not ("UNHAPPY" in tileStates or "HAPPY" in tileStates)


def get_board_state(board):
    game = Board(board)
    game.update()
    if game.is_happy():
        if game.is_solved():
            return "solved"
        else:
            return "happy"
    else:
        return "unhappy"


if __name__ == '__main__':
    # Example board, happy state.
    print(get_board_state('''
...1.0.
X......
..X.X..
X...L.X
..X.3..
.L....X
L3L2...'''.strip().split('\n')))
    # Example board, solved state.
    print(get_board_state('''
..L1.0.
X...L..
L.X.X.L
X...L.X
..XL3L.
.L....X
L3L2L..'''.strip().split('\n')))
    # Example board, unhappy state.
    print(get_board_state('''
L..1L0.
X.L....
L.X.X.L
X...L.X
..XL3L.
.L....X
L3L2L..'''.strip().split('\n')))
    # Different board, happy state.
    print(get_board_state('''
L1.L.
..L3L
..X1.
.1...
.....'''.strip().split('\n')))
