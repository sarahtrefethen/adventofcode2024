import math

DIRS = [[1,0], [0,-1], [-1, 0], [0,1]]
[DOWN, RIGHT, UP, LEFT] = DIRS
STARTING_GUARD_TO_DIR = {
    "v": 0,
    "<": 1,
    "^": 2,
    ">": 3
}

class Guard:
    grid: list[list]
    row: int
    col: int
    dir_index: int
    visited: set

    def __init__(self, grid, r, c, arrow):
        self.grid = grid
        self.steps = 0
        self.row = r
        self.col = c
        self.dir_index = STARTING_GUARD_TO_DIR[arrow]
        self.visited = set()

    def step(self):
        # print(f'stepping from {self.row},{self.col}')
        dir = DIRS[self.dir_index]
        [next_r, next_c] = [a+b for (a,b) in zip(dir, [self.row, self.col])]
        if self.is_outside(next_r, next_c):
            return False
        elif grid[next_r][next_c] == "#":
            self.turn()
            return True
        else:
            self.row = next_r
            self.col = next_c
            if (next_r, next_c) not in self.visited:
                self.visited.add((next_r, next_c))
            return True

    def turn(self):   
        # print(f'turning, current visited = {len(self.visited)}')
        self.dir_index = (self.dir_index+1)%len(DIRS)
    
    def is_outside(self, r, c):
        return (r >= len(self.grid) 
                or c >= len(grid[0])
                or c < 0
                or r < 0) 
    
    def get_visited_count(self):
        return len(self.visited)


with open('../input/D06.txt', 'r') as file:
    grid = []
    r=0
    for line in file.readlines():
        grid.append([])
        c=0
        for char in line:
            if char in STARTING_GUARD_TO_DIR:
                start_tuple = (r,c,char)
            grid[r].append(char) 
            c+=1
        r+=1

guard = Guard(grid, *start_tuple)
while (True):
    if not guard.step():
        break
print(f'part 1: {guard.get_visited_count()}')
