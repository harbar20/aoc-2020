with open("one.txt") as f:
    numbers = f.read().split("\n")

# Part 1
for i in numbers:
    i = int(i)
    
    for j in numbers:
        j = int(j)
        
        if i + j == 2020:
            print(i * j)

# Part 2
for i in numbers:
    i = int(i)

    for j in numbers:
        j = int(j)

        for k in numbers:
            k = int(k)

            if i + j + k == 2020:
                print(i * j * k)