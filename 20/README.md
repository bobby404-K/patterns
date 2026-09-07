# Pattern 20: Butterfly Star Pattern

## Intuition
A symmetric butterfly outline made of stars. The wing width grows from the top to the middle (`N` rows) and shrinks from the middle to the bottom.

## Approach
1. Initialize `spaces = 2 * N - 2`.
2. Run a loop `i` from `1` to `2 * N - 1`.
3. Calculate stars: `stars = i if i <= N else 2 * N - i`.
4. Print `stars` stars, `spaces` spaces, and `stars` stars.
5. If `i < N`, `spaces -= 2`, else `spaces += 2`.

## Complexity
- **Time Complexity:** `O(N²)` — `2*N - 1` rows each printing `2*N` characters.
- **Space Complexity:** `O(1)` — Constant extra space.
