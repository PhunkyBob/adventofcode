class Passport:
    items = {}

    def __init__(self, items):
        self.items = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': '', 'hcl': '', 'ecl': '', 'pid': '', 'cid': ''}
        for i in items:
            self.items[i.split(':')[0]] = i.split(':')[1]

    def is_valid(self):
        return all(self.items[key] or key == "cid" for key in self.items)


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