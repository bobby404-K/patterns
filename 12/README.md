In this pattern, we create a mirrored number triangle. Each row contains numbers increasing from 1, followed by spaces, then numbers decreasing back to 1.

1.Run an outer loop (i) from 1 to N for rows.
2.For each row, print numbers from 1 to i.
3.Print (2 \* (N - i)) spaces in the middle.
4.Print numbers from i back down to 1.
5.After each row, adjust spacing and move to the next line.

Time Complexity: O(N²), because nested loops iterate through O(N²) elements.

Space Complexity: O(1), as only loop variables are used.











