import math
DIRS = [E, S, W, N] = [[0,1], [1,0], [0, -1], [-1,0]]

END = "E"
START = "S"
OPEN = "."
WALL = "#"

def turn_left(dir_index):
    return (dir_index-1) % 4

def turn_right(dir_index):
    return (dir_index+1) % 4

def move_one(r,c,dir_index):
    return [a+b for (a,b) in zip([r,c], DIRS[dir_index])]


class Maze:
    def __init__(self, input):
        self.grid = [[char for char in line] for line in input.strip().splitlines()]
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0])
        for r in range(0, self.num_rows):
            for c in range(0, self.num_cols):
                if self.grid[r][c] == START:
                    self.start = (r,c)
                elif self.grid[r][c] == END:
                    self.end = (r,c)

    def get(self, coords):
        [r,c] = coords
        if 0 <= r < self.num_rows and 0 <= c < self.num_cols:
            return self.grid[r][c]
        else:
            return ""



def part1(input):
    maze = Maze(input)
    queue = [(*maze.start, 0, 0)]
    solutions = []
    min_score_to_get_to = {maze.start: 0}
    while len(queue) > 0:
        (r,c,dir_index, score) = queue.pop(0)
        forward = move_one(r,c,dir_index)
        left = move_one(r,c,turn_left(dir_index))
        right = move_one(r,c,turn_right(dir_index))
        if maze.get(forward) == END:
            solutions.append(score + 1)
        if maze.get(left) == END or maze.get(right) == END:
            solutions.append(score + 1000)
        
        if maze.get(forward) == OPEN:
            [fr, fc] = forward
            if min_score_to_get_to.get((fr,fc), math.inf) > score+1:
                min_score_to_get_to[(fr,fc)] = score+1
                queue.append((fr, fc, dir_index, score+1))
        if maze.get(left) == OPEN:
            if min_score_to_get_to.get((left[0],left[1]), math.inf) > score+1001:
                min_score_to_get_to[(left[0],left[1])] = score+1001
                queue.append((*left, turn_left(dir_index), score+1001))
        if maze.get(right) == OPEN:
            [rr, rc] = right
            if min_score_to_get_to.get((rr,rc), math.inf) > score+1001:
                min_score_to_get_to[(rr,rc)] = score+1001
                queue.append((rr, rc, turn_right(dir_index), score+1001))
    print(solutions)
    return min(solutions)


example = '''
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
'''

assert part1(example) == 7036

with open('../input/D16.txt', 'r') as file:
    test_input=file.read()

print(f'part 1: {part1(test_input)}')