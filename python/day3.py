import re

with open("input/day3.txt") as f:
    _input = f.read()

# Part 1
commands = re.findall(r"mul\((\d+),(\d+)\)", _input)
totalProduct = sum(int(x) * int(y) for x, y in commands)

# Part 2
split_content = re.split(r"(do\(\)|don't\(\))", _input)

# Process the split content to determine the preceding pattern
processed_content = [("do()", split_content[0])]
for i in range(1, len(split_content), 2):
    preceding_pattern = split_content[i]
    content = split_content[i + 1]
    processed_content.append((preceding_pattern, content))

# Print the results
totalProduct = 0
for pattern, content in processed_content:
    if pattern == "do()":
        commands = re.findall(r"mul\((\d+),(\d+)\)", content)
        totalProduct += sum(int(x) * int(y) for x, y in commands)

print(totalProduct)