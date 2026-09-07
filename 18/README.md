# Pattern 18: Alpha-Triangle Pattern

## Intuition
Each row starts from the `(N - i)`-th letter of the alphabet and prints consecutive letters up to the `N`-th letter (e.g., for N=4: `D`, `C D`, `B C D`, `A B C D`).

## Approach
1. Run an outer loop `i` from `0` to `N-1` for rows.
2. For each row, run an inner loop `ch` from `ord('A') + N - 1 - i` to `ord('A') + N - 1`.
3. Print `chr(ch)` followed by a space.
4. After each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Nested loops iterate across triangular elements.
- **Space Complexity:** `O(1)` — Constant extra space.
