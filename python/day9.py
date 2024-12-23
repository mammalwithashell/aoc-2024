def separate_file_length_and_free_space(string):
    file_length_arr, free_space_arr = [], []
    for i in range(0, len(string), 2):
        free_space_idx = i + 1
        if free_space_idx < len(string):
            file_length_arr.append(int(string[i]))
            free_space_arr.append(int(string[free_space_idx]))
        else:
            file_length_arr.append(int(string[i]))
            free_space_arr.append(0)
    return file_length_arr, free_space_arr

def convert_to_longhand(file_length_arr, free_space_arr):
    long_hand = []
    for file_id, (fl, fs) in enumerate(zip(file_length_arr, free_space_arr)):
        # print(f"fileId {file_id}, fl {fl}, fs {fs}")
        for _ in range(fl):
            long_hand.append(file_id)
        for _ in range(fs):
            long_hand.append(-1)
    return long_hand

def longhand_to_string(longhand):
    return ''.join(str(x) if x > -1 else '.' for x in longhand)

def compactify_file(longhand: list[int]):
    pass
    
def calculate_checksum_pt1(file_length_arr, free_space_arr):
    number_of_files = len(file_length_arr)
    last_file_idx = number_of_files - 1
    front_idx = 0
    checksum = 0
    j = 0

    x = sum(free_space_arr)
    y = sum(file_length_arr)
    sub_checksum_log = []

    back_fl = file_length_arr[last_file_idx]
    while j < y:
        front_fl = file_length_arr[front_idx]
        front_fs = free_space_arr[front_idx]

        for _ in range(front_fl):
            sub_checksum = front_idx * j
            checksum += sub_checksum

            j += 1
            if j == y:
                break
        if j == y:
            break

        for _ in range(front_fs):
            if back_fl == 0:
                last_file_idx -= 1
                back_fl = file_length_arr[last_file_idx]

            sub_checksum = last_file_idx * j
            checksum += sub_checksum

            back_fl -= 1
            j += 1
            if j == y:
                break
        front_idx += 1

    return checksum, sub_checksum_log

def calculate_checksum_pt2(file_length_arr, free_space_arr):
    number_of_files = len(file_length_arr)
    last_file_idx = number_of_files - 1
    front_file_idx = 0
    checksum = 0
    j = 0 # idx for the longhand string

    x = sum(free_space_arr)
    y = sum(file_length_arr)
    longhand_len = x + y
    sub_checksum_log = []
    unmoved_files = [i for i in range(number_of_files -1, 0, -1)]
    moved_files = []
    back_files_tested = []
    front_file_was_moved = False
    sub_checksum_log_fmt = lambda file_idx, j, sub_checksum, pos: f"{'front' if pos else 'back'}_file_idx: {file_idx} * j: {j} = sub_checksum: {sub_checksum}"
    # test each file idx from the back
    while True:
        increment_file_idx = True
        front_fl = file_length_arr[front_file_idx]
        front_fs = free_space_arr[front_file_idx]
        if front_file_idx in unmoved_files or front_file_idx == 0:
            for _ in range(front_fl):
                sub_checksum = front_file_idx * j
                checksum += sub_checksum
                sub_checksum_log.append(sub_checksum_log_fmt(front_file_idx, j, sub_checksum, True))
                j += 1
        else:
            j += front_fl #+ front_fs
            front_file_was_moved = True
            # front_file_idx += 1
            # increment_file_idx = False

        """
        test all file idx starting from the back, if the total file length is 
        less than the front file space then we 'move' 
        it to the front and calculate the checksum for the moved file's position
        """
        



        test_fs = front_fs
        for last_file_idx in range(number_of_files -1, 0, -1):
            if test_fs == 0:
                break
            if last_file_idx not in unmoved_files:
                continue
            if last_file_idx < front_file_idx:
                break
            back_fl = file_length_arr[last_file_idx]
            if back_fl <= test_fs:
                space_diff = test_fs - back_fl
                test_fs -= back_fl
                moved_files.append(last_file_idx)
                unmoved_files.remove(last_file_idx)
                moved_file = True
                for _ in range(back_fl):
                    sub_checksum = last_file_idx * j
                    checksum += sub_checksum
                    sub_checksum_log.append(sub_checksum_log_fmt(last_file_idx, j, sub_checksum, False))

                    j += 1
        if moved_file:

            j += test_fs
            moved_file = False

                #j += space_diff
        # if increment_file_idx:

        # if space_diff > 0:
        #     j += space_diff
        #     space_diff = 0

        front_file_idx += 1
    return checksum, sub_checksum_log


def part_1(file_length_arr, free_space_arr):
    checksum, _ = calculate_checksum_pt1(file_length_arr, free_space_arr)
    return checksum
    
if __name__ == '__main__':
    with open('input/day9.txt') as f:
        line = f.readline().strip()

    test_input = '2333133121414131402'
    test_input_1 = '12345'

    # break up input into file length and the subsequent free space
    file_length_arr, free_space_arr = separate_file_length_and_free_space(test_input) # 60
    lh = convert_to_longhand(file_length_arr, free_space_arr)
    lh_str = longhand_to_string(lh)
    print(calculate_checksum_pt2(file_length_arr, free_space_arr))
    print(longhand_to_string(lh))
    # print(file_length_arr)
    # print(free_space_arr)
    # print(len(line))