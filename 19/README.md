# Symmetric Void Pattern

## Intuition
In this pattern, we create a hollow diamond shape (symmetric void). The upper half has decreasing stars on the borders with growing spaces in between, and the lower half has increasing stars on the borders with shrinking spaces in between.

## Approach
1. Upper Half (i = 0 to N - 1): Print (N - i) stars, 2i spaces, and (N - i) stars.
2. Lower Half (i = 1 to N): Print i stars, 2(N - i) spaces, and i stars.
3. Move to the next line after each row.

## Complexity Analysis
- **Time Complexity:** O(N^2), as both halves process 2N rows of length 2N.
- **Space Complexity:** O(1), as only loop variables are used.
