#  Pattern Programs in DSA — 22 Patterns

A curated collection of **22 classic pattern-printing programs**, commonly asked in coding interviews and an excellent starting point for anyone beginning their **Data Structures & Algorithms (DSA)** journey.

Pattern problems are one of the best ways to build a strong foundation in **loops, nested iteration, and logical thinking** — core skills that carry over into more advanced DSA topics like recursion, backtracking, and dynamic programming.

---

##  Why This Repository?

-  Beginner-friendly — no prior DSA experience required
-  Covers the most frequently asked pattern problems in interviews
-  Each pattern includes **intuition, approach, and complexity analysis**
-  Helps build intuition for **nested loops and iteration control**
-  A great warm-up before diving into arrays, strings, and recursion

---

##  Patterns Included

| # | Pattern Name | Difficulty |
|---|---------------------------|------------|
| 1 | Square Pattern | Easy |
| 2 | Right-Angled Triangle (Numbers) | Easy |
| 3 | Right-Angled Triangle (Stars) | Easy |
| 4 | Inverted Right-Angled Triangle | Easy |
| 5 | Pyramid Pattern | Easy |
| 6 | Inverted Pyramid Pattern | Easy |
| 7 | Diamond Pattern | Medium |
| 8 | Hollow Square Pattern | Medium |
| 9 | Hollow Triangle Pattern | Medium |
| 10 | Number Triangle (Increasing) | Easy |
| 11 | Number Triangle (Reverse) | Easy |
| 12 | Floyd's Triangle | Easy |
| 13 | Pascal's Triangle | Medium |
| 14 | Butterfly Pattern | Medium |
| 15 | Zig-Zag Pattern | Medium |
| 16 | Alphabet Triangle | Easy |
| 17 | Alphabet Pyramid | Medium |
| 18 | Hollow Diamond Pattern | Medium |
| 19 | Number Pyramid (Repeated Row Number) | Medium |
| 20 | Palindromic Number Pattern | Hard |
| 21 | Spiral Number Pattern | Hard |
| 22 | Sandglass / Hourglass Pattern | Hard |

>  Update the table above with the exact names/order of your 22 implementations.

---

##  Example Patterns many are there 

### 1. Square Pattern

**Intuition:** Since the number of rows and columns are equal, two nested loops suffice — the outer loop for rows and the inner loop for printing `N` stars per row.

**Approach:**
1. Take an integer `N` as input to define the size of the square.
2. Use a loop from `0` to `N-1` to represent each row.
3. Inside that loop, use another loop from `0` to `N-1` to print stars in the current row.
4. Print `"* "` during each inner loop iteration to form the row.
5. After each inner loop completes, move to the next line.

**Complexity:**
- Time: `O(N²)`
- Space: `O(1)`

---

### 2. Right-Angled Triangle (Numbers)

**Intuition:** Each row contains numbers starting from `1` up to the row number — row 1 has `1`, row 2 has `1 2`, row 3 has `1 2 3`, and so on until `N`.

**Approach:**
1. Use an outer loop `i` from `1` to `N` for rows.
2. For each row, use an inner loop `j` from `1` to `i` to print numbers.
3. Each row prints numbers starting from `1` up to the current row index.
4. After printing each row, move to the next line.

**Complexity:**
- Time: `O(N²)`, since the outer loop runs `N` times and the inner loop runs up to `i` times for each row.
- Space: `O(1)`, since only loop variables are used.

---

##  Getting Started

```bash
# Clone the repository
git clone <your-repo-url>

# Navigate into the project
cd pattern-programs

# Run any pattern file
python patternX.py
```

---

##  Who Is This For?

This repository is ideal for:
- Students starting their **DSA/coding interview prep**
- Beginners learning **loops and nested iteration**
- Anyone who wants daily practice with simple, visual problems before moving to arrays, strings, and recursion

---

##  Contributing

Contributions are welcome! If you'd like to add a new pattern or improve an existing solution:
1. Fork the repository
2. Create a new branch (`git checkout -b add-new-pattern`)
3. Commit your changes
4. Open a pull request

---

##  License

This project is open-source and available under the [MIT License](LICENSE).

---

 If you found this helpful for your DSA journey, consider giving the repository a star:)
 
