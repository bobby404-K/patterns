# Pattern 12: Number Crown Pattern

## 💡 Intuition
In this pattern, we create a mirrored number triangle (number crown). Each row contains numbers increasing from $1$ to $i$, followed by spaces, then numbers decreasing from $i$ back to $1$.

## 🛠️ Approach
1. Initialize `spaces = 2 * (N - 1)`.
2. Run an outer loop $i$ from $1$ to $N$ for rows.
3. For each row:
   - Print numbers from $1$ to $i$.
   - Print `spaces` number of spaces in the middle.
   - Print numbers from $i$ down to $1$.
4. Decrease `spaces` by 2 and move to the next line.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, as each row processes $2N$ characters across $N$ rows.
- **Space Complexity:** $O(1)$, as only loop variables are used.
