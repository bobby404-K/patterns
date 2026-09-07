# Pattern 17: Alpha-Hill Pattern

## Intuition
A centered pyramid formed with letters. Letters start from `A`, increase towards the midpoint, and then decrease symmetrically back to `A`.

## Approach
1. Run an outer loop `i` from `0` to `N-1` for rows.
2. Print `N - i - 1` leading spaces for centering.
3. Start with `ch = ord('A')` and midpoint breakpoint `(2 * i + 1) // 2`.
4. For column `j` from `1` to `2 * i + 1`:
   - Print `chr(ch)`
   - If `j <= breakpoint`, `ch += 1`, else `ch -= 1`.
5. After each row, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Nested loops iterate through pyramid elements.
- **Space Complexity:** `O(1)` — Constant extra space.
