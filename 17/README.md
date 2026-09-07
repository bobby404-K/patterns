In this pattern, we create a diamond shape using letters. Letters start from A and increase towards the middle, then decrease symmetrically.

1.Run an outer loop (i) from 0 to N-1 for rows.
2.Print (N - i - 1) leading spaces for centering.
3.For each row, start with letter A and increment up to the midpoint, then decrement.
4.Print each letter in sequence.
5.After each row, move to the next line.

Time Complexity: O(N²), because nested loops iterate through O(N²) elements.


Space Complexity: O(1), as only loop variables are used.








