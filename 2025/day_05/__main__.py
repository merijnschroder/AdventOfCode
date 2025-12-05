"""Advent of Code 2025, Day 5"""


def add_range(range_list: list[tuple], new_range: tuple) -> list[tuple]:
    covered_idxs = [
        i
        for i, r in enumerate(range_list)
        if r[0] <= new_range[1] and r[1] >= new_range[0]
    ]
    if len(covered_idxs) == 0:
        return sorted(range_list + [new_range], key=lambda r: r[0])
    range_list[covered_idxs[0]] = (
        min(range_list[min(covered_idxs)][0], new_range[0]),
        max(range_list[max(covered_idxs)][1], new_range[1]),
    )
    return range_list[: min(covered_idxs) + 1] + range_list[max(covered_idxs) + 1 :]


with open("2025/day_05/input.txt", "r", encoding="utf-8") as f:
    ranges: list[tuple] = []
    while (l := f.readline()) != "\n":
        new = tuple(int(r) for r in l.strip().split("-"))
        ranges = add_range(ranges, new)
    result_1 = sum(
        1 for i in f.readlines() if any(1 for r in ranges if r[0] <= int(i) <= r[1])
    )
    result_2 = sum(r[1] - r[0] + 1 for r in ranges)
    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")
