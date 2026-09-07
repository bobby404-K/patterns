# Alpha-Triangle Pattern

## Intuition
In this pattern, each row i begins with the (N - i)-th letter of the alphabet and prints consecutive letters up to the N-th letter.

## Approach
1. Run an outer loop i from 0 to N - 1 for rows.
2. For each row, loop ch from ord('A') + N - 1 - i to ord('A') + N - 1.
3. Print chr(ch) followed by a space.
4. After each row, move to the next line.

## Complexity Analysis
- **Time Complexity:** O(N^2), since nested loops iterate through N(N+1)/2 characters.
- **Space Complexity:** O(1), as only loop variables are used.
