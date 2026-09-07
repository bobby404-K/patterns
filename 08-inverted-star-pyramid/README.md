# Pattern 08: Inverted Star Pyramid

## 💡 Intuition
In this pattern, we form an inverted centered pyramid of stars. Each row $i$ (0-indexed) contains $i$ leading spaces, $(2N - (2i + 1))$ stars, and $i$ trailing spaces.

## 🛠️ Approach
1. Run an outer loop $i$ from $0$ to $N - 1$ for rows.
2. For each row, print $i$ spaces for indentation.
3. Print $(2N - (2i + 1))$ stars in the center.
4. Print $i$ trailing spaces for symmetry.
5. Move to the next line after each row.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, because each row prints up to $(2N - 1)$ characters across $N$ rows.
- **Space Complexity:** $O(1)$, as only loop variables are used.
