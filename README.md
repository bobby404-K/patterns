# 🌟 Pattern Programs in DSA — Complete 22 Patterns

A comprehensive, curated collection of **22 classic pattern-printing problems** implemented in Python. These problems are standard warmup questions in **Data Structures & Algorithms (DSA)** interviews and coding rounds.

Pattern problems build a rock-solid mental model for **nested iteration, index arithmetic, 2D coordinate calculations, and conditional logic** — foundational skills for matrices, recursion, backtracking, and dynamic programming.

---

## 🚀 Why This Repository?

- 🎯 **Complete Striver A2Z Pattern Series**: Covers all 22 fundamental pattern problems.
- 📂 **Zero-Padded Folder Structure (`01`–`22`)**: Eliminates lexicographical sorting bugs in GitHub and IDE file trees.
- 💡 **Intuition & Complexity Analysis**: Every pattern folder includes a dedicated `README.md` breaking down the intuition, step-by-step approach, time complexity, and space complexity.
- 🖼️ **Visual Reference**: Includes diagrams/output previews for quick visual recall.

---

## 📋 Patterns Catalog

| # | Folder | Pattern Name | Difficulty | Visual Preview |
|:---:|:---:|:---|:---:|:---|
| 01 | [`01`](./01) | **Rectangular / Square Star Pattern** | `Easy` | `* * * *`<br>`* * * *`<br>`* * * *`<br>`* * * *` |
| 02 | [`02`](./02) | **Right-Angled Star Triangle** | `Easy` | `*`<br>`* *`<br>`* * *`<br>`* * * *` |
| 03 | [`03`](./03) | **Right-Angled Number Triangle** | `Easy` | `1`<br>`1 2`<br>`1 2 3`<br>`1 2 3 4` |
| 04 | [`04`](./04) | **Repeated Row Number Triangle** | `Easy` | `1`<br>`2 2`<br>`3 3 3`<br>`4 4 4 4` |
| 05 | [`05`](./05) | **Inverted Right-Angled Star Triangle** | `Easy` | `* * * *`<br>`* * *`<br>`* *`<br>`*` |
| 06 | [`06`](./06) | **Inverted Right-Angled Number Triangle** | `Easy` | `1 2 3 4`<br>`1 2 3`<br>`1 2`<br>`1` |
| 07 | [`07`](./07) | **Star Pyramid** | `Easy` | `   *   `<br>`  ***  `<br>` ***** `<br>`*******` |
| 08 | [`08`](./08) | **Inverted Star Pyramid** | `Easy` | `*******`<br>` ***** `<br>`  ***  `<br>`   *   ` |
| 09 | [`09`](./09) | **Diamond Star Pattern** | `Medium` | `   *   `<br>`  ***  `<br>` ***** `<br>`*******`<br>`*******`<br>` ***** `<br>`  ***  `<br>`   *   ` |
| 10 | [`10`](./10) | **Half Diamond Star Pattern** | `Medium` | `*`<br>`**`<br>`***`<br>`****`<br>`***`<br>`**`<br>`*` |
| 11 | [`11`](./11) | **Binary Alternating Triangle** | `Easy` | `1`<br>`0 1`<br>`1 0 1`<br>`0 1 0 1` |
| 12 | [`12`](./12) | **Number Crown / Mirrored Triangle** | `Medium` | `1      1`<br>`12    21`<br>`123  321`<br>`12344321` |
| 13 | [`13`](./13) | **Floyd's Triangle** | `Easy` | `1`<br>`2 3`<br>`4 5 6`<br>`7 8 9 10` |
| 14 | [`14`](./14) | **Increasing Letter Triangle** | `Easy` | `A`<br>`A B`<br>`A B C`<br>`A B C D` |
| 15 | [`15`](./15) | **Inverted Letter Triangle** | `Easy` | `A B C D`<br>`A B C`<br>`A B`<br>`A` |
| 16 | [`16`](./16) | **Alpha-Ramp Pattern** | `Easy` | `A`<br>`B B`<br>`C C C`<br>`D D D D` |
| 17 | [`17`](./17) | **Alpha-Hill Pattern** | `Medium` | `   A   `<br>`  ABA  `<br>` ABCBA `<br>`ABCDCBA` |
| 18 | [`18`](./18) | **Alpha-Triangle Pattern** | `Medium` | `D`<br>`C D`<br>`B C D`<br>`A B C D` |
| 19 | [`19`](./19) | **Symmetric Void Pattern** | `Hard` | `********`<br>`***  ***`<br>`**    **`<br>`*      *`<br>`*      *`<br>`**    **`<br>`***  ***`<br>`********` |
| 20 | [`20`](./20) | **Butterfly Star Pattern** | `Hard` | `*      *`<br>`**    **`<br>`***  ***`<br>`********`<br>`***  ***`<br>`**    **`<br>`*      *` |
| 21 | [`21`](./21) | **Hollow Square Star Pattern** | `Medium` | `****`<br>`*  *`<br>`*  *`<br>`****` |
| 22 | [`22`](./22) | **Concentric Square Number Pattern** | `Hard` | `4 4 4 4 4 4 4`<br>`4 3 3 3 3 3 4`<br>`4 3 2 2 2 3 4`<br>`4 3 2 1 2 3 4`<br>`4 3 2 2 2 3 4`<br>`4 3 3 3 3 3 4`<br>`4 4 4 4 4 4 4` |

---

## 🔍 Pattern Walkthrough Examples

### Example 1: Square Star Pattern (Pattern 01)

**Intuition:** Since the number of rows and columns are equal, two nested loops suffice — the outer loop for rows and the inner loop for printing `N` stars per row.

```python
def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
```

- **Time Complexity:** `O(N²)`
- **Space Complexity:** `O(1)`

---

### Example 2: Right-Angled Star Triangle (Pattern 02)

**Intuition:** Each row `i` (0-indexed) prints exactly `i + 1` stars.

```python
def pattern2(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()
```

- **Time Complexity:** `O(N²)`
- **Space Complexity:** `O(1)`

---

### Example 3: Star Pyramid (Pattern 07)

**Intuition:** For row `i` (0-indexed), print `N - i - 1` leading spaces, `2 * i + 1` stars, and `N - i - 1` trailing spaces.

```python
def pattern7(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1) + " " * (n - i - 1))
```

- **Time Complexity:** `O(N²)`
- **Space Complexity:** `O(1)`

---

## 🛠️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/patterns.git
cd patterns
```

### 2. Run any pattern
To run any pattern solution, navigate into its folder or execute it with Python:

```bash
# Run Pattern 01 (Square Star Pattern)
python 01/one.py

# Run Pattern 08 (Inverted Star Pyramid)
python 08/eight.py

# Run Pattern 22 (Concentric Square Number Pattern)
python 22/twentytwo.py
```

---

## 📁 Repository Structure

```text
patterns/
├── 01/             # Pattern 01: Rectangular / Square Star Pattern
│   ├── one.py
│   ├── one.png
│   └── README.md
├── 02/             # Pattern 02: Right-Angled Star Triangle
│   ├── two.py
│   ├── two.png
│   └── README.md
...
├── 22/             # Pattern 22: Concentric Square Number Pattern
│   ├── twentytwo.py
│   ├── twentytwo.png
│   └── README.md
└── README.md       # Main repository documentation & index
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewPattern`)
3. Commit your Changes (`git commit -m 'Add new pattern solution'`)
4. Push to the Branch (`git push origin feature/NewPattern`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

⭐ If this repository helped you in your DSA journey, don't forget to give it a star!
