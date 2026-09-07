# Pattern 22: Concentric Square Number Pattern

## Intuition
A `(2*N - 1) x (2*N - 1)` grid of concentric numerical squares. Numbers decrease towards the center, where the value at position `(i, j)` is `N - min(top, bottom, left, right)`.

## Approach
1. Run nested loops for `i` from `0` to `2*N - 2` and `j` from `0` to `2*N - 2`.
2. Calculate distances to all four borders:
   - `top = i`, `left = j`, `bottom = (2*N - 2) - i`, `right = (2*N - 2) - j`
3. Compute `min_dist = min(top, bottom, left, right)`.
4. Print `N - min_dist` followed by a space.
5. After each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Grid contains `(2*N - 1)²` elements.
- **Space Complexity:** `O(1)` — Constant extra space.
