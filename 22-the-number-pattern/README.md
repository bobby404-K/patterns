# Pattern 22: The Number Pattern (Concentric Square)

## 💡 Intuition
In this pattern, we create a concentric square number matrix of size $(2N - 1) \times (2N - 1)$. Numbers start with $N$ at the outer border and decrease towards $1$ as we move towards the center layers.

## 🛠️ Approach
1. Run nested loops for $i$ from $0$ to $2N - 2$ and $j$ from $0$ to $2N - 2$.
2. For each position $(i, j)$, calculate the minimum distance from all four borders:
   - $\text{top} = i$
   - $\text{left} = j$
   - $\text{bottom} = (2N - 2) - i$
   - $\text{right} = (2N - 2) - j$
3. Compute $\text{min\_dist} = \min(\text{top}, \text{bottom}, \text{left}, \text{right})$.
4. The value at $(i, j)$ is $N - \text{min\_dist}$.
5. Print the value followed by a space, and after each row, move to the next line.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, because nested loops iterate through $(2N - 1)^2 = O(N^2)$ elements.
- **Space Complexity:** $O(1)$, as only loop variables are used.
