import math
with open("three.txt") as f:
    rows = f.read().split("\n")

# Part 1
def count_trees(rows, down, right2):
    trees = 0
    new_down = down
    i = 0
    while new_down < len(rows):
        row = rows[new_down]
        if row[(right2*(i+1)) % len(row)] == "#":
            trees += 1
        i += 1
        new_down = (i+1)*down
    return trees

print(count_trees(rows, 2, 1))

print()

# Part 2
counts = [count_trees(rows, 1, 1), count_trees(rows, 1, 3), count_trees(rows, 1, 5), count_trees(rows, 1, 7), count_trees(rows, 2, 1)]
print(counts)
product = 1
print(math.prod(counts))
