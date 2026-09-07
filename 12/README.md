# Pattern 12: Number Crown Pattern

## Intuition
Each row contains numbers increasing from `1` to `i`, followed by a gap of `2 * (N - i)` spaces, and then numbers decreasing from `i` back down to `1`.

## Approach
1. Initialize `spaces = 2 * (N - 1)`.
2. Run an outer loop `i` from `1` to `N` for rows.
3. Print numbers from `1` to `i`.
4. Print `spaces` spaces in the middle.
5. Print numbers from `i` down to `1`.
6. Decrement `spaces -= 2` and move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Nested loops print `2 * N` elements per row.
- **Space Complexity:** `O(1)` — Constant extra space.
