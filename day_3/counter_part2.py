#!/bin/python3


board = []
with open('input.txt', 'r') as f:
    for line in f:
        arr = []
        for char in line.strip():
            arr.append(char) 
        board.append(arr)

f.close()

# from puzzle input
rows=len(board)
cols=len(board[0])

def getValue(board, x, y):
    return board[y][x % cols]

tree_count_1 = 0
for y in range(1,rows):
    val = getValue(board, y, y)
    
    if val == '#':
        tree_count_1 += 1

tree_count_2 = 0
for y in range(1,rows):
    val = getValue(board, y*3, y)
    
    if val == '#':
        tree_count_2 += 1

tree_count_3 = 0
for y in range(1,rows):
    val = getValue(board, y*5, y)
    
    if val == '#':
        tree_count_3 += 1

tree_count_4 = 0
for y in range(1,rows):
    val = getValue(board, y*7, y)
    
    if val == '#':
        tree_count_4 += 1

tree_count_5 = 0
for y in range(1,rows):
    if y*2 > rows:
        break
    val = getValue(board, y, y*2)
    
    if val == '#':
        tree_count_5 += 1
    
print("Trees hit: " + str(tree_count_1))
print("Trees hit: " + str(tree_count_2))
print("Trees hit: " + str(tree_count_3))
print("Trees hit: " + str(tree_count_4))
print("Trees hit: " + str(tree_count_5))

result = tree_count_1*tree_count_2*tree_count_3*tree_count_4*tree_count_5
print("Result: " + str(result))
print()
print("Done - Happy Christmas")
