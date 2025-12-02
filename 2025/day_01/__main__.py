"""Advent of Code 2025, Day 1"""

with open("2025/day_01/input.txt", "r", encoding="utf-8") as f:
    position: int = 50
    result_1: int = 0
    result_2: int = 0
    for line in f.readlines():
        rotation = int(line.strip().replace("L", "-").replace("R", "+"))
        new_position = position + rotation
        if new_position <= 0 or new_position >= 100:
            result_2 += abs(((new_position + 100) // 100) - 1)
            if rotation < 0:
                result_2 += int(new_position % 100 == 0)
                result_2 -= int(position == 0)
        new_position = new_position % 100
        result_1 += int(new_position == 0)
        position = new_position

print(f"Result 1: {result_1}")
print(f"Result 2: {result_2}")
