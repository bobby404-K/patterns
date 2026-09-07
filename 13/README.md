# Pattern 13: Floyd's Triangle

## Intuition
Consecutive numbers starting from `1` are printed in sequence across rows in a right-angled triangular form.

## Approach
1. Initialize a counter `num = 1`.
2. Run an outer loop `i` from `1` to `N` for rows.
3. For each row, run an inner loop `j` from `1` to `i`.
4. Print the current value of `num` with a space and increment `num += 1`.
5. After each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Total numbers printed = `N*(N+1)/2`.
- **Space Complexity:** `O(1)` — Constant extra space.
