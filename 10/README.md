# Half Diamond Star Pattern

## Intuition
In this pattern, we create a half diamond shape using stars. The number of stars increases from 1 up to N in the first half, and then decreases from N - 1 down to 1 in the second half.

## Approach
1. Run a loop i from 1 to 2N - 1.
2. Calculate stars: if i <= N, stars = i; else stars = 2N - i.
3. Print stars count of '*' characters.
4. Move to the next line after each row.

## Complexity Analysis
- **Time Complexity:** O(N^2), because total characters printed across 2N - 1 rows is N^2.
- **Space Complexity:** O(1), as only loop variables are used.
