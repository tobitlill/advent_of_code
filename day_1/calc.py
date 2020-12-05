#!/bin/python3

numbers = []
with open('input.txt', 'r') as f:
    for line in f:
        number = int(line.strip())
        numbers.append(number)

for a in numbers:
    for b in numbers:
        if a + b == 2020:
            print("a: " + str(a))
            print("b: " + str(b))
            print("a*b: " + str(a*b))
            print("Done - Happy Christmas")
            exit()
