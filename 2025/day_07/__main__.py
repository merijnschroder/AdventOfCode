"""Advent of Code 2025, Day 7"""

with open("2025/day_07/input.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    split_cnt: int = 0
    locations: list[int] = [0] * len(line)
    locations[line.index("S")] = 1
    while line := f.readline():
        for loc, count in enumerate(locations):
            if count > 0 and line[loc] == "^":
                split_cnt += 1
                locations[loc] -= count
                locations[loc + 1] += count
                locations[loc - 1] += count
    print(f"Result 1: {split_cnt}")
    print(f"Result 2: {sum(locations)}")
