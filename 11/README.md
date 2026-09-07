In this pattern, we create a binary alternating triangle. Each row contains alternating 0s and 1s, starting with 1 if the row is even, and 0 if the row is odd.

1.Run an outer loop (i) from 0 to N-1 for rows.
2.For each row, determine the starting value: 1 if i is even, 0 if i is odd.
3.Run an inner loop (j) from 0 to i, printing the current value and toggling between 0 and 1.
4.After each row, move to the next line.

Time Complexity: O(N²), because nested loops iterate through triangular elements.



Space Complexity: O(1), as only loop variables are used.
















