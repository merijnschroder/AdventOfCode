"""Advent of Code 2025, Day 3"""


def get_output_joltage(banks: list[list[int]], battery_cnt: int) -> int:
    result = 0
    for bank in banks:
        batteries = bank[:battery_cnt]
        for battery in bank[battery_cnt:]:
            batteries.append(battery)
            for i in range(1, battery_cnt + 1):
                if batteries[i - 1] < batteries[i]:
                    batteries = batteries[: i - 1] + batteries[i:]
                    break
            batteries = batteries[:battery_cnt]
        result += int("".join(str(b) for b in batteries))
    return result


with open("2025/day_03/input.txt", "r", encoding="utf-8") as f:
    input_lines = [[int(b) for b in l.strip()] for l in f.readlines()]
    print(f"Result 1: {get_output_joltage(input_lines, 2)}")
    print(f"Result 2: {get_output_joltage(input_lines, 12)}")
