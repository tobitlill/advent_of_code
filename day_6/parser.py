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

unique_answers = []
sum_all_answers = 0
for group in data:
    for person in group:
        for char in person:
            if char not in unique_answers:
                unique_answers.append(char)
    sum_all_answers += len(unique_answers)
    #print(len(unique_answers))
    unique_answers = []

print("Summe aller Antworten pro Gruppe: {}".format(sum_all_answers))