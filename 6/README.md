This pattern looks similar to an inverted right-angled triangle, but instead of stars, we print numbers. Each row starts from 1 and continues up to N - i, where i is the current row index. Thus, the number of elements decreases with each row, creating an inverted triangle of numbers.

1.Run an outer loop (i) from 0 to N-1 for rows.  
2.Inside it, run an inner loop (j) from N down to i+1.  
3.Print numbers starting from 1 to N - i using the formula (N - j + 1).  
4.After finishing each row, print a newline.

Time Complexity: O(N²), because nested loops iterate across the triangular number of elements.  

Space Complexity: O(1), as no extra data structures are used.






