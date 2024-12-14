
import math


def wrap(val, boundary):
    if val < 0:
        return boundary + val
    elif val >= boundary:
        return val % boundary
    return val

class Robot:
    def __init__(self, start, direction):
        self.current = start
        self.direction = direction
    
    def print(self):
        print(f'robot at {self.current}, headed in {self.direction}')
    
    def tick(self, height, width):
        [next_x, next_y] = [a+b for (a,b) in zip(self.current, self.direction)]
        self.current = [wrap(next_x,width), wrap(next_y, height)]

class Room:
    def __init__(self, robots, width, height):
        self.width = width
        self.height = height
        self.robots = robots
        self.ticks = 0

    def tick(self):
        self.ticks += 1
        for robot in self.robots:
            robot.tick(self.height, self.width)

    def print(self):
        for robot in self.robots:
            robot.print()


    def score(self):
        grid = [[0 for i in range(0,self.width)] for n in range(0, self.height)]
        ul = ur = ll = lr = 0
        i = 0
        y_middle_row = math.floor(self.height/2)
        x_middle_col = math.floor(self.width/2)
        for y in range(0, self.height):
            for x in range(0, self.width):
                if y == y_middle_row or x == x_middle_col:
                    grid[y][x]='*'
        for row in grid:
            print(row)
        for robot in self.robots:
            self.robots[i].print()
            i +=1
            [x,y] = robot.current
            if x > x_middle_col:
                if y > y_middle_row:
                    lr+=1
                    grid[y][x] += 1

                elif y < y_middle_row:
                    ll+=1
                    grid[y][x] += 1
                # else:
                    # print("skipped")
            elif x < x_middle_col:
                if y > y_middle_row:
                    ur+=1
                    grid[y][x] += 1
                elif y < y_middle_row:
                    ul+=1
                    grid[y][x] += 1
                # else:
                    # print("skipped")
        for row in grid:
            print(row)
        print(f'{ul}, {ur}, {ll}, {lr}')
        return ul*ur*ll*lr
    
def part1(input, width, height):
    data = [[[int(char) 
            for char in substring.split("=")[1].split(",")]
            for substring in line.split(" ")] 
            for line in input.strip().splitlines()]
    room = Room([Robot(s,d) for [s,d] in data], width=width, height=height)
    for i in range(0,100):
        room.tick()
    return room.score()

assert part1('''
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
             ''', width=11, height=7) == 12

with open('../input/D14.txt', 'r') as file:
    input = file.read()

print(f'part1: {part1(input, width=101, height=103)}')