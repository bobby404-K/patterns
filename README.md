<div align="center">

# 🌟 Master Pattern Printing in DSA
### 🚀 The Ultimate 22-Pattern Collection for Coding Interviews & Loop Mastery

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![DSA Warmup](https://img.shields.io/badge/DSA-Pattern%20Mastery-FF6F00?style=for-the-badge&logo=codeforces&logoColor=white)](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)
[![Patterns Count](https://img.shields.io/badge/Completed-22%2F22%20Patterns-2ea44f?style=for-the-badge&logo=checkmarx&logoColor=white)](#-complete-patterns-catalog)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

<br/>

> **"If you can control nested loops, you can conquer matrices, recursion, backtracking, and dynamic programming."**

<br/>

[🔥 Features](#-why-this-repository) • [🧠 4-Step Blueprint](#-the-4-step-pattern-solving-blueprint) • [📋 Catalog](#-complete-patterns-catalog) • [✨ Highlights](#-featured-pattern-highlights) • [⚡ Quick Start](#-quick-start)

</div>

---

## 📊 Repository At A Glance

<div align="center">

| 🌟 **Star Patterns** | 🔢 **Number Patterns** | 🔤 **Alphabet Patterns** | ⏱️ **Avg Time Complexity** | 💾 **Space Complexity** |
|:---:|:---:|:---:|:---:|:---:|
| **10 Problems** | **7 Problems** | **5 Problems** | `O(N²)` | `O(1) Aux Space` |

</div>

---

## 💡 Why This Repository?

- 🎯 **100% Striver’s A2Z DSA Pattern Coverage**: Covers every fundamental pattern asked in tech interviews (FAANG, top product & service companies).
- 📁 **Clean Zero-Padded Directory Structure (`01`–`22`)**: No lexicographical sorting bugs in GitHub or VS Code file trees.
- 📘 **Deep-Dive Explanations**: Every folder features an individual `README.md` with:
  - 🧠 **Intuition & Mental Model**
  - 🪜 **Step-by-Step Approach**
  - ⏱️ **Time & Space Complexity Proofs**
  - 🖼️ **Visual Diagrams / Output Previews**
- ⚡ **Production-Ready Python Implementations**: Clean, readable, and idiomatic Python 3 code with interactive inputs.

---

## 🧠 The 4-Step Pattern Solving Blueprint

Every pattern problem, no matter how intimidating, boils down to these 4 fundamental steps:

```text
┌─────────────────────────────────────────────────────────────┐
│                 THE 4-STEP PATTERN FORMULA                  │
├─────────────────────────────────────────────────────────────┤
│  1. Count Rows           ──▶  Outer loop: for i in range(N) │
│  2. Identify Columns     ──▶  Inner loops: spaces + symbols │
│  3. Find the Math Link   ──▶  Formula relating i and j      │
│  4. Move to Next Line    ──▶  print() after inner loop      │
└─────────────────────────────────────────────────────────────┘
```

1. **Outer Loop (Rows):** Count the total number of lines. If there are $N$ lines, loop from `0` to `N-1` or `1` to `N`.
2. **Inner Loops (Columns & Spaces):** Break each row down into **Leading Spaces** $\rightarrow$ **Characters / Numbers / Stars** $\rightarrow$ **Trailing Spaces**.
3. **Connect with Formulas:** Express the number of spaces and characters in terms of the row index `i` and input `N`.
4. **Row Termination:** Print a newline `print()` after completing the elements of the row.

---

## 📋 Complete Patterns Catalog

<details open>
<summary><b>🌟 Star Patterns (10 Patterns)</b></summary>

| # | Folder | Pattern Name | Difficulty | Code | Solution Docs | Visual Preview |
|:---:|:---:|:---|:---:|:---:|:---:|:---|
| **01** | [`01`](./01) | **Rectangular / Square Star Pattern** | `🟢 Easy` | [one.py](./01/one.py) | [Notes](./01/README.md) | `****`<br>`****`<br>`****`<br>`****` |
| **02** | [`02`](./02) | **Right-Angled Star Triangle** | `🟢 Easy` | [two.py](./02/two.py) | [Notes](./02/README.md) | `*`<br>`**`<br>`***`<br>`****` |
| **05** | [`05`](./05) | **Inverted Star Triangle** | `🟢 Easy` | [five.py](./05/five.py) | [Notes](./05/README.md) | `****`<br>`***`<br>`**`<br>`*` |
| **07** | [`07`](./07) | **Star Pyramid** | `🟢 Easy` | [seven.py](./07/seven.py) | [Notes](./07/README.md) | `   *   `<br>`  ***  `<br>` ***** `<br>`*******` |
| **08** | [`08`](./08) | **Inverted Star Pyramid** | `🟢 Easy` | [eight.py](./08/eight.py) | [Notes](./08/README.md) | `*******`<br>` ***** `<br>`  ***  `<br>`   *   ` |
| **09** | [`09`](./09) | **Diamond Star Pattern** | `🟡 Medium` | [nine.py](./09/nine.py) | [Notes](./09/README.md) | `   *   `<br>`  ***  `<br>`*******`<br>`*******`<br>`  ***  `<br>`   *   ` |
| **10** | [`10`](./10) | **Half Diamond Star Pattern** | `🟡 Medium` | [ten.py](./10/ten.py) | [Notes](./10/README.md) | `*`<br>`**`<br>`***`<br>`****`<br>`***`<br>`**`<br>`*` |
| **19** | [`19`](./19) | **Symmetric Void Pattern** | `🔴 Hard` | [nineteen.py](./19/nineteen.py) | [Notes](./19/README.md) | `********`<br>`***  ***`<br>`*      *`<br>`*      *`<br>`***  ***`<br>`********` |
| **20** | [`20`](./20) | **Butterfly Star Pattern** | `🔴 Hard` | [twenty.py](./20/twenty.py) | [Notes](./20/README.md) | `*      *`<br>`**    **`<br>`********`<br>`**    **`<br>`*      *` |
| **21** | [`21`](./21) | **Hollow Square Star Pattern** | `🟡 Medium` | [twentyone.py](./21/twentyone.py) | [Notes](./21/README.md) | `****`<br>`*  *`<br>`*  *`<br>`****` |

</details>

<details open>
<summary><b>🔢 Number Patterns (7 Patterns)</b></summary>

| # | Folder | Pattern Name | Difficulty | Code | Solution Docs | Visual Preview |
|:---:|:---:|:---|:---:|:---:|:---:|:---|
| **03** | [`03`](./03) | **Right-Angled Number Triangle** | `🟢 Easy` | [three.py](./03/three.py) | [Notes](./03/README.md) | `1`<br>`1 2`<br>`1 2 3`<br>`1 2 3 4` |
| **04** | [`04`](./04) | **Repeated Row Number Triangle** | `🟢 Easy` | [four.py](./04/four.py) | [Notes](./04/README.md) | `1`<br>`2 2`<br>`3 3 3`<br>`4 4 4 4` |
| **06** | [`06`](./06) | **Inverted Number Triangle** | `🟢 Easy` | [six.py](./06/six.py) | [Notes](./06/README.md) | `1 2 3 4`<br>`1 2 3`<br>`1 2`<br>`1` |
| **11** | [`11`](./11) | **Binary Alternating Triangle** | `🟢 Easy` | [eleven.py](./11/eleven.py) | [Notes](./11/README.md) | `1`<br>`0 1`<br>`1 0 1`<br>`0 1 0 1` |
| **12** | [`12`](./12) | **Number Crown / Mirrored Triangle** | `🟡 Medium` | [twelve.py](./12/twelve.py) | [Notes](./12/README.md) | `1      1`<br>`12    21`<br>`123  321`<br>`12344321` |
| **13** | [`13`](./13) | **Floyd's Triangle** | `🟢 Easy` | [thirteen.py](./13/thirteen.py) | [Notes](./13/README.md) | `1`<br>`2 3`<br>`4 5 6`<br>`7 8 9 10` |
| **22** | [`22`](./22) | **Concentric Square Number Pattern** | `🔴 Hard` | [twentytwo.py](./22/twentytwo.py) | [Notes](./22/README.md) | `4 4 4 4 4 4 4`<br>`4 3 3 3 3 3 4`<br>`4 3 2 2 2 3 4`<br>`4 3 2 1 2 3 4` |

</details>

<details open>
<summary><b>🔤 Alphabet & Palindromic Patterns (5 Patterns)</b></summary>

| # | Folder | Pattern Name | Difficulty | Code | Solution Docs | Visual Preview |
|:---:|:---:|:---|:---:|:---:|:---:|:---|
| **14** | [`14`](./14) | **Increasing Letter Triangle** | `🟢 Easy` | [fourteen.py](./14/fourteen.py) | [Notes](./14/README.md) | `A`<br>`A B`<br>`A B C`<br>`A B C D` |
| **15** | [`15`](./15) | **Inverted Letter Triangle** | `🟢 Easy` | [fifteen.py](./15/fifteen.py) | [Notes](./15/README.md) | `A B C D`<br>`A B C`<br>`A B`<br>`A` |
| **16** | [`16`](./16) | **Alpha-Ramp Pattern** | `🟢 Easy` | [sixteen.py](./16/sixteen.py) | [Notes](./16/README.md) | `A`<br>`B B`<br>`C C C`<br>`D D D D` |
| **17** | [`17`](./17) | **Alpha-Hill Pattern** | `🟡 Medium` | [seventeen.py](./17/seventeen.py) | [Notes](./17/README.md) | `   A   `<br>`  ABA  `<br>` ABCBA `<br>`ABCDCBA` |
| **18** | [`18`](./18) | **Alpha-Triangle Pattern** | `🟡 Medium` | [eighteen.py](./18/eighteen.py) | [Notes](./18/README.md) | `D`<br>`C D`<br>`B C D`<br>`A B C D` |

</details>

---

## ✨ Featured Pattern Highlights

### 🔥 1. Concentric Square Number Matrix (Pattern 22)
> **The Boss Level Pattern** — Frequently asked in advanced coding rounds.

```python
def pattern22(n):
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            top = i
            left = j
            bottom = (2 * n - 2) - i
            right = (2 * n - 2) - j
            min_dist = min(top, bottom, left, right)
            print(n - min_dist, end=" ")
        print()
```
💡 **Key Intuition:** Instead of printing by layers, view the grid as coordinate distances to the four borders (`top`, `bottom`, `left`, `right`). The number printed is simply `N - min(distances)`.

---

### 🦋 2. Symmetric Butterfly Pattern (Pattern 20)

```python
def pattern20(n):
    spaces = 2 * n - 2
    for i in range(1, 2 * n):
        stars = i if i <= n else 2 * n - i
        print("*" * stars + " " * spaces + "*" * stars)
        spaces += -2 if i < n else 2
```
💡 **Key Intuition:** Symmetrically expand stars and shrink spaces until row $N$, then invert the transition.

---

### 👑 3. Number Crown Pattern (Pattern 12)

```python
def pattern12(n):
    spaces = 2 * (n - 1)
    for i in range(1, n + 1):
        # Left numbers: 1 to i
        for j in range(1, i + 1): print(j, end="")
        # Middle spaces
        print(" " * spaces, end="")
        # Right numbers: i down to 1
        for j in range(i, 0, -1): print(j, end="")
        print()
        spaces -= 2
```
💡 **Key Intuition:** Combines an increasing triangle, dynamic gap reduction (`spaces -= 2`), and a mirror-reflected decreasing triangle.

---

## ⚡ Quick Start

### 1. Clone & Enter
```bash
git clone https://github.com/namaysingh3925/patterns.git
cd patterns
```

### 2. Run Any Pattern Instantly
No dependencies needed — runs with pure standard Python:

```bash
# Run Pattern 01 (Square Star Pattern)
python 01/one.py

# Run Pattern 17 (Alpha-Hill Pyramid)
python 17/seventeen.py

# Run Pattern 22 (Concentric Number Matrix)
python 22/twentytwo.py
```

---

## 📁 Repository Layout

```text
patterns/
├── 01/                     # Pattern 01: Rectangular Star Pattern
│   ├── one.py              # Python Source Code
│   ├── one.png             # Visual Output Diagram
│   └── README.md           # Intuition, Logic & Complexity
├── 02/ ... 21/             # Patterns 02 through 21
├── 22/                     # Pattern 22: Concentric Number Pattern
│   ├── twentytwo.py
│   ├── twentytwo.png
│   └── README.md
└── README.md               # Main Interactive Documentation Hub
```

---

## 🤝 Contributing

Have an optimization, an alternative language solution (C++, Java, Rust), or a new pattern idea?

1. **Fork** the repo
2. **Branch** out: `git checkout -b feature/cool-new-pattern`
3. **Commit**: `git commit -m 'feat: Add C++ solution for Pattern 22'`
4. **Push**: `git push origin feature/cool-new-pattern`
5. **PR**: Open a Pull Request & get featured!

---

## 🌟 Show Your Support

If this repository helped you level up your loop logic and DSA foundations:
- ⭐ **Star this repository** on GitHub!
- 📢 **Share it** with friends preparing for coding interviews!

<div align="center">

Made with ❤️ for DSA Aspirants & Problem Solvers worldwide.

</div>
