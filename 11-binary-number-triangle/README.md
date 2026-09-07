# Pattern 11: Binary Number Triangle

## 💡 Intuition
In this pattern, we create a binary alternating triangle. Each row contains alternating `0`s and `1`s, starting with `1` if the row index is even, and `0` if the row index is odd.

## 🛠️ Approach
1. Run an outer loop $i$ from $0$ to $N - 1$ for rows.
2. For each row, determine the starting value: `1` if $i$ is even, `0` if $i$ is odd.
3. Run an inner loop $j$ from $0$ to $i$, appending/printing the current value and toggling it ($1 - \text{start}$).
4. After each row, move to the next line.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, because the nested loops iterate through $\frac{N(N+1)}{2}$ elements.
- **Space Complexity:** $O(1)$, as only loop variables are used.
