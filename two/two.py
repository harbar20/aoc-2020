with open("two.txt") as f:
    passwordsList = f.read().split("\n")

# Part 1
ctr = 0
for policy in passwordsList:
    password = policy.split(": ")[1]
    letter = policy.split(": ")[0].split(" ")[1]
    minimum = int(policy.split("-")[0])
    maximum = int(policy.split("-")[1].split(" ")[0])
    
    if password.count(letter) >= minimum and password.count(letter) <= maximum:
        ctr += 1
        
print(ctr)

# Part 2
ctr = 0
for policy in passwordsList:
    password = policy.split(": ")[1]
    letter = policy.split(": ")[0].split(" ")[1]
    pos1 = int(policy.split("-")[0])-1
    pos2 = int(policy.split("-")[1].split(" ")[0])-1
    
    if bool(password[pos1] == letter) ^ bool(password[pos2] == letter):
        ctr += 1

print(ctr)