In this pattern, we create an inverted letter triangle where each row contains the last N - i letters of the alphabet.

1.Run an outer loop (i) from 0 to N-1 for rows.
2.For each row, start from the (N - i)-th letter and print up to the N-th letter.
3.Print each letter in the range.
4.After each row, move to the next line.

Time Complexity: O(N²), because nested loops iterate through triangular elements.

Space Complexity: O(1), as only loop variables are used.






