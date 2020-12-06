#!/usr/bin/python3

import re

# read input data into raw_input var 
raw_input = ""
with open('input.txt', 'r') as f:
    raw_input = f.readlines()

f.close()


# convert the raw data into an array of arrays (for each passport ONE array)
tmp_data = []
tmp = []
for field in raw_input:
    if field != "\n":
        tmp.append(field.strip())
    else:
        tmp_data.append(tmp)
        tmp = []

# convert the array of arrays in an array of dicts with the abreviations as keys
data = []
passport = {}
for array in tmp_data:
    tmp = " ".join(array)
    tmp = tmp.split(" ")
    
    for entry in tmp:
        key, value = entry.split(":")
        passport[key] = value

    data.append(passport)
    passport = {}

# list of the needed keys of a valid passport - cid can be omitted :-)
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# now the fun part.. check each passport if it is valid or not
is_valid = True
valid_count = 0

for passport in data:
    has_all_keys = all(k in passport for k in keys)
   
    if not has_all_keys:
        print("Missing keys")
        continue

    if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        print("Invalid BYR")
        continue
    
    if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        print("Invalid IYR")
        continue
    
    if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        print("Invalid EYR")
        continue

    if passport['hgt'][-2:] == "cm":
        if int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193:
            print("Invalid HGT")
            continue
    elif passport['hgt'][-2:] == 'in':
        if int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76:
            print("Invalid HGT")
            continue
    else:
        print("Invalid hgt")
        continue

    if passport['hcl'][0] != '#' or len(re.findall("[a-f0-9]{6}$", passport['hcl'][1:])) == 0:
        print("Invalid HCL")
        continue

    if not any(k in passport['ecl'] for k in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        print("Invalid ECL")
        continue

    if len(re.findall("[0-9]{9}$", passport['pid'])) == 0:
        print("Invalid PID")
        continue

    if is_valid:
        valid_count += 1

print()
print("Number of valid passports: " + str(valid_count))



