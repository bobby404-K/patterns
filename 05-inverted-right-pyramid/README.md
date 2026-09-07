# Pattern 05: Inverted Right Pyramid (Stars)

## 💡 Intuition
In this pattern, the number of stars decreases in each subsequent row. The first row has $N$ stars, the second row has $N-1$, and so on, until only one star remains in the last row.

## 🛠️ Approach
1. Run an outer loop $i$ from $0$ to $N - 1$ for rows.
2. For each row, run an inner loop $j$ from $N$ down to $i + 1$.
3. Print a star (`*`) in each iteration of the inner loop.
4. After finishing each row, move to the next line.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, since nested loops iterate $\sum_{i=0}^{N-1} (N-i) = O(N^2)$ times.
- **Space Complexity:** $O(1)$, as only loop variables are used.
