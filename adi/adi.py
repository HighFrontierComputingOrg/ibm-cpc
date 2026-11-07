#!/usr/bin/env python3

import numpy as np

initial_values1 = [
    [0.400, 0.600, 0.400],
    [0.100, 0.300, 0.100],
]
initial_values2 = [
    [0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000],
]
initial_values = initial_values2
time_step = 0.5

# The boundary ring surrounds the two-by-three interior grid.
grid = np.array([
    [0.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, *initial_values[0], 0.0],
    [0.0, *initial_values[1], 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
])


def tridiagonal(size, diagonal, neighbor):
    matrix = np.eye(size) * diagonal
    for i in range(size - 1):
        matrix[i, i + 1] = neighbor
        matrix[i + 1, i] = neighbor
    return matrix


def adi_step(grid, step):
    inside = grid[1:-1, 1:-1]
    height, width = inside.shape

    # Solve across each row; use the vertical neighbors from the old grid.
    implicit_x = tridiagonal(width, 1 + 2 * step, -step)
    rhs = tridiagonal(height, 1 - 2 * step, step) @ inside
    rhs[0] += step * grid[0, 1:-1]
    rhs[-1] += step * grid[-1, 1:-1]
    rhs[:, 0] += step * grid[1:-1, 0]
    rhs[:, -1] += step * grid[1:-1, -1]
    after_x = np.linalg.solve(implicit_x, rhs.T).T

    # Solve down each column; use the horizontal neighbors from the new rows.
    implicit_y = tridiagonal(height, 1 + 2 * step, -step)
    rhs = after_x @ tridiagonal(width, 1 - 2 * step, step)
    rhs[:, 0] += step * grid[1:-1, 0]
    rhs[:, -1] += step * grid[1:-1, -1]
    rhs[0] += step * grid[0, 1:-1]
    rhs[-1] += step * grid[-1, 1:-1]
    after_y = np.linalg.solve(implicit_y, rhs)

    result = grid.copy()
    result[1:-1, 1:-1] = after_y
    return result


def solve_adi(grid, step=time_step, tolerance=1e-10):
    grid = np.array(grid, dtype=float)
    if grid.ndim != 2 or min(grid.shape) < 3:
        raise ValueError("Grid must have an interior surrounded by boundaries.")
    if step <= 0 or tolerance <= 0:
        raise ValueError("Step and tolerance must be positive.")

    for iteration in range(1, 100_001):
        updated = adi_step(grid, step)
        change = np.max(np.abs(updated[1:-1, 1:-1] - grid[1:-1, 1:-1]))
        if change <= tolerance:
            return updated, iteration
        grid = updated

    raise RuntimeError("ADI did not converge within 100000 iterations.")


def main():
    solution, iterations = solve_adi(grid)
    print(f"Converged after {iterations} ADI iterations.")
    for row in solution:
        print(" ".join(f"{value:.3f}" for value in row))


if __name__ == "__main__":
    main()
