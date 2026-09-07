In this pattern, we form a pyramid of stars. Each row contains increasing stars centered with spaces on both sides.

1.Run an outer loop (i) from 0 to N-1 for rows.
2.For each row, print (N - i - 1) leading spaces for centering.
3.Print (2 \* i + 1) stars in the middle.
4.Print (N - i - 1) trailing spaces for symmetry.
5.Move to the next line after each row.

Time Complexity: O(N²), since we have two nested loops iterating through triangular elements.


Space Complexity: O(1), as only loop variables are used.






