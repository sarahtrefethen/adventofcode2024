with open('../input/D04.txt', 'r') as file:
    grid = [[char for char in line] for line in file.read().splitlines()]

def scan_left(grid,x,y):
    try:
        return grid[x][y-1]+grid[x][y-2]+grid[x][y-3] == 'MAS'
    except:
        return False

def scan_right(grid,x,y):
    try:
        return grid[x][y+1]+grid[x][y+2]+grid[x][y+3] == 'MAS'
    except:
        return False
def scan_up(grid,x,y):
    try:
        return x >= 3 and grid[x-1][y]+grid[x-2][y]+grid[x-3][y] == 'MAS'
    except:
        return False
def scan_down(grid,x,y):
    try:
        return grid[x+1][y]+grid[x+2][y]+grid[x+3][y] == 'MAS'
    except:
        return False   
def scan_ul(grid,x,y):
    try:
        return x >= 3 and y >= 3 and grid[x-1][y-1]+grid[x-2][y-2]+grid[x-3][y-3] == 'MAS'
    except:
        return False
def scan_ur(grid,x,y):
    try: 
        return x >= 3 and grid[x-1][y+1]+grid[x-2][y+2]+grid[x-3][y+3] == 'MAS'
    except:
        return False
def scan_dr(grid,x,y):
    try:
        return grid[x+1][y+1]+grid[x+2][y+2]+grid[x+3][y+3] == 'MAS'
    except:
        return False
def scan_dl(grid,x,y):
    try:
        return y >= 3 and grid[x+1][y-1]+grid[x+2][y-2]+grid[x+3][y-3] == 'MAS'
    except:
        return False
    
max_x = len(grid)
max_y = len(grid[0])
count = 0
for x in range(0, max_x):
    for y in range(0, max_y):
        char = grid[x][y]
        if char == 'X':
            if scan_up(grid,x, y):
                count+=1 
            if scan_left(grid,x,y):
                count+=1 
            if scan_right(grid,x,y):
                count+=1 
            if scan_down(grid,x,y):
                count+=1
            if scan_dl(grid, x, y):
                count+=1
            if scan_dr(grid, x, y):
                count+=1
            if scan_ul(grid, x, y):
                count+=1
            if scan_ur(grid, x, y):
                count+=1

print(f'part 1: {count}')

count = 0
for x in range(1, max_x-1):
    for y in range(1, max_y-1):
        if grid[x][y] == 'A':
            if grid[x-1][y-1] == 'M' and grid[x+1][y+1] =="S":
                if (grid[x+1][y-1] == 'M' and grid[x-1][y+1] =="S" or
                    grid[x+1][y-1] == 'S' and grid[x-1][y+1] =="M"):
                    count +=1
            elif grid[x-1][y-1] == 'S' and grid[x+1][y+1] =="M":
                if (grid[x+1][y-1] == 'M' and grid[x-1][y+1] =="S" or
                    grid[x+1][y-1] == 'S' and grid[x-1][y+1] =="M"):
                    count+=1
print(f'part 2: {count}')
