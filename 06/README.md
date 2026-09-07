# Inverted Numbered Right Pyramid

## Intuition
This pattern is an inverted right-angled triangle with numbers. Each row starts from 1 and continues up to N - i, where i is the current row index.

## Approach
1. Run an outer loop i from 0 to N - 1 for rows.
2. Inside it, run an inner loop j from N down to i + 1.
3. Print numbers starting from 1 to N - i using the formula (N - j + 1).
4. After finishing each row, move to the next line.

## Complexity Analysis
- **Time Complexity:** O(N^2), because nested loops iterate across the triangular number of elements.
- **Space Complexity:** O(1), as only loop variables are used.
