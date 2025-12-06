"""Advent of Code 2025, Day 6"""


def transpose(matrix: list[list]) -> list[list]:
    return [list(r) for r in zip(*matrix)]


def prod(l: list[int], res: int = 1) -> int:
    return res if len(l) == 0 else res * l[0] * prod(l[1:])


with open("2025/day_06/input.txt", "r", encoding="utf-8") as f:
    matrix = transpose([[n for n in l if n != "\n"] for l in f.readlines()])
    matrix.append([" "] * len(matrix[0]))
    result_1 = result_2 = i = 0
    while i < len(matrix):
        op = matrix[i][-1]
        nmbr_matrix = []
        while any(v.strip() for v in matrix[(i)]):
            nmbr_matrix.append(matrix[i][:-1])
            i += 1
        nmbrs_1 = [int("".join(r)) for r in transpose(nmbr_matrix)]
        nmbrs_2 = [int("".join(r)) for r in nmbr_matrix]
        result_1 += sum(nmbrs_1) if op == "+" else prod(nmbrs_1)
        result_2 += sum(nmbrs_2) if op == "+" else prod(nmbrs_2)
        i += 1
    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")
