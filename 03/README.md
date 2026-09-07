# Pattern 03: Right-Angled Number Triangle

## Intuition
Each row contains numbers starting from `1` up to the current row number. The 1st row has `1`, the 2nd row has `1 2`, the 3rd row has `1 2 3`, and so on up to `N`.

## Approach
1. Use an outer loop `i` from `1` to `N` for rows.
2. For each row, use an inner loop `j` from `1` to `i` to print numbers.
3. Each row prints numbers starting from `1` up to `i`.
4. After printing each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Outer loop runs `N` times and inner loop runs up to `i` times.
- **Space Complexity:** `O(1)` — Only loop control variables are used.
