In this pattern, we create a diamond shape using stars. The number of stars increases up to the middle and then decreases symmetrically.

1.Run a loop from i = 1 to 2*N-1.
2.Calculate the number of stars: if i <= N, stars = i; else stars = 2*N - i.
3.Print the calculated number of stars in each row.
4.Move to the next line after each row.

Time Complexity: O(N²), because we print approximately N² total characters.

Space Complexity: O(1), as only loop variables are used.


































