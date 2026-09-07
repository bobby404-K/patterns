# Pattern 21: Hollow Rectangle / Square Pattern

## 💡 Intuition
In this pattern, we create a hollow square/rectangle outline of stars. The border cells are filled with stars while the interior cells are empty spaces.

## 🛠️ Approach
1. Run an outer loop $i$ from $0$ to $N - 1$ for rows.
2. For each row, run an inner loop $j$ from $0$ to $N - 1$ for columns.
3. If the current position is on the border ($i = 0$, $j = 0$, $i = N - 1$, or $j = N - 1$), print `*`.
4. Otherwise, print a space ` `.
5. After each row, move to the next line.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, since we iterate through an $N \times N$ matrix.
- **Space Complexity:** $O(1)$, as only loop variables are used.
