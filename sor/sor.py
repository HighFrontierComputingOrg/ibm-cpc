#!/usr/bin/env python3

initial_values1 = [
    [0.400, 0.600, 0.400],
    [0.100, 0.300, 0.100],
]
initial_values2 = [
    [0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000],
]
initial_values = initial_values2
omega = 1.3

# Include the boundary ring around the two-by-three interior grid.
grid = [
    [0.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, *initial_values[0], 0.0],
    [0.0, *initial_values[1], 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
]


def update_cell(row, col):
    neighbors = (
        grid[row - 1][col],
        grid[row][col - 1],
        grid[row + 1][col],
        grid[row][col + 1],
    )
    grid[row][col] += omega * (sum(neighbors) / 4 - grid[row][col])


def formatted_grid():
    return tuple(" ".join(f"{value:.3f}" for value in row) for row in grid)


previous_output = formatted_grid()
iterations = 0
while True:
    for row in range(1, 3):
        for col in range(1, 4):
            update_cell(row, col)
    iterations += 1
    current_output = formatted_grid()
    if current_output == previous_output:
        break
    previous_output = current_output

print(f"Converged after {iterations} iterations (to 3 decimal places).")
for row in current_output:
    print(row)
