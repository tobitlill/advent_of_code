#!/usr/bin/python3

import re

# read in input data
data = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        line = re.sub(r'[F|L]', "0", line)
        line = re.sub(r'[B|R]', "1", line)
        # print(line)
        
        data.append(line)
f.close()

seat_ids = []
row_max = 0
col_max = 0
for passport in data:
    row = int(passport[:7], 2)
    col = int(passport[-3:], 2)
    
    if row > row_max:
        row_max = row
    
    if col > col_max:
        col_max = col

    seat_id = row * 8 + col
    
    if seat_id == 15:
        print(row)
    # the first row is not part of the solution according to the task description
    if row != 1:
        seat_ids.append(seat_id)    

seat_ids.sort()

# The Seat ID is the only missing one 
# print the ID, which is not one bigger than the id before it
for i in range(len(seat_ids)):
    if seat_ids[-1] != None:
        if seat_ids[i] != int(seat_ids[i-1]) + 1:
            print(seat_ids[i]-1)

# print("Row Max: {}, Col Max: {}".format(row_max, col_max))
print(seat_ids)