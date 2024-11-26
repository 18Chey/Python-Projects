frequency = {
    "quads": 0,
    "chest": 0,
    "lats": 0,
    "upper back": 0,
    "hamstrings": 0,
    "delts": 0,
    "biceps": 0,
    "triceps": 0,
    "calves": 0,
}
dayA = ["quads", "upper back", "triceps", "lats", "hamstrings", "calves"]
dayB = ["chest", "hamstrings", "biceps", "quads", "delts", "triceps"]
dayC = ["lats", "delts", "calves", "chest", "upper back", "biceps"]
rest = []
split = [dayA, rest, dayB, rest, dayC, rest]
days = 0
while True:
    for day in split:
        days += 1
        for muscle in day:
            frequency[muscle] += 1
        wait = input()
        print(f"Day {days}: {frequency}")
