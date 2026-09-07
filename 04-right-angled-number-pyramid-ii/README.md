# Pattern 04: Right-Angled Number Pyramid - II

## 💡 Intuition
Instead of printing increasing numbers from $1$ to $i$ in each row, we print the row number $i$ itself repeatedly $i$ times. Row 1 has `1`, row 2 has `2 2`, row 3 has `3 3 3`, and so on.

## 🛠️ Approach
1. Use an outer loop $i$ from $1$ to $N$ for rows.
2. For each row, use an inner loop $j$ from $1$ to $i$.
3. Print $i$ (the current row number) in each inner loop iteration.
4. After completing one row, move to the next line.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, because of the nested loop structure running $N(N+1)/2$ total operations.
- **Space Complexity:** $O(1)$, as only loop variables are used.
