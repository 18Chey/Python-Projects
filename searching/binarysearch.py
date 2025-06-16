def binary_search(l: list[int], target: int) -> int | None:
    """Returns index of target in l or None if not present"""
    lowerbound = 0
    upperbound = len(l) - 1

    while lowerbound <= upperbound:
        midpoint = (lowerbound + upperbound) // 2
        if target < l[midpoint]:
            upperbound = midpoint - 1
        elif target > l[midpoint]:
            lowerbound = midpoint + 1
        else:
            return midpoint
    return None


def main() -> None:
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(l, 9))


if __name__ == "__main__":
    main()
