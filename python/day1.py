from collections import Counter

with open("input/day1.txt") as f:
    data = f.readlines()

# create two empty lists
l1, l2 = [], []

# split each line into two integers and append to the lists
for line in data:
    a, b = line.split()
    l1.append(int(a))
    l2.append(int(b))

# sort the lists
l1.sort()
l2.sort()


# totalDifference = sum(a - b for a, b in zip(l1, l2))
# Part 1
totalDifference = 0
for a, b in zip(l1, l2):
    totalDifference += abs(a - b)
print(totalDifference)

# Part 2
similarityScore = 0

# Count the number of times each id appears in l2 and add the product of the id and its count to the similarity score
for _id in l1:
    if _id in l2:
        _count = Counter(l2)
        similarityScore += _count[_id] * _id

print(similarityScore)
