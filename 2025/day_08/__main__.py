"""Advent of Code 2025, Day 8"""

with open("2025/day_08/input.txt", "r", encoding="utf-8") as f:
    boxes: list[tuple[int, int, int]] = []
    connections: list[tuple[int, int, int]] = []
    while line := f.readline():
        x, y, z = map(int, line.split(","))
        for j, box in enumerate(boxes):
            distance = pow(box[0] - x, 2) + pow(box[1] - y, 2) + pow(box[2] - z, 2)
            connections.append((len(boxes), j, distance))
        boxes.append((x, y, z))

circuit_ids = list(range(0, len(boxes)))
for i, connection in enumerate(sorted(connections, key=lambda d: d[2])):
    if i == 1000:
        sizes = sorted([circuit_ids.count(c) for c in set(circuit_ids)], reverse=True)
        print(f"Result 1: {sizes[0] * sizes[1] * sizes[2]}")
    circuit_ids = [
        c if c != circuit_ids[connection[1]] else circuit_ids[connection[0]]
        for c in circuit_ids
    ]
    if len(set(circuit_ids)) == 1:
        print(f"Result 2: {boxes[connection[0]][0] * boxes[connection[1]][0]}")
        break
