#!/usr/bin/python3

# read in input data
data = []
group = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()

        if line != "":
            group.append(line)
        else:
            data.append(group)
            group = []
    data.append(group)
    group = []
f.close()

# strategy: 
# count every occurence of each character (= question answered with yes)
# if count for a specific char is equal to the amount of people in that group
# all of them answered yes to that question 

sum_all_answers = 0

for group in data:
    persons_in_group = len(group)
    chars_in_group = {}
    for person in group:
        for char in person:
            if char in chars_in_group:
                chars_in_group[char] += 1
            else:
                chars_in_group[char] = 1

    # if count of one char is equal to the amount of people 
    # then this question has been answered by all with yes
    # -> add one to the overall count :-)
    for char in chars_in_group:
        if chars_in_group[char] == persons_in_group:
            sum_all_answers += 1


print("Sum of all groups: {}".format(sum_all_answers))