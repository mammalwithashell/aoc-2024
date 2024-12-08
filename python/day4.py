with open("input/day4.txt") as f:
    _input = f.readlines()

# Convert the input into a 2D grid
grid = [line.strip() for line in _input]

def find_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    # Check all directions
    for r in range(rows):
        for c in range(cols):
            # Check horizontally to the right
            if c + word_len <= cols and all(grid[r][c + i] == word[i] for i in range(word_len)):
                count += 1
            # Check horizontally to the left
            if c - word_len >= -1 and all(grid[r][c - i] == word[i] for i in range(word_len)):
                count += 1
            # Check vertically downwards
            if r + word_len <= rows and all(grid[r + i][c] == word[i] for i in range(word_len)):
                count += 1
            # Check vertically upwards
            if r - word_len >= -1 and all(grid[r - i][c] == word[i] for i in range(word_len)):
                count += 1
            # Check diagonally down-right
            if r + word_len <= rows and c + word_len <= cols and all(grid[r + i][c + i] == word[i] for i in range(word_len)):
                count += 1
            # Check diagonally down-left
            if r + word_len <= rows and c - word_len >= -1 and all(grid[r + i][c - i] == word[i] for i in range(word_len)):
                count += 1
            # Check diagonally up-right
            if r - word_len >= -1 and c + word_len <= cols and all(grid[r - i][c + i] == word[i] for i in range(word_len)):
                count += 1
            # Check diagonally up-left
            if r - word_len >= -1 and c - word_len >= -1 and all(grid[r - i][c - i] == word[i] for i in range(word_len)):
                count += 1

    return count

word = "XMAS"
count = find_word(grid, word)
print(f"Total instances of '{word}': {count}")