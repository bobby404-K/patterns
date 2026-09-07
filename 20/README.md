# Symmetric Butterfly Pattern

## Intuition
In this pattern, we create a butterfly shape using stars. The butterfly wings grow outward from row 1 to N, meet at the middle, and then shrink back down from row N + 1 to 2N - 1.

## Approach
1. Initialize spaces = 2 * N - 2.
2. Run a loop i from 1 to 2N - 1.
3. Calculate stars: if i <= N, stars = i; else stars = 2N - i.
4. Print stars count of '*', then spaces spaces, then stars count of '*'.
5. Adjust spaces (+2 or -2) and move to the next line.

## Complexity Analysis
- **Time Complexity:** O(N^2), as 2N - 1 rows each print 2N characters.
- **Space Complexity:** O(1), as only loop variables are used.
