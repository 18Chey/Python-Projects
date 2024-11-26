from random import randint


def merge(list1: list[int], list2: list[int]) -> list[int]:
    """Merges list1 and list2 into an ordered list ascending"""
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result


def merge_sort(l: list[int]) -> list[int]:
    """Sorts l ascending"""

    # Base case: lists containing one item are already sorted
    if len(l) == 1:
        return l

    # Splits list and merges two resultant sublists
    else:
        midpoint = len(l) // 2
        sub1 = merge_sort(l[0:midpoint])
        sub2 = merge_sort(l[midpoint:])

        result = merge(sub1, sub2)

        return result


stuff = [randint(0, 1000) for i in range(20)]
print(merge_sort(stuff))
