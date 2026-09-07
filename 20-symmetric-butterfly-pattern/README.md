# Pattern 20: Symmetric Butterfly Pattern

## 💡 Intuition
In this pattern, we create a butterfly shape using stars. The butterfly wings grow outward from row 1 to $N$, meet at the middle, and then shrink back down from row $N + 1$ to $2N - 1$.

## 🛠️ Approach
1. Initialize `spaces = 2 * N - 2`.
2. Run a loop $i$ from $1$ to $2N - 1$.
3. Calculate stars for row $i$:
   - If $i \le N$, then $\text{stars} = i$.
   - Else, $\text{stars} = 2N - i$.
4. Print $\text{stars}$ stars, followed by `spaces` spaces, followed by $\text{stars}$ stars.
5. If $i < N$, decrement `spaces` by 2; otherwise, increment `spaces` by 2.
6. Move to the next line after each row.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, as $2N - 1$ rows each print $2N$ characters.
- **Space Complexity:** $O(1)$, as only loop variables are used.
