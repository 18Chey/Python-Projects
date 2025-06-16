def insertion_sort(l: list[int]) -> None:
    """Sorts list ascending"""
    length = len(l)
    for i in range(1, length):
        j = i
        key = l[j]
        while j > 0 and key < l[j - 1]:
            l[j] = l[j - 1]
            j -= 1
        l[j] = key


def main() -> None:
    l = [4, 3, 2, 1]
    insertion_sort(l)
    print(l)


if __name__ == "__main__":
    main()
