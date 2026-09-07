# Reverse Letter Triangle

## Intuition
In this pattern, we create an inverted letter triangle. Each row starts from 'A' and continues up to (N - i) letters.

## Approach
1. Run an outer loop i from 0 to N - 1 for rows.
2. For each row, run an inner loop j from 0 to N - i - 1.
3. Print chr(65 + j) ('A', 'B', 'C', ...) followed by a space.
4. After each row, move to the next line.

## Complexity Analysis
- **Time Complexity:** O(N^2), because nested loops iterate through N(N+1)/2 characters.
- **Space Complexity:** O(1), as only loop variables are used.
