array = [
    [1, "9:00", "5877RC"],
    [2, "9:30", "435879HF"],
    [3, "10:00", ""],
    [4, "10:30", "HYF568"],
    [5, "11:00", ""],
    [6, "11:30", ""],
    [7, "12:00", "GHJR345"],
]


def findFirst(array):
    for appointment in array:
        if appointment[2] == "":
            return appointment[0]
    return -1


print(findFirst(array))
