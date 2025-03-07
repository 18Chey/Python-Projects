def insertion_sort(l: list[int]) -> list[int]:
    length = len(l)
    for i in range(1, length):
        current = i
        while current != 0 and l[current] < l[current - 1]:
            l[current - 1], l[current] = l[current], l[current - 1]
            current -= 1
    return l


def main() -> None:
    l = [5, 7, 2, 9, 1, 10]
    print(insertion_sort(l))


if __name__ == "__main__":
    main()
