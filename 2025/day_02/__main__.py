"""Advent of Code 2025, Day 2"""

with open("2025/day_02/input.txt", "r", encoding="utf-8") as f:
    id_ranges: list[tuple] = [
        tuple(int(p) for p in r.split("-")) for r in f.read().split(",")
    ]

result_1: int = 0
result_2: int = 0
for start, end in id_ranges:
    invalid_ids: set[int] = set()
    for repeats in range(2, len(str(end)) + 2):
        x: int = 1
        while (invalid_id := int(str(x) * repeats)) <= end:
            if invalid_id >= start:
                invalid_ids.add(invalid_id)
                result_1 += invalid_id * (repeats == 2)
            x += 1
    result_2 += sum(invalid_ids)

print(f"Result 1: {result_1}")
print(f"Result 2: {result_2}")
