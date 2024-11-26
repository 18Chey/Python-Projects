def bubble_sort(l: list[int]) -> list[int]:
    """Returns sorted list ascending"""
    n = len(l)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
        if not swapped:
            break
    return l


def main() -> None:
    l = [3, 1, 2, 4, 9, 4, 6, 4]
    print(bubble_sort(l))


if __name__ == "__main__":
    main()
