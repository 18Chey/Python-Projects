def bubble_sort(l: list[int]) -> None:
    """Sorts list ascending"""
    length = len(l)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
        if not swapped:
            break


def main() -> None:
    l = [4, 3, 2, 1, 2]
    bubble_sort(l)
    print(l)


if __name__ == "__main__":
    main()
