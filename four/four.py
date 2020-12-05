with open("four.txt") as f:
    passports = f.read().split("\n\n")

# Part 1
numValid = 0
for passport in passports:
    creds = passport.split("\n")
    creds = [i.split(" ") for i in creds]
    creds = [inner if type(outer) == list else outer for outer in creds for inner in outer]
    creds = " ".join(creds)
    if "byr:" in creds and "iyr:" in creds and "eyr:" in creds and "hgt:" in creds and "hcl:" in creds and "ecl:" in creds and "pid:" in creds:
        numValid += 1
print(numValid)

print()

# Part 2
def isInt(s, sys):
    try: 
        int(s, sys)
        return True
    except ValueError:
        return False
numValid = 0
for passport in passports:
    creds = passport.split("\n")
    creds = [i.split(" ") for i in creds]
    creds = [inner if type(outer) == list else outer for outer in creds for inner in outer]

    new = {}
    for cred in creds:
        split_cred = cred.split(":")
        new[split_cred[0]] = split_cred[1]


    valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


    creds = " ".join(creds)
    if "byr:" in creds and "iyr:" in creds and "eyr:" in creds and "hgt:" in creds and "hcl:" in creds and "ecl:" in creds and "pid:" in creds:
        bool1 = (int(new["byr"]) >= 1920 and int(new["byr"]) <= 2002)

        bool2 = (int(new["iyr"]) >= 2010 and int(new["iyr"]) <= 2020)

        bool3 = (int(new["eyr"]) >= 2020 and int(new["eyr"]) <= 2030)

        bool4_1 = (new["hgt"].endswith("cm") and isInt(new["hgt"][0:3], 10) and (int(new["hgt"][0:3]) >= 150 and int(new["hgt"][0:3]) <= 193))
        bool4_2 = (new["hgt"].endswith("in") and isInt(new["hgt"][0:2], 10) and (int(new["hgt"][0:2]) >= 59 and int(new["hgt"][0:2]) <= 76))
        bool4 = bool4_1 or bool4_2

        bool5_1 = (new["hcl"].startswith("#"))
        bool5_2 = isInt(new["hcl"][1:], 16)
        bool5 = bool5_1 and bool5_2

        bool6 = (new["ecl"] in valid_eye_colors)

        bool7 = (len(new["pid"]) == 9)

        new_bool = bool1 and bool2 and bool3 and bool4 and bool5 and bool6 and bool7
        
        
        if new_bool:
            numValid += 1
print(numValid)