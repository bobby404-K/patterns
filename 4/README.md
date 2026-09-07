In this pattern, instead of printing increasing numbers from 1 to i in each row, we print the row number itself repeatedly. For example, the first row prints 1, the second row prints 2 2, the third row prints 3 3 3, and so on until N.

1.Use an outer loop (i) from 1 to N for rows.  
2.For each row, use an inner loop (j) from 1 to i.  
3.Instead of printing j, print i (the current row number).  
4.After completing one row, move to the next line.

Time Complexity: O(N²), because there are two nested loops: the outer loop for rows and the inner loop for printing numbers.


Space Complexity: O(1) as only loop variables are used.




