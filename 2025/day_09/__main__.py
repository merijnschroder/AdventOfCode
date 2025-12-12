"""Advent of Code 2025, Day 9"""

from shapely import Polygon, box

with open("2025/day_09/input.txt", "r", encoding="utf-8") as f:
    red_tiles: list[tuple[int, int]] = []
    rectangles: list[tuple[int, int, int]] = []
    for tile in [tuple(map(int, l.strip().split(","))) for l in f.readlines()]:
        x, y = tile
        for j, tile in enumerate(red_tiles):
            area = (abs(x - tile[0]) + 1) * (abs(y - tile[1]) + 1)
            rectangles.append((len(red_tiles), j, area))
        red_tiles.append((x, y))
    rectangles.sort(key=lambda r: r[2], reverse=True)
    print(f"Result 1: {rectangles[0][2]}")

polygon = Polygon(red_tiles)
for rect in rectangles:
    x1, y1 = red_tiles[rect[0]]
    x2, y2 = red_tiles[rect[1]]
    if polygon.contains(box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))):
        print(f"Result 2: {rect[2]}")
        break
