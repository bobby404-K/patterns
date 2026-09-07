# Pattern 18: Alpha-Triangle Pattern

## 💡 Intuition
In this pattern, each row $i$ begins with the $(N - i)$-th letter of the alphabet and prints consecutive letters up to the $N$-th letter. For $N=5$, row 1 prints `E`, row 2 prints `D E`, and so on.

## 🛠️ Approach
1. Run an outer loop $i$ from $0$ to $N - 1$ for rows.
2. For each row, loop `ch` from $\text{ord}('A') + N - 1 - i$ to $\text{ord}('A') + N - 1$.
3. Print `chr(ch)` followed by a space.
4. After each row, move to the next line.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, since nested loops iterate through $\frac{N(N+1)}{2}$ characters.
- **Space Complexity:** $O(1)$, as only loop variables are used.
