from typing import Any


def linear_search(l: list[Any], target: Any) -> int:
    """Returns index of first occurence of target in list and None if not in list"""
    for i in range(len(l)):
        if l[i] == target:
            return i
    return None


def main() -> None:
    stuff = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(linear_search(stuff, 3))


if __name__ == "__main__":
    main()
