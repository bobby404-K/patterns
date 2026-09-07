# Pattern 19: Symmetric Void Pattern

## Intuition
A symmetric shape with stars on the edges and a hollow diamond void in the center. The upper half has decreasing stars with expanding void, and the lower half has increasing stars with closing void.

## Approach
1. **Upper Half:**
   - `iniS = 0`
   - For `i` from `0` to `N-1`: print `N - i` stars, `iniS` spaces, and `N - i` stars. Increment `iniS += 2`.
2. **Lower Half:**
   - `iniS = 2 * N - 2`
   - For `i` from `1` to `N`: print `i` stars, `iniS` spaces, and `i` stars. Decrement `iniS -= 2`.

## Complexity
- **Time Complexity:** `O(N²)` — Two halves of `N` rows each printing `2 * N` characters.
- **Space Complexity:** `O(1)` — Constant extra space.
