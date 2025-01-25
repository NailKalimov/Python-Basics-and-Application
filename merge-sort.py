import random

random_lst = [random.randint(0, 20) for _ in range(10)]
print(random_lst)


def merge(ll, rl):
    left_list_len, right_list_len = len(ll), len(rl)
    left_index, right_index = 0, 0
    res = []

    while left_index < left_list_len and right_index < right_list_len:
        if ll[left_index] < rl[right_index]:
            res.append(ll[left_index])
            left_index += 1
        elif ll[left_index] > rl[right_index]:
            res.append(rl[right_index])
            right_index += 1
        elif ll[left_index] == rl[right_index]:
            res.append(ll[left_index])
            res.append(rl[right_index])
            left_index += 1
            right_index += 1

    if right_index < right_list_len:
        res.extend(rl[right_index:])
    elif left_index < left_list_len:
        res.extend(ll[left_index:])
    return res


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    left_lst = merge_sort(lst[:len(lst) // 2])
    right_lst = merge_sort(lst[len(lst) // 2:])
    return merge(left_lst, right_lst)


print(merge_sort(random_lst))

