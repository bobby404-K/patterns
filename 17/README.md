# Alpha-Hill Pattern

## Intuition
In this pattern, we create a centered pyramid using letters. Letters start from 'A', increment up to the peak of the pyramid, and then decrement symmetrically back down to 'A'.

## Approach
1. Run an outer loop i from 0 to N - 1 for rows.
2. Print (N - i - 1) leading spaces for centering.
3. Determine the midpoint breakpoint as (2i + 1) // 2.
4. Loop j from 1 to 2i + 1: print chr(ch), then increment or decrement ch based on the breakpoint.
5. After each row, move to the next line.

## Complexity Analysis
- **Time Complexity:** O(N^2), because each row prints (2N - 1) characters across N rows.
- **Space Complexity:** O(1), as only loop variables are used.
