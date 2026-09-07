# Pattern 16: Alpha-Ramp Pattern

## Intuition
Each row repeats the same letter `i + 1` times, with the letter advancing for each subsequent row (`A`, `B B`, `C C C`, ...).

## Approach
1. Run an outer loop `i` from `0` to `N-1` for rows.
2. Determine character: `ch = chr(ord('A') + i)`.
3. Run an inner loop `j` from `0` to `i` and print `ch` followed by a space.
4. After each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Total letters printed = `N*(N+1)/2`.
- **Space Complexity:** `O(1)` — Constant extra space.
