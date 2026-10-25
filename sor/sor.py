#!/usr/bin/env python3

from math import floor, log10

initial_values = [
    [0.400, 0.600, 0.400],
    [0.100, 0.300, 0.100],
]

# Include the boundary ring around the two-by-three interior grid.
grid = [
    [0.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, *initial_values[0], 0.0],
    [0.0, *initial_values[1], 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
]


def round_three_significant(value):
    if value == 0:
        return 0.0
    scale = 10 ** (2 - floor(log10(abs(value))))
    return floor(value * scale + 0.5) / scale


def update_cell(row, col):
    neighbors = (
        grid[row - 1][col],
        grid[row][col - 1],
        grid[row + 1][col],
        grid[row][col + 1],
    )
    total = round_three_significant(sum(neighbors))
    grid[row][col] = round_three_significant(total / 4)


for row in range(1, 3):
    for col in range(1, 4):
        update_cell(row, col)

for row in grid:
    print(" ".join(f"{value:.3f}" for value in row))
