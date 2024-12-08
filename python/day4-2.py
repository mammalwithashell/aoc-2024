with open("input/day4.txt") as f:
    _input = [line.strip() for line in f.readlines()]


x, y = len(_input[0]), len(_input)
def find_x_pattern_count(grid, pattern):
    # only odd length patterns are allowed
    if len(pattern) % 2 != 1:
        return 0
    pattern_center = pattern[len(pattern) // 2]

    center_idx = len(pattern) // 2
    
    count = 0
    topleft = (-1, -1)
    topright = (-1, 1)
    bottomleft = (1, -1)
    bottomright = (1, 1)

    for j in range(1, y-1):
        for i in range(1, x - 1):
            if grid[j][i] == pattern_center:
                # check top left diagonal for pattern completion from center idx
                for letter in pattern[:center_idx]:
                    

                # check top right diagonal for pattern completion from center idx
                # check bottom left diagonal for pattern completion from center idx
                # check bottom right diagonal for pattern completion from center idx
                if topleft == "M" and topright == "M" and bottomleft == "S" and bottomright == "S":
                    count += 1
                    continue
                if topleft == "M" and topright == "S" and bottomleft == "M" and bottomright == "S":
                    count += 1
                    continue
                if topleft == "S" and topright == "S" and bottomleft == "M" and bottomright == "M":
                    count += 1
                    continue
                if topleft == "S" and topright == "M" and bottomleft == "S" and bottomright == "M":
                    count += 1
                    continue
    return count

print(count)