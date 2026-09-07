

In this pattern, we create an inverted letter triangle. Each row starts from A and continues up to (N - i) letters.

1.Run an outer loop (i) from 0 to N-1 for rows.
2.For each row, run an inner loop (j) from 0 to (N - i - 1).
3.Print the j-th letter (A, B, C, ...) for each column.
4.After each row, move to the next line.
5.The time Complexity and the space Complexity is given below. 

Time Complexity: O(N²), because nested loops iterate through triangular elements.




















Space Complexity: O(1), as only loop variables are used.















