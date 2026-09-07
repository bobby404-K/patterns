# Pattern 05: Inverted Right-Angled Star Triangle

## Intuition
The number of stars decreases in each row. The 1st row has `N` stars, the 2nd row has `N-1`, the 3rd has `N-2`, and so on until only 1 star remains in the last row.

## Approach
1. Run an outer loop `i` from `0` to `N-1` for rows.
2. For each row, run an inner loop `j` from `N` down to `i+1`.
3. Print `*` in each iteration of the inner loop.
4. After finishing each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Total stars printed = `N*(N+1)/2`.
- **Space Complexity:** `O(1)` — Constant extra space.
