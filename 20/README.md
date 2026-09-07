In this pattern, we create a diamond outline using stars. The diamond grows from the top to the middle and shrinks from the middle to the bottom.

1.Initialize spaces = 2 * N - 2.
2.Run a loop from i = 1 to 2*N-1.
3.Calculate stars: if i <= N, stars = i; else stars = 2\*N - i.
4.Print stars, then spaces in the middle, then stars again.
5.Update spacing and move to the next line.

Time Complexity: O(N²), because nested loops iterate through O(N²) elements.

Space Complexity: O(1), as only loop variables are used.
















