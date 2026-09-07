In this pattern, we create a hollow diamond shape. The upper half has decreasing stars on sides, and the lower half has increasing stars on sides with space between them.

1.For the upper half (i = 0 to N-1), print (N - i) stars, then (2 _ i) spaces, then (N - i) stars.
2.For the lower half (i = 1 to N), print i stars, then (2 _ (N - i)) spaces, then i stars.
3.Adjust spacing between upper and lower halves.
4.Move to the next line after each row.

Time Complexity: O(N²), because nested loops iterate through O(N²) elements.


Space Complexity: O(1), as only loop variables are used.









