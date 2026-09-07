In this pattern, we create a concentric square pattern. Numbers decrease as we move towards the center, creating nested square layers.

1.Run nested loops for i from 0 to 2*N-2 and j from 0 to 2*N-2.
2.For each position, calculate the minimum distance from all four borders.
3.The value at each position is N minus this minimum distance.
4.Print the value for each position.
5.After each row, move to the next line.

Time Complexity: O(N²), because nested loops iterate through (2\*N-1)² elements.

Space Complexity: O(1), as only loop variables are used.




