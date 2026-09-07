# Pattern 01: Rectangular / Square Star Pattern

## Intuition
The task is to print an `N x N` square pattern of stars. Since the number of rows and columns are equal, we can use two nested loops: the outer loop iterates through rows, and the inner loop prints `N` stars per row.

## Approach
1. Take an integer `N` as input to define the size of the square.
2. Use an outer loop `i` from `0` to `N-1` to represent each row.
3. Inside that loop, use an inner loop `j` from `0` to `N-1` to print `*` in the current row.
4. After each inner loop completes, move to the next line.

## Complexity
- **Time Complexity:** `O(N²)` — Two nested loops each running `N` times.
- **Space Complexity:** `O(1)` — Only loop control variables are used.
