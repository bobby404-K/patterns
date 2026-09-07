# Pattern 06: Inverted Right-Angled Number Triangle

## Intuition
Each row starts from `1` and continues up to `N - i`, where `i` is the current row index. The number of elements decreases with each row, creating an inverted triangle of numbers.

## Approach
1. Run an outer loop `i` from `0` to `N-1` for rows.
2. Inside it, run an inner loop `j` from `N` down to `i+1`.
3. Print numbers starting from `1` to `N - i` using `(N - j + 1)`.
4. After finishing each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Outer loop runs `N` times and inner loop runs `N-i` times.
- **Space Complexity:** `O(1)` — Constant extra space.
