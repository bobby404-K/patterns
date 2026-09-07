# Pattern 01: Rectangular Star Pattern

## 💡 Intuition
The task is to print a square/rectangular grid of stars. Since the number of rows and columns are equal to $N$, two nested loops are used: the outer loop handles the rows, and the inner loop prints $N$ stars for each row.

## 🛠️ Approach
1. Take an integer $N$ as input to define the size of the square.
2. Run an outer loop $i$ from $0$ to $N - 1$ for each row.
3. Inside, run an inner loop $j$ from $0$ to $N - 1$ to print stars.
4. Print `*` during each inner loop iteration.
5. After each inner loop completes, move to the next line.

## ⏱️ Complexity Analysis
- **Time Complexity:** $O(N^2)$, since two nested loops iterate $N$ times each.
- **Space Complexity:** $O(1)$, as only loop variables are used.
