# Pattern 15: Inverted Letter Triangle

## Intuition
Each row starts from `A` and continues up to `N - i` letters, decreasing by 1 letter in each row until only `A` remains.

## Approach
1. Run an outer loop `i` from `0` to `N-1` for rows.
2. For each row, run an inner loop `j` from `0` to `N - i - 1`.
3. Print `chr(ord('A') + j)` followed by a space.
4. After each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Nested loops iterate through triangular elements.
- **Space Complexity:** `O(1)` — Constant extra space.
