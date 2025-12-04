"""Advent of Code 2025, Day 4"""


def get_removed_rolls(diagram: list[list[str]], actually_remove: bool) -> int:
    result: int = 0
    while True:
        removed_rolls = 0
        for i in range(1, len(diagram) - 1):
            for j in range(1, len(diagram[i]) - 1):
                if diagram[i][j] == "@" and (
                    sum(
                        (
                            1
                            for y in range(j - 1, j + 2)
                            for x in range(i - 1, i + 2)
                            if diagram[x][y] == "@"
                        )
                    ) < 5
                ):
                    result += 1
                    removed_rolls += int(actually_remove)
                    diagram[i][j] = "." if actually_remove else "@"
        if removed_rolls == 0:
            return result


with open("2025/day_04/input.txt", "r", encoding="utf-8") as f:
    input_lines = [["."] + list(l.strip()) + ["."] for l in f.readlines()]
    empty_line = [["."] * len(input_lines[0])]
    input_lines = empty_line + input_lines + empty_line
    print(f"Result 1: {get_removed_rolls(input_lines, False)}")
    print(f"Result 2: {get_removed_rolls(input_lines, True)}")
