# Pattern 21: Hollow Square Star Pattern

## Intuition
An `N x N` square outline where the outer boundary is filled with stars and the interior is empty (filled with spaces).

## Approach
1. Run an outer loop `i` from `0` to `N-1` for rows.
2. For each row, run an inner loop `j` from `0` to `N-1` for columns.
3. Print `*` if the position is on the border (`i == 0` or `j == 0` or `i == N - 1` or `j == N - 1`).
4. Otherwise, print a space ` `.
5. After each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Checks all `N * N` positions in the grid.
- **Space Complexity:** `O(1)` — Constant extra space.
