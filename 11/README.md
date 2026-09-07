# Pattern 11: Binary Alternating Triangle

## Intuition
Each row contains alternating `0`s and `1`s. Even-indexed rows (0, 2, 4...) start with `1`, and odd-indexed rows (1, 3, 5...) start with `0`.

## Approach
1. Run an outer loop `i` from `0` to `N-1` for rows.
2. For each row, determine starting value: `start = 1 if i % 2 == 0 else 0`.
3. Run an inner loop `j` from `0` to `i`, print `start`, and toggle `start = 1 - start`.
4. After each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Nested loops iterate through triangular elements.
- **Space Complexity:** `O(1)` — Constant extra space.
