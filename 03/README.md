# Right-Angled Number Pyramid

## Intuition
We need to print a right-angled triangle where each row contains numbers starting from 1 up to the row number. Row 1 has '1', row 2 has '1 2', row 3 has '1 2 3', and so on up to N.

## Approach
1. Use an outer loop i from 1 to N for rows.
2. For each row, use an inner loop j from 1 to i to print numbers.
3. Print each number j followed by a space.
4. After finishing each row, move to the next line.

## Complexity Analysis
- **Time Complexity:** O(N^2), since the outer loop runs N times and the inner loop runs i times per row.
- **Space Complexity:** O(1), as only loop variables are used.
