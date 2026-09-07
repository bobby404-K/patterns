# Pattern 02: Right-Angled Star Triangle

## Intuition
We need to form a right-angled triangle where the number of stars in each row increases line by line. Row `i` (0-indexed) contains exactly `i + 1` stars.

## Approach
1. Run an outer loop `i` from `0` to `N-1` to handle rows.
2. For each row `i`, run an inner loop `j` from `0` to `i`.
3. In the inner loop, print a star `*`.
4. After finishing the stars of one row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Total stars printed = `1 + 2 + ... + N = N*(N+1)/2`.
- **Space Complexity:** `O(1)` — Constant extra space.
