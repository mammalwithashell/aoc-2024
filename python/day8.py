from collections import defaultdict
import itertools

with open('input/day8.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def build_frequency_lookup(lines: list[str]) -> dict:
    """
    Builds a dictionary of frequencies to coordinates in the grid
    """
    frequency_lookup = defaultdict(list)
    for y, line in enumerate(lines):
        for x, frequency in enumerate(line):
            if frequency != '.':  # Ignore empty spaces
                frequency_lookup[frequency].append((x, y))
    return frequency_lookup

def get_frequency_pairs(frequency_coordinates: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Gets all unordered pairs of frequencies
    """
    return list(itertools.combinations(frequency_coordinates, 2))

def find_antinodes_from_pair_pt1(pair: tuple[tuple[int, int], tuple[int, int]], bounds: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Finds the antinode coordinates within the grid from a pair of frequency coordinates
    """
    (x1, y1), (x2, y2) = pair
    mx, my = bounds
    dx, dy = abs(x1 - x2), abs(y1 - y2)
    antinode_positions = []
    if x1 > x2: # first coordinate is farther right
        ax1 = x1 + dx
        ax2 = x2 - dx
        if y1 < y2: # first coordinate is higher
            ay1 = y1 - dy
            ay2 = y2 + dy
        else: # first coordinate is farther right and lower 
            ay1 = y1 + dy
            ay2 = y2 - dy
    else: # first coordinate is farther left
        ax1 = x1 - dx
        ax2 = x2 + dx
        if y1 < y2: # first coordinate is higher
            ay1 = y1 - dy
            ay2 = y2 + dy
        else: # first coordinate is lower
            ay1 = y1 + dy
            ay2 = y2 - dy
    if ax1 >= 0 and ax1 < mx and ay1 >= 0 and ay1 < my:
        antinode_positions.append((ax1, ay1))
    if ax2 >= 0 and ax2 < mx and ay2 >= 0 and ay2 < my:
        antinode_positions.append((ax2, ay2))
    return antinode_positions

def find_antinodes_from_pair_pt2(pair: tuple[tuple[int, int], tuple[int, int]], bounds: tuple[int, int]) -> list[tuple[int, int]]:
    """Finds all antinode positions within the grid inline with the pair of frequencies

    Args:
        pair (tuple[tuple[int, int], tuple[int, int]]): xy coordinates of both frequencies
        bounds (tuple[int, int]): max x and y coordinates

    Returns:
        list[tuple[int, int]]: list of antinode coordinates
    """
    
    (x1, y1), (x2, y2) = pair
    mx, my = bounds
    dx, dy = abs(x1 - x2), abs(y1 - y2)
    antinode_positions = []
    if x1 > x2: # first coordinate is farther right
        if y1 < y2: # first coordinate is higher
            antinode_positions.extend((ax, ay) for ax, ay in zip(range(x1, mx, dx), range(y1, -1, -dy)))
            antinode_positions.extend((ax, ay) for ax, ay in zip(range(x2, -1, -dx), range(y2, my, dy)))
        else: # first coordinate is farther right and lower 
            antinode_positions.extend((ax, ay) for ax, ay in zip(range(x1, mx, dx), range(y1, my, dy)))
            antinode_positions.extend((ax, ay) for ax, ay in zip(range(x2, -1, -dx), range(y2, -1, -dy)))
    else: # first coordinate is farther left
        if y1 < y2: # first coordinate is higher
            antinode_positions.extend((ax, ay) for ax, ay in zip(range(x1, -1, -dx), range(y1, -1, -dy)))
            antinode_positions.extend((ax, ay) for ax, ay in zip(range(x2, mx, dx), range(y2, my, dy)))
        else: # first coordinate is lower
            antinode_positions.extend((ax, ay) for ax, ay in zip(range(x1, -1, -dx), range(y1, my, dy)))
            antinode_positions.extend((ax, ay) for ax, ay in zip(range(x2, mx, dx), range(y2, -1, -dy)))

    return antinode_positions

def part_1(lines: list[str]) -> int:
    """
    Finds the number of unique antinode positions in the grid
    """
    antinode_positions = set()
    mx, my = len(lines[0]), len(lines)
    frequency_lookup = build_frequency_lookup(lines)

    for _, frequency_coordinates in frequency_lookup.items():
        frequency_pairs = get_frequency_pairs(frequency_coordinates)

        for pair in frequency_pairs:
            antinode_positions.update(find_antinodes_from_pair_pt1(pair, (mx, my)))

    return len(antinode_positions)

def part_2(lines: list[str]) -> int:
    """Find the number of unique antinode positions in the grid if all positions in line with frequencies are counted as antinodes

    Args:
        lines (list[str]): input lines

    Returns:
        int: number of unique antinode positions
    """
    antinode_positions = set()
    mx, my = len(lines[0]), len(lines)
    frequency_lookup = build_frequency_lookup(lines)

    for _, frequency_coordinates in frequency_lookup.items():
        frequency_pairs = get_frequency_pairs(frequency_coordinates)

        for pair in frequency_pairs:
            antinode_positions.update(find_antinodes_from_pair_pt2(pair, (mx, my)))

    return len(antinode_positions)


if __name__ == '__main__':
    print(part_1(lines)) 
    print(part_2(lines))  # 0