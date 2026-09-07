In this pattern, we print a triangle of repeated numbers. Each row i prints the number i repeated i times.

1.Run an outer loop (i) from 1 to N for rows.
2.For each row, run an inner loop (j) from 1 to i.
3.Instead of printing j, print i (the current row number) repeatedly.
4.After completing each row, move to the next line.

Time Complexity: O(N²), because nested loops iterate through triangular elements.


Space Complexity: O(1), as only loop variables are used.






