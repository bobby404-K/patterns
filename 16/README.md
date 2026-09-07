In this pattern, we create a letter triangle where each row repeats the same letter i times, with letters increasing for each row.

1.Run an outer loop (i) from 0 to N-1 for rows.
2.Get the character corresponding to the i-th letter (A, B, C, ...).
3.Run an inner loop (j) from 0 to i and print the same character.
4.After each row, move to the next line.

Time Complexity: O(N²), because nested loops iterate through triangular elements.

Space Complexity: O(1), as only loop variables are used.











