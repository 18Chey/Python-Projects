def second_largest(l: list[int]) -> int | None:
    """Returns second largest value in list or None"""
    first, second = float("-inf"), float("-inf")

    for number in l:
        if number > first:
            second = first
            first = number
        elif second < number < first:
            second = number

    if second == float("-inf"):
        return None
    return second


def main() -> None:
    l = [4, 7, 9, 3, 2, 0]
    print(second_largest(l))


if __name__ == "__main__":
    main()
