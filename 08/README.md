# Pattern 08: Inverted Star Pyramid

## Intuition
We form an inverted centered pyramid of stars. Row `i` (0-indexed) has `i` leading spaces, `2 * N - (2 * i + 1)` stars in the middle, and `i` trailing spaces.

## Approach
1. Run an outer loop `i` from `0` to `N-1` for rows.
2. For each row, print `i` leading spaces.
3. Print `2 * N - (2 * i + 1)` stars.
4. Print `i` trailing spaces for symmetry.
5. Move to the next line after each row.

## Complexity
- **Time Complexity:** `O(N²)` — Nested loops iterate through inverted pyramid elements.
- **Space Complexity:** `O(1)` — Constant extra space.
