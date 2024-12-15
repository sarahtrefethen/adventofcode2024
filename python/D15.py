

ARROW_DIR_MAP = {
    ">": [0, 1],
    "<": [0, -1],
    "^": [-1, 0],
    "v": [1, 0],
}

BOX = "O"
WALL = "#"
OPEN_SPACE = '.'
ROBOT = '@'

def next(coordinates, arrow):
        return [a+b for (a,b) in zip(coordinates, ARROW_DIR_MAP[arrow])]

class Grid:
    def __init__(self, input):
        self.grid = [[char for char in line] for line in input.strip().splitlines()]
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0])
        for r in range(0, self.num_rows):
            for c in range(0, self.num_cols):
                if self.grid[r][c] == ROBOT:
                    self.robot = (r,c)
                    break
    
    def get(self, r, c):
        if 0 <= r < self.num_rows and 0 <= c < self.num_cols:
            return self.grid[r][c]
        else:
            return ""
    def set(self, r, c, sym):
        self.grid[r][c] = sym
        
    def move_robot(self, arrow):
        [next_r, next_c] = next(self.robot, arrow)
        # print(f' next is {next_r}, {next_c}')
        next_sym = self.grid[next_r][next_c]
        if  next_sym == WALL:
            # print('hit a wall')
            return
        elif next_sym == OPEN_SPACE:
            # print("moving to open space")
            self.set(next_r,next_c,ROBOT)
            self.set(*self.robot, OPEN_SPACE)
            self.robot = (next_r, next_c)
            return
        elif next_sym == BOX:
            end_of_line=[next_r, next_c]
            while self.get(*end_of_line) == BOX:
                end_of_line = next(end_of_line, arrow)
            # print(f'end of line {end_of_line}')
            if self.get(*end_of_line) == WALL:
                return
            elif self.get(*end_of_line) == OPEN_SPACE:
                # print("found some boxes that need to be moved into open space")
                # print(f'({next_r}, {next_c}) to {end_of_line}')
                self.set(*end_of_line, BOX)
                self.set(next_r, next_c, ROBOT)
                self.set(*self.robot, OPEN_SPACE)
                self.robot= (next_r, next_c)
    
    def get_all_box_gps(self):
        total = 0
        for r in range(0, self.num_rows):
            for c in range(0, self.num_cols):
                if self.grid[r][c] == BOX:
                    total += 100*r + c
        return total
    
    def print(self):
        for row in self.grid:
            print(row)        

def part1(input):
    [g, moves] = input.strip().split('\n\n')
    grid = Grid(g)
    # grid.print()
    for dir in moves:
        if dir == '\n':
            continue
        # print(f'attempting to move {dir}')
        grid.move_robot(dir)
        # grid.print()
    return grid.get_all_box_gps()


ex1= '''
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
'''

ex2='''
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''

assert part1(ex1)==2028
assert part1(ex2)==10092

with open('../input/D15.txt', 'r') as file:
    input = file.read()

print(f'part 1: {part1(input)}')