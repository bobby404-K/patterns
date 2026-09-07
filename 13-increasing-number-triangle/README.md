# Pattern 13: Increasing Number Triangle (Floyd's Triangle)

## 💡 Intuition
In this pattern, consecutive integers are printed in increasing order starting from $1$ in a triangular layout.

## 🛠️ Approach
1. Initialize a counter `num = 1`.
2. Run an outer loop $i$ from $1$ to $N$ for rows.
3. For each row, run an inner loop $j$ from $1$ to $i$.
4. Print the current value of `num` followed by a space, and increment `num` by 1.
5. After each row, move to the next line.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, because total elements printed is $\frac{N(N+1)}{2}$.
- **Space Complexity:** $O(1)$, as only loop variables and a scalar counter are used.
