"""Solve the maximum-profit refinery running plan from Symonds (1955), Chapter 3.

The refinery has limited weekly supplies of crudes A, B, C, and D. It can run
crude C through either operation C1 or C2. Each of the five operations produces
a different mix of products G, H, L, and F, and earns a different profit per
barrel. The plan must stay within the available crude supplies and must not
produce more than the stated target for any product.

The weekly crude supplies are 100 Mbpw each for A, B, and D, and 200 Mbpw
for C. The product targets are 170 Mbpw of G, 85 of H, 20 of L, and 85 of F.
The per-barrel profits for A, B, C1, C2, and D are 10, 20, 15, 25, and 7
cents, respectively.

The product targets cap production; they are not mandatory minimums. A target
can remain partly unmet if producing the product would not be profitable
enough, and the unfilled amount is tracked as a slack variable. This is why the
solution can leave some of the F target unfilled while meeting the targets for
G, H, and L.

The simplex method starts with a feasible plan that runs no crude and has all
product targets unfilled. At each step, the most negative coefficient in the
profit row identifies the operation that can improve profit most. The minimum
ratio test finds which crude supply or product target limits that operation.
A tableau pivot brings the operation into the plan and the limiting variable
out. When the profit row has no negative coefficients, the plan is optimal.

The resulting weekly plan runs A, B, C1, C2, and D at 37.5, 100, 100, 100, and
about 58.3 Mbpw. It leaves 3.75 Mbpw of F unmet and earns about $67,833 per
week; Symonds reports $67,830 using the rounded tableau value.
"""

import numpy as np


def main() -> None:
    """Build the refinery model, apply simplex pivots, and print the plan."""
    # Each column is a refinery operation; each row is a product yield.
    operations = ("A", "B", "C1", "C2", "D")
    products = ("G", "H", "L", "F")
    yields = np.array(
        [
            [0.6, 0.5, 0.4, 0.4, 0.3],
            [0.2, 0.2, 0.3, 0.1, 0.3],
            [0.0, 0.0, 0.0, 0.2, 0.0],
            [0.1, 0.2, 0.2, 0.2, 0.3],
        ]
    )

    # Crude C can be run through either C1 or C2.
    crude_used = np.array(
        [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1],
        ]
    )
    constraints = np.vstack((crude_used, yields))
    crude_limits = np.array([100, 100, 200, 100])  # A, B, C, D (Mbpw)
    product_limits = np.array([170, 85, 20, 85])  # G, H, L, F (Mbpw)
    limits = np.concatenate((crude_limits, product_limits))
    profit_per_barrel = np.array([10, 20, 15, 25, 7])  # cents

    crude_names = ("A", "B", "C", "D")
    slack_names = (
        "Unused A",
        "Unused B",
        "Unused C",
        "Unused D",
        "Unfilled G",
        "Unfilled H",
        "Unfilled L",
        "Unfilled F",
    )
    variable_names = operations + slack_names
    constraint_count = len(limits)
    operation_count = len(operations)
    variable_count = len(variable_names)
    tolerance = 1e-10

    # The tableau stores the constraints, slack variables, and right-hand limits.
    # Starting with all slacks in the basis gives an initial feasible plan.
    tableau = np.zeros((constraint_count + 1, variable_count + 1))
    tableau[:constraint_count, :operation_count] = constraints
    tableau[:constraint_count, operation_count:variable_count] = np.eye(
        constraint_count
    )
    tableau[:constraint_count, -1] = limits
    tableau[-1, :operation_count] = -profit_per_barrel
    basis = list(range(operation_count, variable_count))
    pivots = []

    # Pivot until no operation can improve the profit.
    while True:
        objective_row = tableau[-1, :-1]
        entering_column = int(np.argmin(objective_row))
        if objective_row[entering_column] >= -tolerance:
            break

        # Of the rows that can supply this operation, choose the smallest
        # limit-to-use ratio. That row's current basic variable must leave.
        entering_values = tableau[:constraint_count, entering_column]
        eligible_rows = entering_values > tolerance
        if not np.any(eligible_rows):
            raise RuntimeError(
                f"profit is unbounded while increasing "
                f"{variable_names[entering_column]}"
            )

        ratios = np.full(constraint_count, np.inf)
        ratios[eligible_rows] = (
            np.maximum(tableau[:constraint_count, -1][eligible_rows], 0)
            / entering_values[eligible_rows]
        )
        leaving_row = int(np.argmin(ratios))
        pivots.append(
            (variable_names[entering_column], variable_names[basis[leaving_row]])
        )

        # Make the pivot 1, then 0 out the rest of its column.
        tableau[leaving_row] /= tableau[leaving_row, entering_column]
        for row in range(constraint_count + 1):
            if row != leaving_row:
                tableau[row] -= tableau[row, entering_column] * tableau[leaving_row]
        basis[leaving_row] = entering_column
        tableau[np.abs(tableau) < tolerance] = 0

    # Read the operations and remaining limits from the final basis.
    values = np.zeros(variable_count)
    values[basis] = tableau[:constraint_count, -1]
    operation_volumes = values[:operation_count]
    slack_values = values[operation_count:]
    product_volumes = yields @ operation_volumes

    print("Simplex pivots:")
    for entering, leaving in pivots:
        print(f"  enter {entering:>2}; leave {leaving}")

    print("\nCrude operations (Mbpw):")
    for name, volume in zip(operations, operation_volumes):
        print(f"  {name:>2}: {volume:7.3f}")

    print("\nProducts (Mbpw):")
    for index, name in enumerate(products):
        print(
            f"  {name}: produced {product_volumes[index]:7.3f}, "
            f"unfilled {slack_values[len(crude_names) + index]:6.3f}, "
            f"limit {limits[len(crude_names) + index]}"
        )

    print("\nUnused crude (Mbpw):")
    for name, volume in zip(crude_names, slack_values[: len(crude_names)]):
        print(f"  {name}: {volume:7.3f}")

    # Volumes are in thousand barrels per week; profit is in cents per barrel.
    weekly_profit = (profit_per_barrel @ operation_volumes) * 10
    print(f"\nMaximum profit: ${weekly_profit:,.2f} per week")
    print("The book reports $67,830 per week after rounding its tableau value.")


if __name__ == "__main__":
    main()
