# Pattern 04: Repeated Row Number Triangle

## Intuition
Instead of printing increasing numbers from `1` to `i` in each row, we print the row number itself repeatedly. The 1st row prints `1`, the 2nd row prints `2 2`, the 3rd row prints `3 3 3`, and so on until `N`.

## Approach
1. Use an outer loop `i` from `1` to `N` for rows.
2. For each row, use an inner loop `j` from `1` to `i`.
3. Instead of printing `j`, print `i` (the current row number).
4. After completing each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Nested loops iterate across triangular elements.
- **Space Complexity:** `O(1)` — Only loop control variables are used.
