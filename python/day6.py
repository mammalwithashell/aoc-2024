from collections import defaultdict


def get_starting_position(grid: list[list[str]]) -> tuple[int, int]:
    for y in range(len(grid)):
        x = "".join(grid[y]).find("^")
        if x != -1:
            return x, y

# Pad the grid with 0s on x and y axis
def pad_grid(grid: list[list[str]]) -> list[list[str]]:
    grid_height = len(grid)
    grid_width = len(grid[0])
    padded_grid = [["0"] * (grid_width + 2) for _ in range(grid_height + 2)]
    #inscribe the original grid into the padded grid
    for y in range(grid_height):
        for x in range(grid_width):
            padded_grid[y+1][x+1] = grid[y][x]
    return padded_grid

# Walk the grid, replacing the current position with an X. Count the number of unique steps taken
def walk_grid(grid: list[list[str]], starting_position: tuple[int, int]) -> int:
    # keep track of direction
    direction_list = [(0, -1), (1, 0), (0, 1), (-1, 0)] # up, right, down, left
    direction_idx = 0
    current_direction = (0, -1) # up (x, y)
    steps = 0
    x, y = starting_position
    try:

        while True:
            if grid[y][x] != "X":
                # mark current position as visited if it's not already marked
                grid[y][x] = "X"
                steps += 1

            dx, dy = direction_list[direction_idx]
            tx = x + dx
            ty = y + dy
            # check the next position
            if grid[ty][tx] == "#":
                # if the next position is an obstacle (#), turn right
                direction_idx = (direction_idx + 1) % 4
                dx, dy = direction_list[direction_idx]
                tx = x + dx
                ty = y + dy
            if grid[ty][tx] == ".":
                # if the next position is open space, move forward
                x, y = tx, ty
            elif grid[ty][tx] == "0":
                # if the next position is a 0, end the walk and return the count of unique steps taken
                return steps
    except KeyboardInterrupt as e:
        print("Interrupted")
        return steps

def find_all_hashtags(grid: list[list[str]]) -> list[tuple[int, int]]:
    hashtags = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#" :
                hashtags.append((x, y))
    return hashtags

def compute_path(grid: list[list[str]], starting_position: tuple[int, int], hashtag_coordinates: list[tuple[int, int]]) -> int:
    direction_list = [(0, -1), (1, 0), (0, 1), (-1, 0)] # up 0, right 1, down 2, left 3 (x, y)
    direction_idx = 0
    x_find_y = defaultdict(list)
    y_find_x = defaultdict(list)
    
    for x, y in hashtag_coordinates:
        x_find_y[x].append(y)
        y_find_x[y].append(x)
    
    is_vertical_move = lambda direction_idx: direction_idx % 2 == 0
    get_lookup = lambda idx: x_find_y if is_vertical_move(idx) else y_find_x # use x lookup if direction is up or down, y lookup if direction is left or right

    # if i hit a hash while going up, ive hit its bottom, decrement y 1 and find nearest hash after turning right
    def get_next_position(x, y, direction_idx) -> tuple[int, int]:
        lookup = get_lookup(direction_idx)
        lookup_nbr = x if is_vertical_move(direction_idx) else y
        xy_of_inline_obstacles = lookup[lookup_nbr]
        # find the hash closest to the current position by finding the hash with the smallest absolute difference in x or y depending on the direction
        # if going up (0) i need the smallest difference in y value where y2 is greater than y1
        # if going right (1) i need the smallest difference in x value where x2 is greater than x1
        # if going down (2) i need the smallest difference in y value where y2 is less than y1
        # if going left (3) i need the smallest difference in x value where x2 is less than x1
        if is_vertical_move(direction_idx):
            if direction_idx == 0:  # up
                if len([y2 for y2 in xy_of_inline_obstacles if y2 < y]) == 0:
                    return -1, -1
                closest_hash = min((abs(y - y2) for y2 in xy_of_inline_obstacles if y2 < y), default=y)
            else:  # down
                if len([y2 for y2 in xy_of_inline_obstacles if y2 > y]) == 0:
                    return -1, -1
                closest_hash = min((abs(y2 - y) for y2 in xy_of_inline_obstacles if y2 > y), default=y)
        else:
            if direction_idx == 1:  # right
                if len([x2 for x2 in xy_of_inline_obstacles if x2 > x]) == 0:
                    return -1, -1
                closest_hash = min((abs(x2 - x) for x2 in xy_of_inline_obstacles if x2 > x), default=x)
            else:  # left
                if len([x2 for x2 in xy_of_inline_obstacles if x2 < x]) == 0:
                    return -1, -1
                closest_hash = min((abs(x - x2) for x2 in xy_of_inline_obstacles if x2 < x), default=x)

        match direction_idx:
            case 0:
                nx, ny = x, y - closest_hash + 1
                return nx, ny
            case 1:
                nx, ny = x + closest_hash - 1, y
                return nx, ny
            case 2:
                nx, ny = x, y + closest_hash - 1
                return nx, ny
            case 3:
                nx, ny = x - closest_hash + 1, y
                return nx, ny

    def add_positions_between_to_set(x1, y1, x2, y2, visited_positions: set[tuple[int, int]]):
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                visited_positions.add((x1, y))
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                visited_positions.add((x, y1))
    
    visited_positions = set()
    x, y = starting_position
    next_position = get_next_position(x, y, direction_idx)
    try:
        while True:
            add_positions_between_to_set(x, y, next_position[0], next_position[1], visited_positions)
            x, y = next_position
            direction_idx = (direction_idx + 1) % 4
            next_position = get_next_position(x, y, direction_idx)
            if next_position == (-1, -1):
                break
    except KeyboardInterrupt as e:
        print("Interrupted")
        
    return len(visited_positions)


# def define_grid_from_input(grid: list[list[str]], starting_position: tuple[int, int]):
#     y, x = starting_position
#     grids_starting_position = grid[y][x]
#     direction_list = [(0, -1), (1, 0), (0, 1), (-1, 0)] # up, right, down, left (x, y)
#     direction_idx = 0
#     while 
#     for line in _input:
#         grid.append(list(line))
#     return grid

def part_1(grid: list[list[str]]) -> int:
    all_tag_locations = find_all_hashtags(grid)
    starting_position = get_starting_position(grid)
    unique_positions = compute_path(grid=grid, starting_position=starting_position, hashtag_coordinates=all_tag_locations)
    return unique_positions



if __name__ == "__main__":
    with open("input/day6.txt") as f:
        _input = [line.strip() for line in f.readlines()]

    print(part_1(_input))  # 6368