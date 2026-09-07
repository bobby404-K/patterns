In this pattern, we create a square outline (hollow square). The border is filled with stars while the interior is empty.

1.Run an outer loop (i) from 0 to N-1 for rows.
2.For each row, run an inner loop (j) from 0 to N-1 for columns.
3.Print a star if the element is on the border (first/last row or first/last column).
4.Otherwise, print a space.
5.After each row, move to the next line.

Time Complexity: O(N²), because nested loops iterate through N² elements.

Space Complexity: O(1),
as only loop variables are used.






