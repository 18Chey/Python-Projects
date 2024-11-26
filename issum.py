def is_sum(l: list[int], target=int) -> bool:
    length = len(l)
    for i in range(length - 2):
        if l[i] > target:
            continue
        for j in range(i + 1, length - 1):
            if l[j] > target:
                continue
            if l[i] + l[j] == target:
                return True
    return False


def main() -> None:
    l = [1, 2, 4, 7]
    print(is_sum(l, 1))


if __name__ == "__main__":
    main()
