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



big_board = []
for row in board:
    big_board.append(row*32)

outfile = open('output.txt', 'w')
for row in big_board:
    for char in row:
#        print(char, end='')
        outfile.write(char)
#    print()
    outfile.write("\n")

outfile.close()

tree_count = 0
for y in range(1,rows):
    val = getValue(board, y*3, y)
    #val = big_board[y][y*3-1]
    
    if val == '#':
        tree_count += 1
        big_board[y][y*3-1] = 'X'
    else:
        big_board[y][y*3-1] = 'O'
    print("(" + str(y) + "," + str(y*3-1) + ") | " + str(tree_count) + ": " + str(val))

print("Trees hit: " + str(tree_count))

outfile = open('output.txt', 'w')
for row in big_board:
    for char in row:
#        print(char, end='')
        outfile.write(char)
#    print()
    outfile.write("\n")

outfile.close()


print()
print("Done - Happy Christmas")
