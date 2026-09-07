We need to print a right-angled triangle where each row contains numbers starting from 1 up to the row number. So, the first row has 1, the second row has 1 2, the third row has 1 2 3, and so on until N.

1.Use an outer loop (i) from 1 to N for rows.  
2.For each row, use an inner loop (j) from 1 to i to print numbers.  
3.Each row prints numbers starting from 1 up to the current row index.  
4.After printing each row, move to the next line.

Time Complexity: O(N²), because the outer loop runs N times and the inner loop runs up to i times for each row.


Space Complexity: O(1), since only loop variables are used




