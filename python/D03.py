
with open('../input/D03.txt', 'r') as file:
    input = file.read()

total = 0
i = 0
while i < len(input)-4:
    current = input[i]
    if input[i: i+4].lower() == "mul(":
        i += 4
        substring_to_check = input[i:i+8]
        next_cp_in_substring = substring_to_check.find(")")
        if next_cp_in_substring > 0:
            in_parens = substring_to_check[:next_cp_in_substring]
            try:
                [x,y] = in_parens.split(",")
            except:
                continue
            if x.isnumeric() and y.isnumeric():
                total += int(x)*int(y)
    
    i += 1
print(f'part 1: {total}')


total = 0
i = 0
enabled = True
while i < len(input)-4:
    if input[i:].startswith("don't()"):
        enabled = False
    elif input[i:].startswith("do()"):
        enabled = True
    current = input[i]
    if input[i: i+4].lower() == "mul(":
        i += 4
        substring_to_check = input[i:i+8]
        next_cp_in_substring = substring_to_check.find(")")
        if next_cp_in_substring > 0:
            in_parens = substring_to_check[:next_cp_in_substring]
            try:
                [x,y] = in_parens.split(",")
            except:
                continue
            if x.isnumeric() and y.isnumeric() and enabled:
                total += int(x)*int(y)
    
    i += 1

print(f'part 2: {total}')