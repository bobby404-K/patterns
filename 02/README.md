# Right-Angled Triangle (Stars)

## Intuition
We need to form a right-angled triangle where the number of stars in each row increases line by line. Row i (0-indexed) contains exactly i + 1 stars.

## Approach
1. Run an outer loop i from 0 to N - 1 for the rows.
2. For each row i, print i + 1 stars.
3. After finishing the stars for a row, move to the next line.

## Complexity Analysis
- **Time Complexity:** O(N^2), as row i prints i + 1 stars, giving N(N+1)/2 total operations.
- **Space Complexity:** O(1), as only loop variables are used.
