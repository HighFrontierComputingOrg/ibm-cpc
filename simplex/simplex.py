"""Solve the Chapter 3 refinery running-plan example from Symonds (1955)."""

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


FloatArray = NDArray[np.float64]


@dataclass(frozen=True)
class SimplexResult:
    solution: FloatArray
    slacks: FloatArray
    objective: float
    basis: tuple[str, ...]
    pivots: tuple[tuple[str, str], ...]


def simplex_maximize(
    objective: FloatArray,
    constraints: FloatArray,
    limits: FloatArray,
    variable_names: tuple[str, ...],
    slack_names: tuple[str, ...],
    *,
    tolerance: float = 1e-10,
    max_iterations: int = 100,
) -> SimplexResult:
    """Maximize c @ x subject to A @ x <= b and x >= 0."""
    objective = np.asarray(objective, dtype=float)
    constraints = np.asarray(constraints, dtype=float)
    limits = np.asarray(limits, dtype=float)

    if constraints.ndim != 2:
        raise ValueError("constraints must be a two-dimensional array")
    row_count, variable_count = constraints.shape
    if row_count == 0 or variable_count == 0:
        raise ValueError("constraints must contain rows and decision variables")
    if objective.shape != (variable_count,):
        raise ValueError("objective length must match the constraint columns")
    if limits.shape != (row_count,):
        raise ValueError("limits length must match the constraint rows")
    if len(variable_names) != variable_count:
        raise ValueError("variable_names length must match the constraint columns")
    if len(slack_names) != row_count:
        raise ValueError("slack_names length must match the constraint rows")
    if not all(np.isfinite(values).all() for values in (objective, constraints, limits)):
        raise ValueError("objective, constraints, and limits must be finite")
    if np.any(limits < -tolerance):
        raise ValueError("the initial slack basis requires nonnegative limits")
    if not np.isfinite(tolerance) or tolerance <= 0 or max_iterations <= 0:
        raise ValueError("tolerance and max_iterations must be positive")

    tableau = np.zeros(
        (row_count + 1, variable_count + row_count + 1),
        dtype=float,
    )
    tableau[:row_count, :variable_count] = constraints
    tableau[:row_count, variable_count : variable_count + row_count] = np.eye(
        row_count
    )
    tableau[:row_count, -1] = limits
    tableau[-1, :variable_count] = -objective

    all_names = variable_names + slack_names
    basis = list(range(variable_count, variable_count + row_count))
    pivots: list[tuple[str, str]] = []

    for _ in range(max_iterations):
        entering = int(np.argmin(tableau[-1, :-1]))
        if tableau[-1, entering] >= -tolerance:
            break

        entering_column = tableau[:row_count, entering]
        eligible = entering_column > tolerance
        if not np.any(eligible):
            raise RuntimeError(
                f"objective is unbounded; no leaving variable for "
                f"{all_names[entering]}"
            )

        ratios = np.full(row_count, np.inf)
        ratios[eligible] = (
            np.maximum(tableau[:row_count, -1][eligible], 0.0)
            / entering_column[eligible]
        )
        leaving_row = int(np.argmin(ratios))
        pivots.append((all_names[entering], all_names[basis[leaving_row]]))

        tableau[leaving_row] /= tableau[leaving_row, entering]
        for row in range(row_count + 1):
            if row != leaving_row:
                tableau[row] -= tableau[row, entering] * tableau[leaving_row]
        basis[leaving_row] = entering
        tableau[np.abs(tableau) < tolerance] = 0.0
    else:
        if np.min(tableau[-1, :-1]) < -tolerance:
            raise RuntimeError(
                f"simplex did not converge in {max_iterations} pivots"
            )

    values = np.zeros(variable_count + row_count)
    values[basis] = tableau[:row_count, -1]

    return SimplexResult(
        solution=values[:variable_count],
        slacks=values[variable_count:],
        objective=float(objective @ values[:variable_count]),
        basis=tuple(all_names[index] for index in basis),
        pivots=tuple(pivots),
    )


def solve_running_plan() -> tuple[SimplexResult, FloatArray]:
    """Build and solve the refinery model; return the result and product yields."""
    operations = ("A", "B", "C1", "C2", "D")

    yields = np.array(
        [
            [0.6, 0.5, 0.4, 0.4, 0.3],
            [0.2, 0.2, 0.3, 0.1, 0.3],
            [0.0, 0.0, 0.0, 0.2, 0.0],
            [0.1, 0.2, 0.2, 0.2, 0.3],
        ],
        dtype=float,
    )
    crude_availability = np.array(
        [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1],
        ],
        dtype=float,
    )
    constraints = np.vstack((crude_availability, yields))
    limits = np.array([100, 100, 200, 100, 170, 85, 20, 85], dtype=float)
    profit_cents_per_barrel = np.array([10, 20, 15, 25, 7], dtype=float)
    slack_names = (
        "Unused A",
        "Unused B",
        "Unused C",
        "Unused D",
        "Unmet G",
        "Unmet H",
        "Unmet L",
        "Unmet F",
    )

    result = simplex_maximize(
        profit_cents_per_barrel,
        constraints,
        limits,
        operations,
        slack_names,
    )
    return result, yields @ result.solution


def main() -> None:
    result, product_yields = solve_running_plan()
    operations = ("A", "B", "C1", "C2", "D")
    products = ("G", "H", "L", "F")
    requirements = (170, 85, 20, 85)

    print("Simplex pivots:")
    for entering, leaving in result.pivots:
        print(f"  enter {entering:>2}; leave {leaving}")

    print("\nCrude operations (Mbpw):")
    for name, quantity in zip(operations, result.solution):
        print(f"  {name:>2}: {quantity:7.3f}")

    print("\nProducts (Mbpw):")
    for index, (name, requirement) in enumerate(zip(products, requirements)):
        print(
            f"  {name}: produced {product_yields[index]:7.3f}, "
            f"not made {result.slacks[4 + index]:6.3f}, "
            f"required {requirement}"
        )

    print("\nUnused crude (Mbpw):")
    for name, quantity in zip(("A", "B", "C", "D"), result.slacks[:4]):
        print(f"  {name}: {quantity:7.3f}")

    dollars_per_week = result.objective * 10
    print(f"\nMaximum profit: ${dollars_per_week:,.2f} per week")
    print("The book reports $67,830 per week after rounding its tableau value.")


if __name__ == "__main__":
    main()