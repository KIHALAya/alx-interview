#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island with no lakes.

    Args:
        grid (list): A 2D list representing the grid 
        where 1 is land and 0 is water.

    Returns:
        int: The perimeter of the island.
    """
    p = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, c in enumerate(row):
            if c == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            p += sum(edges)
    return p
