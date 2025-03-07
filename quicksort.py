def quick_sort(l: list[int]) -> list[int]:
    length = len(l)

    if length == 0:  # Base case: empty list
        return []
    if length == 1:  # Base case: list of length 1
        return l

    pivot = l[0]
    left_list = []
    right_list = []

    for element in l[1:]:
        if element < pivot:
            left_list.append(element)
        else:
            right_list.append(element)

    return quick_sort(left_list) + [pivot] + quick_sort(right_list)


def main() -> None:
    l = [5, 7, 2, 9, 1, 10]
    print(quick_sort(l))


if __name__ == "__main__":
    main()
