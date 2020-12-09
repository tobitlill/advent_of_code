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



# helper function
def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)

highest = 0
for passport in data:
    row = int(passport[:7], 2)
    col = int(passport[-3:], 2)
    
    seat_id = row * 8 + col
    if seat_id > highest:
        highest = seat_id
    #print("Row: {}, Col: {}".format(row, col))
print(highest)
