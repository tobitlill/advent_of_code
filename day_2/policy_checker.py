#!/bin/python3
import re

db = []
with open('input.txt', 'r') as f:
    for line in f:
        db.append(line.strip())
f.close()


counter = 0
for entry in db:
    min_val = re.search('^[0-9]+', entry).group(0)
    max_val = str(re.search('[0-9]+ ', entry).group(0)).strip()
    char = str(re.search('[a-z]', entry).group(0)).strip() 
    password = str(re.search('[a-z]+$', entry).group(0)).strip()
    
    if not password.count(char) < int(min_val) and not password.count(char) > int(max_val):
        counter += 1
print("Number of valid passwords: " + str(counter))
print()
print("Done - Happy Christmas!")
