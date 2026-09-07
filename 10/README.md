# Pattern 10: Half Diamond Star Pattern

## Intuition
In this pattern, we create a right-facing half diamond (or rotated triangle) of stars. The number of stars increases up to the middle row `N` and then decreases symmetrically back to 1.

## Approach
1. Run a loop from `i = 1` to `2 * N - 1`.
2. Calculate the number of stars for row `i`:
   - If `i <= N`: `stars = i`
   - Else: `stars = 2 * N - i`
3. Print `stars` stars in the current row.
4. Move to the next line after each row.

## Complexity
- **Time Complexity:** `O(N²)` — Loop runs `2*N - 1` times printing up to `N` stars.
- **Space Complexity:** `O(1)` — Constant extra space.
