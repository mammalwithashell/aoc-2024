from collections import defaultdict

with open("input/day5.txt") as f:
    _input = f.readlines()


def get_rules_dict_and_updates(_input: str) -> tuple[dict, list[str]]:
    rules = [rule.strip() for rule in _input if "|" in rule]
    updates = [update.strip() for update in _input if "|" not in update and update != "\n" and update != ""] 
    rules_dict = defaultdict(list)
    for rule in rules:
        page, follower = rule.split("|")
        rules_dict[page].append(follower)
    return rules_dict, updates

def identify_bad_update(pages: list[str], rules_dict: dict) -> bool:
    is_bad_update = False

    for i in range(len(pages)-1):
        page = pages[i]
        next_page = pages[i+1]
        if next_page not in rules_dict[page]:
            is_bad_update = True
            break

    return is_bad_update

def get_middle_page(pages: list[str]) -> int:
    middle_page_idx = len(pages) // 2
    return int(pages[middle_page_idx])

def correct_update(pages: list[str], rules_dict: dict) -> list[str]:
    i = 0
    while i < len(pages)-1:
        page = pages[i]
        next_page = pages[i+1]
        if next_page not in rules_dict[page]:
            pages[i], pages[i+1] = next_page, page
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1
    return pages

# Part 1

rules_dict, updates = get_rules_dict_and_updates(_input)
middle_update_sum = sum(get_middle_page(update.split(",")) for update in updates if not identify_bad_update(update.split(","), rules_dict))
print(middle_update_sum)


# Part 2
corrected_bad_updates = [correct_update(update.split(","), rules_dict) for update in updates if identify_bad_update(update.split(","), rules_dict)]
middle_update_sum = sum(get_middle_page(update) for update in corrected_bad_updates)
print(middle_update_sum)
# for update in updates:
#     pages = update.split(",")
#     middle_page = pages[len(pages) // 2]
#     middle_page_idx = len(pages) // 2
#     break_flag = False
#     previous_pages = []

#     for i in range(len(pages)-1):
#         page = pages[i]
#         next_page = pages[i+1]
#         if next_page not in rules_dict[page]:
#             break_flag = True
#             break
#     if not break_flag:
#         middle_update_sum += pages[middle_page_idx] 

#     if not break_flag:
#         for i in range(len(pages)):
#             page = pages[i]
#             next_page = pages[i +1]
#             if next_page not in rules_dict[page]:
#                 pages[i], pages[i+1] = page, next_page
#         middle_update_sum += pages[middle_page_idx]
# print(middle_update_sum)
    # for i in range(len(pages)):
    #     page = pages[i]
    #     if all(following_page in rules_dict[page] for following_page in pages[i+1:]):
    #         middle_update_sum += middle_page
    # for i in range(len(pages)-1, -1, -1):
    #     page = pages[i]
    #     if all(page in rules_dict[preceding_page] for preceding_page in pages[:i]):
    #         middle_update_sum += middle_page
    #     else:
    #         break_flag = True
    #         break
    # if break_flag:
    #     continue