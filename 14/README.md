# Pattern 14: Increasing Letter Triangle

## Intuition
Each row contains uppercase letters starting from `A` and increasing up to the `(i + 1)`-th letter of the alphabet (`A`, `A B`, `A B C`, ...).

## Approach
1. Run an outer loop `i` from `0` to `N-1` for rows.
2. For each row, run an inner loop `j` from `0` to `i`.
3. Print `chr(ord('A') + j)` followed by a space.
4. After each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Nested loops iterate through triangular elements.
- **Space Complexity:** `O(1)` — Constant extra space.
