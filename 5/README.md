In this pattern, the number of stars decreases in each row. The first row has N stars, the second row has N-1, the third has N-2, and so on, until only one star remains in the last row. This creates an inverted right-angled triangle.

Run an outer loop (i) from 0 to N-1 for rows.  
For each row, run an inner loop (j) starting from N down to i+1.  
Print a star (\*) in each iteration of the inner loop.  
After finishing each row, print a newline to move to the next row.

Time Complexity: O(N²), since two nested loops are used.  


Space Complexity: O(1), as no extra data structures are needed.





