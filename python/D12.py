
from collections import defaultdict

DIRS = [[1,0],[0,1],[-1,0],[0,-1]]

class Grid:

    def __init__(self, input):
        self.grid = [line for line in input.strip().splitlines()]
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0])
    def get(self, r, c):
        if 0 <= r < self.num_rows and 0 <= c < self.num_cols:
            return self.grid[r][c]
        else:
            return "#"
        

        
def find_neighbors(r,c,grid):
    fences = 0
    for [rd,cd] in DIRS:
        if grid.get(r+rd,c+cd) == grid.get(r,c):
            yield (r+rd,c+cd)

def part1(input):
    grid = Grid(input)
    visited = set()
    total = 0
    for r in range(0, grid.num_rows):
        for c in range(0, grid.num_cols):
            #if we haven't visited this cell, it's not
            # in a previous plot, so we start a new plot
            if (r,c) not in visited:
                # print(f'---- {grid.get(r,c)} -------')
                queue = [(r,c)]
                fences = 0
                squares = 0
                visited.add((r,c))
                while len(queue) > 0:
                    (row,col) = queue.pop()
                    squares += 1
                    neighbors = list(find_neighbors(row,col,grid))
                    fences += (4 - len(neighbors))
                    new_neighbors = [n for n in neighbors if n not in visited]
                    for n in new_neighbors:
                        queue.append(n)
                        visited.add(n)
                # print(f'fences: {fences}')
                # print(f'squares: {squares}')
                total += fences * squares
                
    return total

with open('../input/D12.txt', 'r') as file:
    input = file.read()

print(f'part 1: {part1(input)}')

ex1 = '''
AAAA
BBCD
BBCC
EEEC
'''

ex2 = '''
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
'''

ex3 = '''
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
'''

assert part1(ex1) == 140
assert part1(ex2) == 772
assert part1(ex3) == 1930
