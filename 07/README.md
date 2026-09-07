# Pattern 07: Star Pyramid

## Intuition
We form a centered pyramid of stars. Each row contains increasing stars centered with spaces on both sides. Row `i` (0-indexed) has `N - i - 1` leading spaces, `2 * i + 1` stars, and `N - i - 1` trailing spaces.

## Approach
1. Run an outer loop `i` from `0` to `N-1` for rows.
2. For each row, print `N - i - 1` leading spaces for centering.
3. Print `2 * i + 1` stars in the middle.
4. Print `N - i - 1` trailing spaces for symmetry.
5. Move to the next line after each row.

## Complexity
- **Time Complexity:** `O(N²)` — Nested loops iterate through pyramid elements.
- **Space Complexity:** `O(1)` — Constant extra space.
