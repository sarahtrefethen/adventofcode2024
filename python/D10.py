
DIRS = [[1,0], [0,1], [-1,0], [0,-1]]

class Grid:
    def __init__(self, input):
        self.grid = [[int(c) for c in line] for line in input.strip().splitlines()]
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0])
        self.trail_count = 0
    def get(self, r, c):
        if r >=0 and c >=0 and r < self.num_rows and c < self.num_cols:
            return(self.grid[r][c])
        else:
            return -1                


class TrailHead:
    def __init__(self, r,c):
        self.start=(r,c)
        self.search_queue = [(r,c,0)]
        self.peaks_reached = set()
        self.rating = 0
    def find_trails(self, grid):
        while(len(self.search_queue) > 0):
            (r,c,h) = self.search_queue.pop()
            for [rd, cd] in DIRS:
                if grid.get(r+rd, c+cd) == h+1:
                    if h+1 == 9:
                        self.peaks_reached.add((r+rd, c+cd))
                        self.rating += 1
                    else:
                        self.search_queue.append((r+rd, c+cd, h+1))
    def get_score(self):
        return len(self.peaks_reached)
    def get_rating(self):
        return self.rating


def make_trailheads(input):
    grid = Grid(input)
    trailheads = []
    for r in range(0, grid.num_rows):
        for c in range(0, grid.num_cols):
            if grid.get(r,c) == 0:
                trailheads.append(TrailHead(r,c))

    for th in trailheads:
        th.find_trails(grid)

    return trailheads

def part1(input):
    trailheads = make_trailheads(input)
    return sum([th.get_score() for th in trailheads])

def part2(input):
    trailheads = make_trailheads(input)
    return sum([th.get_rating() for th in trailheads])

with open('../input/D10.txt', 'r') as file:
    input = file.read()

print(f'part 1: {part1(input)}')
print(f'part 2: {part2(input)}')

# test cases
assert part1('''
0123
1234
8765
9876
''') == 1

assert part1('''
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
''')==36

assert part2('''
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
''')==81