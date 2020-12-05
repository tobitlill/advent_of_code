#!/bin/python3
import re

db = []
with open('input.txt', 'r') as f:
    for line in f:
        db.append(line.strip())
f.close()


counter = 0
for entry in db:
    min_val = int(re.search('^[0-9]+', entry).group(0))
    max_val = int(str(re.search('[0-9]+ ', entry).group(0)).strip())
    char = str(re.search('[a-z]', entry).group(0)).strip() 
    password = str(re.search('[a-z]+$', entry).group(0)).strip()
    
    if password[min_val-1:min_val] == char and password[max_val-1:max_val] != char or password[min_val-1:min_val] != char and password[max_val-1:max_val] == char: 
        #print(str(min_val) + " " + str(max_val) + " " + str(char) + " " + str(password))
        counter += 1
    else:
        #print(str(min_val) + " " + str(max_val) + " " + str(char) + " " + str(password))
        pass

print("Number of valid passwords: " + str(counter))
print()
print("Done - Happy Christmas!")
