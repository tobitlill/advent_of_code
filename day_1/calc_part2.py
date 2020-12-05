#!/bin/python3

numbers = []
with open('input.txt', 'r') as f:
    for line in f:
        number = int(line.strip())
        numbers.append(number)

for a in numbers:
    for b in numbers:
        for c in numbers: 
            if a + b + c == 2020:
                print("a: " + str(a))
                print("b: " + str(b))
                print("c: " + str(c))
                print("a*b*c: " + str(a*b*c))
                print("Done - Happy Christmas")
                exit()
