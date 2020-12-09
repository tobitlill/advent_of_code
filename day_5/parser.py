#!/usr/bin/python3

import re

# read in input data
data = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        line = re.sub(r'[F|L]', "0", line)
        line = re.sub(r'[B|R]', "1", line)
        print(line)
        
        data.append(line)
f.close()

highest = 0
for passport in data:
    row = int(passport[:7], 2)
    col = int(passport[-3:], 2)
    
    seat_id = row * 8 + col
    if seat_id > highest:
        highest = seat_id
    #print("Row: {}, Col: {}".format(row, col))
print(highest)
