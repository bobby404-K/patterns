# Pattern 16: Alpha-Ramp Pattern

## 💡 Intuition
In this pattern, each row $i$ repeats the same letter $(i+1)$ times, with letters advancing alphabetically row by row (`A`, `B B`, `C C C`, ...).

## 🛠️ Approach
1. Run an outer loop $i$ from $0$ to $N - 1$ for rows.
2. Get the character `ch = chr(65 + i)` corresponding to the current row.
3. Run an inner loop $(i+1)$ times and print `ch` followed by a space.
4. After each row, move to the next line.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, because nested loops iterate through $\frac{N(N+1)}{2}$ characters.
- **Space Complexity:** $O(1)$, as only loop variables are used.
