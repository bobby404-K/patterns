# Pattern 14: Increasing Letter Triangle

## 💡 Intuition
In this pattern, we create an alphabetical triangle where each row contains letters starting from `A` up to the $(i+1)$-th letter.

## 🛠️ Approach
1. Run an outer loop $i$ from $0$ to $N - 1$ for rows.
2. For each row, run an inner loop $j$ from $0$ to $i$.
3. Print the character corresponding to `chr(65 + j)` (`A`, `B`, `C`, ...) followed by a space.
4. After each row, move to the next line.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, because nested loops iterate through $\frac{N(N+1)}{2}$ characters.
- **Space Complexity:** $O(1)$, as only loop variables are used.
