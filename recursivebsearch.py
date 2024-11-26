def binary_search(array: list[int], target: int) -> int | None:
    """Returns index of target in array or None if not in array"""
    mid = len(array) // 2
    if len(array) == 0:
        return None
    if array[mid] == target:
        return mid
    if array[mid] < target:
        return 1 + mid + binary_search(array[mid + 1 :], target)
    if array[mid] > target:
        return binary_search(array[:mid], target)


def main() -> None:
    stuff = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(stuff, 5))


if __name__ == "__main__":
    main()
