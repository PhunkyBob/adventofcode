import re

class Passport:
    items = {}

    validation = {
        'byr': lambda v: 1920 <= int(v) <= 2002 and len(v) == 4,
        'iyr': lambda v: 2010 <= int(v) <= 2020 and len(v) == 4,
        'eyr': lambda v: 2020 <= int(v) <= 2030 and len(v) == 4,
        'hgt': lambda v: (v[-2:] == 'cm' and 150 <= int(v[:-2]) <= 193) or (v[-2:] == 'in' and 59 <= int(v[:-2]) <= 76),
        'hcl': lambda v: re.match(r'^#[\da-f]{6}$', v),
        'ecl': lambda v: v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda v: re.match(r'^\d{9}$', v),
        'cid': lambda v: True,
    }

    def __init__(self, items):
        self.items = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': '', 'hcl': '', 'ecl': '', 'pid': '', 'cid': ''}
        for i in items:
            self.items[i.split(':')[0]] = i.split(':')[1]

    def is_valid(self):
        return all(self.validation[key](self.items[key]) for key in self.items)



file = open('day_04_input.txt', 'r') 
content = file.read()

lines = content.split("\n\n")
total_valid = 0
for l in lines:
    items = l.replace("\n", " ").strip().split(" ")
    passport = Passport(items)
    if passport.is_valid():
        total_valid = total_valid + 1

print(f"Total valid: {total_valid}")