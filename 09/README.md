# Diamond Star Pattern

## Intuition
In this pattern, we print a full diamond shape by combining an upright star pyramid (Pattern 07) and an inverted star pyramid (Pattern 08).

## Approach
1. Upper Half: Loop i from 0 to N - 1. Print (N - i - 1) spaces, (2i + 1) stars, and (N - i - 1) spaces.
2. Lower Half: Loop i from 0 to N - 1. Print i spaces, (2N - (2i + 1)) stars, and i spaces.
3. Move to the next line after each row.

## Complexity Analysis
- **Time Complexity:** O(N^2), as both the upper and lower pyramids take O(N^2) operations.
- **Space Complexity:** O(1), as only loop variables are used.
