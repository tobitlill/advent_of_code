#!/usr/bin/python3

import re

data = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.strip('.')
        data.append(line)
f.close()

# read in all combinations
combinations = {}
for rule in data:
    parent_bag = rule.split('bags')[0].strip()

    if "no other" in rule:
        combinations[parent_bag] = {}

    else:
        combinations[parent_bag] = {}
        contained_bags = rule.split('contain')[1].strip()
        contained_bags = contained_bags.split(', ')

        for contained_bag in contained_bags:
            amount = int(re.findall('^[0-9]+', contained_bag)[0])
            contained_bag = re.findall('[a-z ]+$', contained_bag)[0].strip()
            contained_bag = contained_bag.split('bag')[0].strip()
            combinations[parent_bag][contained_bag] = amount

# now we have a josn object of combinations
# iterate over all keys and see which bags can contain either
# a shiny gold bag directly or indirectly

#print(combinations)

# get a list of all possible color combinations
candidates = []
candidates_amount = 0
for key in combinations:
    for combination in combinations:
        if combination not in candidates:
            candidates.append(combination)
candidates_amount = len(candidates)

# find all bags, that can contain my bag directly or indirectly
# this can be done (very inefficiently) by iterating #candidates often
# by that we can be sure, that there is no combination where my bag is 
# the last one in a chain of all other combinations

can_contain_my_bag = []
for i in range(candidates_amount):
    for key in combinations:
        for combination in combinations[key]:
            if "shiny gold" in combination or combination in can_contain_my_bag:
                if key not in can_contain_my_bag:
                    can_contain_my_bag.append(key)

print(len(can_contain_my_bag))