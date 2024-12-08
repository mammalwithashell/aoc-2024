with open("input/day2.txt") as f:
    _input = f.readlines()

def is_decreasing(levels):
    for i in range(len(levels) - 1):
        if levels[i] < levels[i + 1]:
            return False
    return True

def is_increasing(levels):
    for i in range(len(levels) - 1):
        if levels[i] > levels[i + 1]:
            return False
    return True

def all_increase_or_decrease(levels):
    return is_decreasing(levels) or is_increasing(levels)

def has_safe_difference(levels):
    for i in range(len(levels) - 1):
        sequential_diff = abs(levels[i] - levels[i + 1])
        if  sequential_diff > 3 or sequential_diff == 0:
            return False
    return True

def generate_permutations(levels):
    return [levels[:i] + levels[i+1:] for i in range(len(levels))]

safe_reports = 0
for report in _input:
    levels = [int(level) for level in report.split()]
    permutations = generate_permutations(levels)

    for perm in permutations:
        if all_increase_or_decrease(perm) and has_safe_difference(perm):
            safe_reports += 1
            break

# Part 1
print(safe_reports)

# Part 2
