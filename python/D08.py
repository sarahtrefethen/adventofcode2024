from collections import defaultdict


class Grid:
    def __init__(self, input):
        self.grid = [line for line in input.strip().splitlines()]
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0])
        self.antennas = defaultdict(lambda: [])
        for r in range(0, self.num_rows):
            for c in range(0, self.num_cols):
                if self.grid[r][c] != ".":
                    self.antennas[self.grid[r][c]].append((r,c))
        print(self.antennas)

    def get_frequencies(self):
        return list(self.antennas.keys())
    
    # for part 1
    def get_antinodes(self, f):
        sources = self.antennas[f]
        antinodes = []
        for a in range(0, len(sources)-1):  
            (ra, ca) = sources[a]
            for b in range(a+1, len(sources)):
                (rb, cb) = sources[b]
                print(f'calcuating antinodes generated by ({ra}, {ca}) and ({rb}, {cb})')
                rd = ra - rb
                cd = ca - cb
                for [r,c] in [[ra+rd, ca+cd], [rb-rd, cb-cd]]:
                    if 0 <= r < self.num_rows and 0 <= c < self.num_cols:
                        antinodes.append((r,c))
        return antinodes
    
    # for part 2
    def gen_resonant_antinodes(self, f):
        sources = self.antennas[f]
        antinodes = []
        for a in range(0, len(sources)-1):  
            (ra, ca) = sources[a]
            for b in range(a+1, len(sources)):
                (rb, cb) = sources[b]
                print(f'calcuating antinodes generated by ({ra}, {ca}) and ({rb}, {cb})')
                rd = ra - rb
                cd = ca - cb

                r = ra
                c= ca    
                while 0 <= r < self.num_rows and 0 <= c < self.num_cols:
                    yield (r,c)
                    r += rd
                    c += cd
                r = rb
                c= cb   
                while 0 <= r < self.num_rows and 0 <= c < self.num_cols:
                    yield (r,c)
                    r -= rd
                    c -= cd


def part1(input):

    grid = Grid(input)
    all_antinodes = []
    for f in grid.get_frequencies():
        all_antinodes.extend(grid.get_antinodes(f))

    return len(set(all_antinodes))

def part2(input):

    grid = Grid(input)
    all_antinodes = []
    for f in grid.get_frequencies():
        all_antinodes.extend(grid.gen_resonant_antinodes(f))

    return len(set(all_antinodes))

example = '''
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
             '''
assert part1(example) == 14
assert part2(example) == 34

with open("../input/D08.txt", "r") as file:
    input = file.read()

print(f'part1: {part1(input)}')
print(f'part2: {part2(input)}')