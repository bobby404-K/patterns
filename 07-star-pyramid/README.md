# Pattern 07: Star Pyramid

## 💡 Intuition
In this pattern, we form a centered pyramid of stars. Each row $i$ (0-indexed) contains $(N - i - 1)$ leading spaces, $(2i + 1)$ stars, and $(N - i - 1)$ trailing spaces.

## 🛠️ Approach
1. Run an outer loop $i$ from $0$ to $N - 1$ for rows.
2. For each row, print $(N - i - 1)$ spaces for left alignment.
3. Print $(2i + 1)$ stars in the middle.
4. Print $(N - i - 1)$ trailing spaces for symmetry.
5. Move to the next line after each row.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, since we have nested iterations totaling $(2N-1)$ characters per row over $N$ rows.
- **Space Complexity:** $O(1)$, as only loop variables are used.
